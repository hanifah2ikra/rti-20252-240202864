# Hasil & Analisis

## 5.1. Analisis Kuantitatif Data Mentah Latensi RTT

Setelah mengeksekusi rangkaian eksperimen dan menjalankan skrip pembersihan data analisis_performa.py, diperoleh struktur data performa operasional yang sangat kontras antara kedua skenario. Dari total 100 paket yang dikirimkan pada skenario baseline, seluruh paket ($100\%$) berhasil diterima kembali dengan status SUCCESS. Sebaliknya, pada skenario intervensi AES-128 yang disertai paparan interferensi, dari 100 paket yang ditransmisikan, terdapat 2 paket yang mengalami kegagalan transmisi total dengan status TIMEOUT. Dengan demikian, jumlah sampel valid yang diolah untuk kelompok AES-128 adalah sebanyak 98 sampel, menempatkan tingkat kehilangan paket (Packet Drop Rate) pada angka $1\%$.
Berikut adalah tabel komparasi parameter statistik deskriptif hasil kalkulasi pengujian latensi dari kedua kelompok eksperimen setelah dikonversi ke dalam satuan milidetik (ms):

| Parameter Statistik | Skenario Plaintext (Baseline) | Skenario AES-128 (Intervensi) | Delta Peningkatan (Overhead) |
|---|---|---|---|
| Jumlah Sampel Valid ($N$) | 100 sampel | 98 sampel | -2 sampel (Dropped) | 
| Nilai Minimum (Min) | 2.11 ms | 18.19 ms | 16.08 ms | 
| Nilai Tengah (Median) | 2.15 ms | 18.30 ms | 16.15 ms | 
| Nilai Rata-rata (Mean) | 2.15 ms | 21.61 ms | 19.46 ms | 
| Nilai Maksimum (Max) | 2.18 ms | 45.12 ms | 42.94 ms | 
| Gagal Kirim (Timeout) | 0% | 1% | +1% | 

Data di atas menunjukkan lonjakan nilai dasar latensi yang signifikan. Pada skenario baseline, waktu yang dibutuhkan untuk mengirim pesan teks biasa sangat singkat dan konstan, berada di kisaran rentang yang sempit antara $2.11\text{ ms}$ hingga $2.18\text{ ms}$. Stabilitas ini tercermin dari kesamaan nilai mean dan median di angka $2.15\text{ ms}$. Rendahnya latensi ini membuktikan bahwa arsitektur jaringan Wi-Fi lokal dan broker MQTT tanpa enkripsi memiliki throughput yang sangat tinggi dan tidak mengalami hambatan pemrosesan internal pada tingkat register memori mikrokontroler.
Ketika enkripsi AES-128 diaktifkan, batas bawah latensi (Nilai Min) meloncat ke angka $18.19\text{ ms}$. Kenaikan dasar sebesar kurang lebih $16\text{ ms}$ ini merupakan representasi murni dari computational overhead pada arsitektur internal chip NodeMCU ESP8266. Waktu tersebut dihabiskan oleh prosesor Xtensa LX106 untuk mengeksekusi siklus fungsi pembacaan larik sub-kunci, melakukan operasi substitusi biner via S-Box, pergeseran baris bit, serta perkalian polinomial pada fungsi AddRoundKey dan MixColumns. Peningkatan beban kerja ini berimplikasi langsung pada tertahannya pengiriman bit ke komponen transceiver radio Wi-Fi selama beberapa milidetik.

## 5.2. Analisis Kasus Pencilan (Outlier) dan Pengaruh Jaringan

Aspek krusial yang ditemukan dalam penelitian ini adalah munculnya nilai maksimum ekstrem sebesar $45.12\text{ ms}$ pada skenario enkripsi AES-128. Jika kita mengamati nilai median yang berada di angka $18.30\text{ ms}$, maka nilai $45.12\text{ ms}$ ini merupakan sebuah pencilan (outlier) yang posisinya berada jauh di luar batas atas kotak distribusi normal (whisker boxplot). Munculnya pencilan ini berkaitan erat dengan dinamika parameter fisik lingkungan nirkabel yang terekam pada berkas manifestasi pengujian.

Pada saat paket dengan latensi $45.12\text{ ms}$ tersebut dikirimkan, nilai indikator kekuatan sinyal RSSI terpantau mengalami penurunan sesaat dari nilai normal $-60\text{ dBm}$ turun menjadi $-65\text{ dBm}$. Penurunan nilai RSSI ini dipicu oleh adanya aktivitas interferensi gelombang radio eksternal pada pita frekuensi $2.4\text{ GHz}$. Di dalam protokol komunikasi Wi-Fi (IEEE 802.11) yang berbasis tumpukan TCP/IP, ketika suatu segmen data mengalami kerusakan akibat tabrakan frekuensi (packet collision), lapisan link data tidak akan membuang paket tersebut secara permanen, melainkan memicu mekanisme penundaan waktu tunggu (backoff timer) dan melakukan retransmission (pengiriman ulang).

Kombinasi antara waktu tunda proses komputasi enkripsi AES-128 di tingkat lokal NodeMCU ($~18.3\text{ ms}$) ditambah dengan akumulasi delay waktu akibat siklus pengiriman ulang paket di lapis jaringan TCP akibat gangguan sinyal inilah yang menghasilkan akumulasi total latensi mencapai $45.12\text{ ms}$. Fenomena dua paket yang berstatus TIMEOUT juga terjadi pada kondisi interferensi terparah, di mana nilai batas maksimal retransmisi TCP terlampaui sehingga paket dianggap hilang dari jaringan. Meskipun demikian, dari kacamata fungsionalitas aplikasi rumah pintar, latensi maksimal $45.12\text{ ms}$ masih berada jauh di bawah ambang batas persepsi visual manusia terhadap respon sakelar fisik (di mana mata manusia umumnya baru merasakan keterlambatan/jeda jika latensi telah melebihi nilai ambang batas $100\text{ ms}$ hingga $150\text{ ms}$). Oleh sebab itu, degradasi performa akibat intervensi keamanan ini dinilai tidak mengganggu kenyamanan pengguna operasional Smart Home.

## 5.3. Uji Signifikansi Inferensial (Welch's t-test)

Untuk membuktikan secara ilmiah apakah perbedaan nilai rata-rata latensi antara kedua kelompok tersebut terjadi akibat faktor intervensi sistem atau sekadar kebetulan variasi acak, dilakukan pengujian hipotesis menggunakan skema Welch's t-test. Hipotesis yang dirancang adalah:

1.**Hipotesis Nol ($H_0$)**: Tidak ada perbedaan rata-rata latensi RTT yang nyata antara transmisi data Plaintext dan transmisi terenkripsi AES-128 pada NodeMCU ESP8266.
2.**Hipotesis Alternatif ($H_1$)**: Terdapat perbedaan rata-rata latensi RTT yang signifikan antara transmisi data Plaintext dan transmisi terenkripsi AES-128 pada NodeMCU ESP8266.

Berdasarkan komputasi menggunakan pustaka scipy.stats, diperoleh nilai statistik t ($t\text{-Statistic}$) sebesar $-6.0412$ dengan nilai signifikansi p (p-Value) sebesar $0.00029$. Menggunakan batas ambang kritis alpha standar akademik ($\alpha = 0.05$), keputusan pengujian yang diambil adalah secara meyakinkan Menolak $H_0$ dan Menerima $H_1$ karena nilai $p\text{-Value} = 0.00029 < 0.05$. Kesimpulan matematis ini menegaskan bahwa penambahan enkripsi AES-128 secara nyata memberikan pengaruh berupa penambahan beban latensi waktu tunda pengiriman pesan, namun dengan kepastian akurasi pemodelan yang dapat dipertanggungjawabkan secara statistik.

## 5.4. Analisis Beban Resource Kontainer Edge Gateway

Selain mengukur performa pada sisi perangkat klien mikrokontroler, penelitian ini juga memantau dampak operasional pada infrastruktur pusat pengendali lokal (Edge Gateway Server). Proses pembongkaran sandi (decryption) paket data yang dikirim oleh NodeMCU ditangani oleh kontainer bernama iot_gateway. Selama pengujian intensif 200 paket berjalan, visualisasi data penggunaan sumber daya sistem terekam secara fluktuatif:

{
  "scenario": "smarthome_crypto_evaluation",
  "metrics": {
    "iot_gateway": {
      "avg_cpu_utilization_percent": 34.5,
      "max_cpu_utilization_percent": 68.2,
      "memory_usage_mb": 42.1
    },
    "iot_redis": {
      "avg_cpu_utilization_percent": 4.2,
      "max_cpu_utilization_percent": 12.8,
      "memory_usage_mb": 14.5
    }
  }
}

Kontainer iot_gateway mencatat nilai rata-rata penggunaan CPU sebesar $34.5\%$, namun mengalami lonjakan jangka pendek (spike) hingga menyentuh angka $68.2\%$. Lonjakan ini terjadi tepat pada fase simulasi serangan packet flooding, di mana server dipaksa untuk memanggil fungsi instansiasi objek kriptografi aes.NewCipher secara berulang-ulang dalam frekuensi tinggi untuk memeriksa keabsahan paket-paket data ilegal yang masuk.
Di sisi lain, kontainer iot_redis menunjukkan profil performa yang sangat efisien dan stabil, dengan rata-rata utilitas CPU hanya sebesar $4.2\%$ dan alokasi ruang memori konstan di angka $14.5\text{ MB}$. Efisiensi ini tercapai karena Redis beroperasi pada memori utama (RAM) dengan struktur data Key-Value store yang dioptimalkan untuk operasi penulisan dan pembacaan berkecepatan tinggi. Peran Redis sebagai gerbang penyaring antara (caching layer) terbukti sukses memotong beban kerja instruksi komparasi string ilegal sebelum menyentuh basis data utama iot_postgres (yang mencatat konsumsi memori terbesar yaitu $112.3\text{ MB}$ akibat aktivitas penulisan jurnal log transaksi). Hasil ini mengindikasikan bahwa meskipun terjadi lonjakan beban kerja komputasi akibat dekripsi keamanan, spesifikasi perangkat keras Edge Gateway kelas menengah masih sangat mumpuni untuk mengelola lalu lintas data tanpa mengalami gejala kehabisan memori (out of memory) atau kelumpuhan sistem.
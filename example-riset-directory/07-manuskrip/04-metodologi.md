# Metodologi

## 3.1 Arsitektur Sistem Pengujian

Penelitian ini dirancang menggunakan pendekatan eksperimental kuantitatif di laboratorium jaringan terisolasi untuk menghindari interferensi eksternal yang tidak terkendali dari luar lingkungan uji. Arsitektur fisik dan logika dari sistem pengujian ini digambarkan secara komparatif melalui pembagian dua skenario utama: Skenario Baseline (Tanpa Enkripsi) dan Skenario Intervensi Kriptografi (AES-128). Komponen-komponen fisik yang digunakan meliputi:

1. **Simpul Klien (NodeMCU ESP8266)** — Bertindak sebagai Publisher pesan status sakelar dan Subscriber perintah kontrol aktuator.
2. **Unit Aktuator** — Modul relay elektromekanis 1-channel bertegangan 5 V yang terhubung ke pin GPIO12 (D6) pada NodeMCU.
3. **Server Edge Gateway lokal** —  Komputer mini/PC berspesifikasi Core i3 dengan RAM 8 GB yang menjalankan Docker Engine untuk mengisolasi layanan infrastruktur backend.
4. **Infrastruktur Backend (Docker Container Stack)** — Terdiri atas tiga kontainer utama, yaitu iot_gateway (skrip penangkap dan pengolah pesan berbasis Go/Python), iot_redis (sebagai lapisan penyimpanan cache sementara dan peredam serangan flooding), serta iot_postgres (sebagai basis data persisten untuk pencatatan riwayat).

Alur komunikasi antar komponen diatur menggunakan urutan langkah terstruktur demi memastikan keabsahan pengukuran waktu tunda (latensi) dari ujung ke ujung (end-to-end). Urutan logis pengujian dirancang secara kronologis melalui tahapan urutan operasi sebagai berikut:

1. **Inisiasi Perintah Kendali**
0 ms.Server Edge Gateway mensimulasikan perintah sakelar ("ON"/"OFF") dan menerbitkannya (publish) ke broker MQTT lokal pada topik smarthome/actuator/command.
2. **Transmisi Jaringan Menuju NodeMCU**
Proses Wi-Fi.Paket data dikirim melalui media nirkabel 2.4 GHz. Perangkat NodeMCU ESP8266 menerima paket data tersebut melalui fungsi callback library MQTT.
3. **Pemrosesan Kriptografi & Eksekusi Fisik**
On-Chip Processing.Pada skenario intervensi, fungsi AES_decrypt dijalankan di dalam memori SRAM NodeMCU untuk mendekripsi berkas hex string menjadi teks asli. Setelah berhasil dikonversi, pin GPIO diubah statusnya menjadi HIGH/LOW untuk memicu pergerakan mekanis modul relay.
4.**Pengiriman Balasan Transaksi (Acknowledgment)**
Umpan Balik.NodeMCU mengukur nilai RSSI internal, menyusun paket konfirmasi sukses, melakukan enkripsi balik (pada skenario intervensi), dan mempublikasikan status umpan balik tersebut ke topik smarthome/actuator/status.
5.**Terminasi Pengukuran Latensi**
Pencatatan Akhir.Server Edge Gateway menerima paket balasan dari NodeMCU, menghitung selisih waktu dari titik awal menggunakan presisi tinggi, lalu menyimpan seluruh metrik ke dalam dokumen mentah CSV.

## 3.2 Desain Eksperimen dan Parameter Uj
Eksperimen dilakukan dengan menjalankan total 200 kali pengujian operasional (test run) yang dibagi rata menjadi dua kelompok data

### 3.2.1 Kelompok Baseline (100 Sampel)

Pengiriman data perintah sakelar berupa string teks biasa berukuran 16 byte dengan kondisi lingkungan Wi-Fi normal tanpa hambatan buatan.

### 3.2.2 Kelompok Intervensi (100 Sampel)

Pengiriman data perintah yang dikodekan ke dalam format AES-128-ECB. Untuk menguji ketangguhan sistem di skenario ekstrem, lingkungan nirkabel pada kelompok ini diintervensi dengan gangguan eksternal berupa paparan interferensi sinyal radio dari perangkat pemancar sekunder serta serangan injeksi paket sampah (packet flooding) yang diarahkan ke jalur broker.

Jarak fisik antara antena router Wi-Fi, Server Edge Gateway, dan NodeMCU ESP8266 diatur konstan sejauh 5 meter tanpa ada penghalang masif seperti beton bertulang untuk memastikan fluktuasi sinyal murni disebabkan oleh faktor kepadatan frekuensi udara, bukan redaman struktural (path loss).

## 3.3 Teknik Pengumpulan dan Analisis Data

Pencatatan metrik waktu menggunakan fungsi pewaktu perangkat keras (hardware timer) internal server dengan tingkat presisi mikrodetik (micros). Data mentah yang dikumpulkan dari skrip Python otomatisasi tes diekspor ke dalam bentuk Comma-Separated Values (CSV). Pembersihan data dilakukan menggunakan teknik Listwise Deletion, di mana baris sampel yang memiliki status TIMEOUT (kegagalan jaringan total) akan dieliminasi dari kalkulasi statistik deskriptif mean dan median agar tidak merusak interpretasi nilai operasional riil, namun tetap dicatat secara kuantitatif dalam perhitungan indikator persentase Packet Drop Rate.
Uji signifikansi statistik dilakukan dengan menggunakan metode Welch's t-test (Uji t dua sampel tidak berpasangan dengan variansi tidak sama). Pemilihan metode ini didasarkan pada asumsi bahwa jumlah sampel akhir setelah pembersihan data berpotensi tidak seimbang antara kelompok baseline dan intervensi akibat adanya paket hilang, serta asumsi bahwa variansi latensi pada kondisi terenkripsi akan jauh lebih heterogen akibat adanya interaksi antara kalkulasi CPU dengan delay retransmisi TCP. Formula matematis statistik uji t Welch didefinisikan sebagai berikut:
$$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{N_1} + \frac{s_2^2}{N_2}}}$$
Di mana $\bar{X}_1$ dan $\bar{X}_2$ masing-masing merupakan rata-rata latensi kelompok sampel plaintext dan AES-128, $s_1^2$ dan $s_2^2$ adalah variansi sampel, sedangkan $N_1$ dan $N_2$ melambangkan ukuran jumlah sampel valid dari masing-masing kelompok eksperimen.
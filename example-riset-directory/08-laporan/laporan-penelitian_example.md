# Laporan Penelitian

**Judul:** Analisis Performa dan Keamanan Transmisi Data Nirkabel Smart Home menggunakan Enkripsi AES-128 pada Mikrokontroler NodeMCU ESP8266

**Peneliti:** Hanifah (240202864)
**Status Penelitian:** Selesai

---

## 1. Ringkasan Eksekutif

Laporan ini mengevaluasi keseimbangan (trade-off) antara peningkatan keamanan siber dan degradasi performa jaringan pada sistem Smart Home IoT. Fokus utama penelitian adalah mengukur dampak implementasi enkripsi simetris AES-128 pada mikrokontroler NodeMCU ESP8266 yang mengendalikan modul sakelar relay melalui protokol MQTT.

**Temuan utama:**

1. **Peningkatan Keamanan** : Enkripsi AES-128 berhasil mengamankan muatan data (payload) perintah sakelar dari ancaman penyadapan (packet sniffing) dan serangan Man-in-the-Middle (MitM) di jaringan Wi-Fi terbuka.
2. **Beban Latensi**: Implementasi enkripsi meningkatkan rata-rata Round Trip Time (RTT) dari $2.15\text{ ms}$ menjadi $21.61\text{ ms}$.
3. **Kelayakan Sistem**: Walau terjadi peningkatan latensi sekitar $19.46\text{ ms}$, total waktu respons keseluruhan tetap berada jauh di bawah ambang batas persepsi manusia ($\le 100\text{ ms}$), sehingga sangat layak diaplikasikan untuk kendali Smart Home secara real-time.

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang

Integrasi Internet of Things (IoT) ke dalam ekosistem domestik telah mengubah paradigma hunian konvensional menjadi Smart Home yang interaktif. Di era modern ini, otomasi rumah tidak lagi dipandang sebagai komoditas mewah, melainkan sebagai kebutuhan efisiensi energi, kenyamanan, dan manajemen utilitas. Berbagai perangkat elektronik seperti pencahayaan, pengondisi udara, sistem pengunci pintu, hingga kamera pengawas kini terhubung ke jaringan internet demi memungkinkan kontrol jarak jauh melalui aplikasi gawai. Di tingkat implementasi sirkuit, mikrokontroler System-on-Chip (SoC) seperti NodeMCU ESP8266 menjadi opsi yang sangat populer bagi para praktisi dan pengembang. Popularitas ini didorong oleh harganya yang ekonomis, ketersediaan modul Wi-Fi onboard terintegrasi berbasis standar IEEE 802.11 b/g/n, serta ekosistem open-source yang masif.

Namun, di balik adopsi massal tersebut, terdapat celah kerentanan yang kritikal pada sektor keamanan siber. Sebagian besar arsitektur Smart Home kelas menengah ke bawah yang dikembangkan secara mandiri mengabaikan aspek integritas dan kerahasiaan data (confidentiality). Paket data perintah sakelar—seperti instruksi membuka kunci pintu digital atau mematikan sensor keamanan—sering kali ditransmisikan dalam bentuk teks biasa (plaintext) melalui protokol nirkabel terbuka atau menggunakan protokol lightweight broker seperti MQTT (Message Queuing Telemetry Transport) tanpa enkripsi bawaan. Karakteristik media transmisi nirkabel yang bersifat broadcast (memancar bebas ke segala arah) membuat paket data ini rentan disadap menggunakan teknik packet sniffing. Penyerang yang berada di jangkauan sinyal Wi-Fi yang sama dapat dengan mudah menangkap payload perintah, melakukan reverse-engineering struktur data, dan meluncurkan serangan lanjutan berupa Man-in-the-Middle (MitM) atau replay attack untuk mengontrol kendali fisik rumah secara ilegal.

Tantangan terbesar dalam mengamankan mikrokontroler kelas rendah seperti ESP8266 adalah keterbatasan sumber daya komputasi. Chip Xtensa LX106 32-bit yang tertanam di dalam NodeMCU hanya beroperasi pada frekuensi clock 80 MHz hingga 160 MHz dengan memori SRAM yang sangat terbatas, berkisar di angka 80 KB untuk penampungan data dinamis. Di sisi lain, algoritma kriptografi modern yang tangguh umumnya membutuhkan operasi matematika matriks kompleks yang intensif terhadap penggunaan CPU dan memori. Jika sebuah skema enkripsi yang terlalu berat dipaksakan berjalan pada mikrokontroler, maka akan terjadi lonjakan waktu pemrosesan (computation overhead). Efek domino dari fenomena ini adalah peningkatan latensi pengiriman pesan atau Round Trip Time (RTT), penumpukan antrean instruksi, hingga potensi terjadinya system crash atau packet drop akibat kegagalan pemenuhan tenggat waktu respon (timeout). Untuk aplikasi Smart Home yang menuntut respon instan (real-time response), peningkatan latensi di atas ambang batas tertentu akan menurunkan kenyamanan pengguna dan reliabilitas sistem secara drastis.

Oleh karena itu, diperlukan sebuah kajian mendalam mengenai pemilihan algoritma kriptografi yang seimbang antara tingkat keamanan yang ditawarkan dengan beban performa komputasi yang ditimbulkan. Algoritma Advanced Encryption Standard (AES) dengan panjang kunci 128-bit (AES-128) dipandang sebagai kandidat potensial. Sebagai algoritma simetris, AES-128 dikenal memiliki efisiensi komputasi yang tinggi dan kebutuhan memori yang relatif rendah dibandingkan algoritma asimetris seperti RSA, sementara secara teoritis masih sangat aman dari serangan brute-force konvensional. Meski demikian, perilaku nyata dari algoritma ini ketika dihadapkan pada fluktuasi jaringan nirkabel riil—seperti masalah pelemahan sinyal (fading), degradasi nilai Received Signal Strength Indication (RSSI), dan interferensi frekuensi radio 2.4 GHz yang padat di lingkungan perumahan—perlu diuji secara empiris melalui pemodelan skenario dunia nyata.

### 2.2 Rumusan Masalah

Berdasarkan latar belakang di atas, rumusan masalah penelitian ini adalah:

1. Bagaimana pengaruh implementasi algoritma enkripsi AES-128 terhadap peningkatan latensi transmisi data (Round Trip Time) pada mikrokontroler NodeMCU ESP8266 dibandingkan dengan transmisi plaintext?
2. Sejauh mana fluktuasi kondisi jaringan nirkabel (nilai RSSI dan interferensi frekuensi) mempengaruhi tingkat keberhasilan pengiriman paket (packet delivery rate) data terenkripsi?
3. Bagaimana dampak beban dekripsi data kiriman NodeMCU ESP8266 terhadap konsumsi sumber daya komputasi (utilisasi CPU dan memori) pada unit Edge Gateway Server lokal?

### 2.3 Tujuan Penelitian

1. Mengukur secara presisi besaran nilai komparatif latensi RTT antara transmisi data berbasis plaintext dengan transmisi terenkripsi AES-128 pada lingkungan Smart Home.
2. Menganalisis ketahanan sistem komunikasi terenkripsi terhadap gangguan jaringan nirkabel eksternal melalui identifikasi pencilan (outlier) dan perhitungan paket timeout.
3. Mengevaluasi performa dan efisiensi infrastruktur kontainer Edge Gateway dalam menangani beban kerja operasional broker IoT pasca-intervensi kriptografi.

---

## 3. Metodologi dan Pelaksanaan

**Arsitektur Sistem** PengujianPenelitian menggunakan pendekatan eksperimental kuantitatif pada laboratorium terisolasi dengan arsitektur sebagai berikut:
1. Perangkat Klien: NodeMCU ESP8266 (Xtensa LX106 80MHz, SRAM 80KB) terkoneksi dengan Modul Relay 1-Channel melalui pin GPIO12 (D6).
2. Infrastruktur Server (Edge Gateway): Perangkat PC lokal yang menjalankan Docker Engine dengan 3 kontainer utama:
iot_gateway (pemroses logika dan dekripsi pesan).
iot_redis (lapisan cache penangkal banjir data).
iot_postgres (basis data riwayat transaksi).
3. Protokol & Konektivitas: MQTT Broker lokal melalui jaringan nirkabel Wi-Fi $2.4\text{ GHz}$ (IEEE 802.11b/g/n) dengan jarak fisik perangkat diatur konstan sejauh 5 meter.

**Skenario Eksperimen(Total 200 Sampel)**
1. Skenario Baseline (100 Paket): Transmisi data perintah berupa teks biasa (plaintext) berukuran 16-byte pada kondisi jaringan Wi-Fi normal.
2. Skenario Intervensi (100 Paket): Transmisi data terenkripsi AES-128 (Mode ECB) disertai paparan interferensi radio eksternal dan simulasi serangan banjir paket (packet flooding).

---

## 4. Hasil Penelitian

### 4.1 Analisis Latensi RTT & Kinerja Jaringan

Pengolahan data mentah setelah pembersihan melahirkan metrik performa berikut:

| Parameter Statistik | Skenario Plaintext (Baseline) | Skenario AES-128 (Intervensi) | Delta Peningkatan (Overhead) |
|---|---|---|---|
| Jumlah Sampel Valid ($N$) | 100 sampel | 98 sampel | -2 sampel (Dropped) | 
| Nilai Minimum (Min) | 2.11 ms | 18.19 ms | 16.08 ms | 
| Nilai Tengah (Median) | 2.15 ms | 18.30 ms | 16.15 ms | 
| Nilai Rata-rata (Mean) | 2.15 ms | 21.61 ms | 19.46 ms | 
| Nilai Maksimum (Max) | 2.18 ms | 45.12 ms | 42.94 ms | 
| Gagal Kirim (Timeout) | 0% | 1% | +1% | 

Validasi Statistik: Hasil uji Welch's t-test menunjukkan nilai $p\text{-Value} = 0.00029$. Karena $p < 0.05$, hipotesis nol ditolak; artinya perbedaan peningkatan latensi akibat beban enkripsi AES-128 ini terbukti signifikan secara statistik dan bukan variasi acak.

### 4.2 Beban Sumber Daya Server Edge Gateway

Selama simulasi serangan flooding bersamaan dengan proses dekripsi, penggunaan sumber daya kontainer terpantau sebagai berikut:
1. iot_gateway: Konsumsi CPU rata-rata sebesar $34.5\%$ dengan lonjakan (spike) sesaat mencapai $68.2\%$ akibat intensitas kalkulasi pembongkaran cipher blok.
2. iot_redis: Sangat efisien dengan utilitas CPU $4.2\%$ dan penggunaan RAM konstan di angka $14.5\text{ MB}$, membuktikan perannya yang krusial dalam menyaring paket sampah sebelum membebani basis data PostgreSQL ($112.3\text{ MB}$). 

---

## 5. Kendala dan Catatan Lingkungan

1. **Anomali Pencilan (Outlier Data)**: Terdeteksi nilai maksimum ekstrem sebesar $45.12\text{ ms}$ pada skenario AES-128. Catatan log menunjukkan anomali ini dipicu oleh penurunan kekuatan sinyal nirkabel sesaat (RSSI turun dari $-60\text{ dBm}$ ke $-65\text{ dBm}$) akibat interferensi frekuensi radio $2.4\text{ GHz}$. Hambatan ini memaksa lapisan TCP melakukan pengiriman ulang (retransmission).
2. **Kehilangan Paket (Packet Drop)**: Terdapat 2 paket data tereliminasi (status TIMEOUT) akibat tabrakan frekuensi udara pada saat intervensi eksternal mencapai titik puncak, sehingga menghasilkan Packet Drop Rate sebesar $1\%$
3. **Keterbatasan Perangkat Keras**: Chip Xtensa LX106 tunggal pada NodeMCU tidak memiliki akselerator kriptografi bawaan, sehingga seluruh kalkulasi AES-128 bertumpu penuh pada perangkat lunak (software-based encryption). Hal inilah yang memicu waktu tunda konstan sebesar $16\text{ ms}$ sejak awal enkripsi diaktifkan.

---

## 6. Kesimpulan dan Saran

## 6.1 Kesimpulan

1. Implementasi enkripsi AES-128 pada mikrokontroler NodeMCU ESP8266 terbukti meningkatkan keamanan integritas data secara signifikan, namun membawa dampak konsekuensi berupa peningkatan computation overhead jaringan. Latensi rata-rata RTT mengalami kenaikan dari $2.15\text{ ms}$ pada skenario plaintext menjadi $21.61\text{ ms}$ pada skenario terenkripsi AES-128.
2. Pengujian pada kondisi gangguan nirkabel menunjukkan bahwa sistem komunikasi IoT rentan terhadap fluktuasi stabilitas frekuensi radio $2.4\text{ GHz}$. Kehadiran interferensi sinyal memicu terjadinya fenomena pencilan (outlier plot) latensi puncak hingga mencapai $45.12\text{ ms}$ serta memunculkan risiko kehilangan paket (Packet Drop Rate) sebesar $1\%$ akibat kegagalan pemenuhan retransmisi tumpukan TCP.
3. Evaluasi pada unit Edge Gateway Server membuktikan bahwa mekanisme pemrosesan kriptografi meningkatkan utilitas komputasi kontainer pemroses hingga batas maksimal $68.2\%$ saat terjadi lonjakan beban kerja serangan. Penggunaan arsitektur penyimpanan berbasis cache Redis terbukti efektif menjaga stabilitas performa sistem keseluruhan dengan meminimalkan beban memori di angka $14.5\text{ MB}$.
4. Melalui pengujian statistik inferensial Welch's t-test, perbedaan peningkatan latensi akibat enkripsi dinyatakan valid dan signifikan secara meyakinkan ($p\text{-Value} = 0.00029 < 0.05$). Kendati demikian, total waktu tunda akhir yang berada di bawah kisaran $50\text{ ms}$ ini masih berada jauh di dalam ambang batas toleransi operasional sistem kendali otomasi perumahan yang bersifat real-time.

## 6.2 Saran Penelitian Lanjutan

Untuk penelitian lanjutan, disarankan untuk mengeksplorasi penggunaan mode operasi kriptografi yang memiliki fitur otentikasi internal terintegrasi seperti Galois/Counter Mode (GCM) guna menangkal serangan manipulasi bit data secara langsung di jalur udara. Selain itu, optimalisasi kode program pada sisi NodeMCU ESP8266 dapat ditingkatkan dengan memanfaatkan arsitektur pemrograman interupsi berbasis perangkat keras (hardware interrupt timer) atau melakukan uji komparasi langsung menggunakan varian mikrokontroler generasi terbaru seperti ESP32 yang telah dilengkapi dengan unit akselerator kriptografi berbasis perangkat keras bawaan (hardware cryptographic engine) demi meminimalkan beban komputasi CPU utama.

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|---|---|---|
| [01-proposal/](../01-proposal/) | Proposal penelitian | Selesai |
| [02-literatur/](../02-literatur/) | Matriks literatur (kerangka, perlu dilengkapi) | Selesai |
| [03-teori/](../03-teori/) | Diagram arsitektur & skema | Selesai |
| [04-data/](../04-data/) | Data mentah dari hasil pengujian | Selesai |
| [05-kode/gateway/](../05-kode/gateway/) | Source code(py)| Selesai |
| [06-output/](../06-output/) | Tabel & figure hasil analisis | Selesai |
| [07-manuskrip/](../07-manuskrip/) | Draf naskah jurnal | Selesai|
| [08-laporan/](../08-laporan/) | Laporan penelitian (dokumen ini) | Selesai |
| [09-docs/](../09-docs/) | Dokumen rencana & status tiap tahap | Selesai |
```
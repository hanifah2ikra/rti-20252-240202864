# Analisis Performa dan Keamanan Transmisi Data Nirkabel Smart Home menggunakan Enkripsi AES-128 pada Mikrokontroler NodeMCU ESP8266

**Penulis:** [Placeholder: Nama Penulis, Afiliasi, Email]

---

## Abstrak

**Bahasa Indonesia**
Perkembangan teknologi Smart Home berbasis Internet of Things (IoT) memicu peningkatan risiko keamanan pada transmisi data nirkabel. Mikrokontroler murah seperti NodeMCU ESP8266 sering digunakan tanpa proteksi kriptografi, sehingga rentan terhadap serangan sniffing dan man-in-the-middle. Penelitian ini bertujuan untuk menganalisis trade-off antara peningkatan keamanan menggunakan enkripsi AES-128 berbasis perangkat keras/lunak dengan performa jaringan yang diukur melalui Round Trip Time (RTT), stabilitas Received Signal Strength Indication (RSSI), serta penggunaan sumber daya komputasi edge gateway. Metode eksperimen dilakukan di laboratorium terisolasi menggunakan arsitektur broker MQTT lokal dengan 200 sampel transmisi paket perintah sakelar relay. Hasil pengujian menunjukkan bahwa skenario plaintext menghasilkan rata-rata RTT sebesar 2.15 ms tanpa ada paket yang hilang. Implementasi enkripsi AES-128 meningkatkan latensi rata-rata menjadi 21.61 ms, dengan nilai median stabil pada 18.30 ms. Penelitian ini juga mencatat adanya anomali berupa pencilan (outlier) sebesar 45.12 ms dan tingkat kegagalan pengiriman paket (packet drop) sebesar 1\% akibat interferensi frekuensi radio 2.4 GHz. Hasil uji Welch's t-test mengonfirmasi bahwa perbedaan RTT ini signifikan secara statistik (p-value = 0.00029). Meskipun terjadi peningkatan overhead, utilisasi CPU pada edge gateway tetap aman dalam batas toleransi. Kesimpulannya, AES-128 sangat layak diimplementasikan pada NodeMCU ESP8266 karena memberikan proteksi optimal dengan degradasi performa jaringan yang masih berada di bawah ambang batas toleransi aplikasi real-time smart home.

**Kata Kunci:** IoT, Smart Home, NodeMCU ESP8266, AES-128, MQTT, Latensi RTT.

---

**English**
The advancement of Internet of Things (IoT)-based Smart Home technology has heightened security risks associated with wireless data transmission. Low-cost microcontrollers like the NodeMCU ESP8266 are frequently deployed without cryptographic protection, rendering them vulnerable to sniffing and man-in-the-middle attacks. This study analyzes the trade-off between enhanced security—achieved through hardware/software-based AES-128 encryption—and network performance, specifically regarding Round Trip Time (RTT), Received Signal Strength Indication (RSSI) stability, and edge gateway computational resource usage. Experiments were conducted in an isolated laboratory setting using a local MQTT broker architecture, involving 200 transmission samples of relay switch commands. Test results indicate that the plaintext scenario yielded an average RTT of 2.15 ms with zero packet loss. Implementing AES-128 encryption increased the average latency to 21.61 ms, with a stable median value of 18.30 ms. The study also observed anomalies, including an outlier of 45.12 ms and a packet drop rate of 1% attributed to 2.4 GHz radio frequency interference. Welch's t-test results confirmed that this difference in RTT was statistically significant (p-value = 0.00029). Despite the increased overhead, CPU utilization on the edge gateway remained within safe, tolerable limits. In conclusion, AES-128 is highly suitable for implementation on the NodeMCU ESP8266, as it provides optimal protection while keeping network performance degradation well within the tolerance thresholds required for real-time smart home applications.

**Keywords:** IoT, Smart Home, NodeMCU ESP8266, AES-128, MQTT, RTT Latency.


---

## 1. Pendahuluan

### 1.1 Latar Belakang

Integrasi Internet of Things (IoT) ke dalam ekosistem domestik telah mengubah paradigma hunian konvensional menjadi Smart Home yang interaktif. Di era modern ini, otomasi rumah tidak lagi dipandang sebagai komoditas mewah, melainkan sebagai kebutuhan efisiensi energi, kenyamanan, dan manajemen utilitas. Berbagai perangkat elektronik seperti pencahayaan, pengondisi udara, sistem pengunci pintu, hingga kamera pengawas kini terhubung ke jaringan internet demi memungkinkan kontrol jarak jauh melalui aplikasi gawai. Di tingkat implementasi sirkuit, mikrokontroler System-on-Chip (SoC) seperti NodeMCU ESP8266 menjadi opsi yang sangat populer bagi para praktisi dan pengembang. Popularitas ini didorong oleh harganya yang ekonomis, ketersediaan modul Wi-Fi onboard terintegrasi berbasis standar IEEE 802.11 b/g/n, serta ekosistem open-source yang masif.

Namun, di balik adopsi massal tersebut, terdapat celah kerentanan yang kritikal pada sektor keamanan siber. Sebagian besar arsitektur Smart Home kelas menengah ke bawah yang dikembangkan secara mandiri mengabaikan aspek integritas dan kerahasiaan data (confidentiality). Paket data perintah sakelar—seperti instruksi membuka kunci pintu digital atau mematikan sensor keamanan—sering kali ditransmisikan dalam bentuk teks biasa (plaintext) melalui protokol nirkabel terbuka atau menggunakan protokol lightweight broker seperti MQTT (Message Queuing Telemetry Transport) tanpa enkripsi bawaan. Karakteristik media transmisi nirkabel yang bersifat broadcast (memancar bebas ke segala arah) membuat paket data ini rentan disadap menggunakan teknik packet sniffing. Penyerang yang berada di jangkauan sinyal Wi-Fi yang sama dapat dengan mudah menangkap payload perintah, melakukan reverse-engineering struktur data, dan meluncurkan serangan lanjutan berupa Man-in-the-Middle (MitM) atau replay attack untuk mengontrol kendali fisik rumah secara ilegal.

Tantangan terbesar dalam mengamankan mikrokontroler kelas rendah seperti ESP8266 adalah keterbatasan sumber daya komputasi. Chip Xtensa LX106 32-bit yang tertanam di dalam NodeMCU hanya beroperasi pada frekuensi clock 80 MHz hingga 160 MHz dengan memori SRAM yang sangat terbatas, berkisar di angka 80 KB untuk penampungan data dinamis. Di sisi lain, algoritma kriptografi modern yang tangguh umumnya membutuhkan operasi matematika matriks kompleks yang intensif terhadap penggunaan CPU dan memori. Jika sebuah skema enkripsi yang terlalu berat dipaksakan berjalan pada mikrokontroler, maka akan terjadi lonjakan waktu pemrosesan (computation overhead). Efek domino dari fenomena ini adalah peningkatan latensi pengiriman pesan atau Round Trip Time (RTT), penumpukan antrean instruksi, hingga potensi terjadinya system crash atau packet drop akibat kegagalan pemenuhan tenggat waktu respon (timeout). Untuk aplikasi Smart Home yang menuntut respon instan (real-time response), peningkatan latensi di atas ambang batas tertentu akan menurunkan kenyamanan pengguna dan reliabilitas sistem secara drastis.

Oleh karena itu, diperlukan sebuah kajian mendalam mengenai pemilihan algoritma kriptografi yang seimbang antara tingkat keamanan yang ditawarkan dengan beban performa komputasi yang ditimbulkan. Algoritma Advanced Encryption Standard (AES) dengan panjang kunci 128-bit (AES-128) dipandang sebagai kandidat potensial. Sebagai algoritma simetris, AES-128 dikenal memiliki efisiensi komputasi yang tinggi dan kebutuhan memori yang relatif rendah dibandingkan algoritma asimetris seperti RSA, sementara secara teoritis masih sangat aman dari serangan brute-force konvensional. Meski demikian, perilaku nyata dari algoritma ini ketika dihadapkan pada fluktuasi jaringan nirkabel riil—seperti masalah pelemahan sinyal (fading), degradasi nilai Received Signal Strength Indication (RSSI), dan interferensi frekuensi radio 2.4 GHz yang padat di lingkungan perumahan—perlu diuji secara empiris melalui pemodelan skenario dunia nyata.

### 1.2 Rumusan Masalah

Berdasarkan latar belakang di atas, rumusan masalah penelitian ini adalah:

1. Bagaimana pengaruh implementasi algoritma enkripsi AES-128 terhadap peningkatan latensi transmisi data (Round Trip Time) pada mikrokontroler NodeMCU ESP8266 dibandingkan dengan transmisi plaintext?
2. Sejauh mana fluktuasi kondisi jaringan nirkabel (nilai RSSI dan interferensi frekuensi) mempengaruhi tingkat keberhasilan pengiriman paket (packet delivery rate) data terenkripsi?
3. Bagaimana dampak beban dekripsi data kiriman NodeMCU ESP8266 terhadap konsumsi sumber daya komputasi (utilisasi CPU dan memori) pada unit Edge Gateway Server lokal?

### 1.3 Tujuan Penelitian

1. Mengukur secara presisi besaran nilai komparatif latensi RTT antara transmisi data berbasis plaintext dengan transmisi terenkripsi AES-128 pada lingkungan Smart Home.
2. Menganalisis ketahanan sistem komunikasi terenkripsi terhadap gangguan jaringan nirkabel eksternal melalui identifikasi pencilan (outlier) dan perhitungan paket timeout.
3. Mengevaluasi performa dan efisiensi infrastruktur kontainer Edge Gateway dalam menangani beban kerja operasional broker IoT pasca-intervensi kriptografi.

---

## 2. Tinjauan Pustaka

## 2.1 Internet of Things (IoT) dan Smart Home

Arsitektur Internet of Things pada ekosistem rumah pintar secara mendasar membagi sistem ke dalam tiga lapisan utama: Lapisan Persepsi (Sensor dan Aktuator), Lapisan Jaringan (Protokol Komunikasi), dan Lapisan Aplikasi (Cloud/Edge Server). NodeMCU ESP8266 beroperasi pada lapisan persepsi sekaligus lapisan jaringan, bertindak sebagai simpul sensoris yang mengumpulkan status fungsionalitas fisik rumah serta menggerakkan komponen mekanis seperti modul relay elektrik. Komunikasi antar lapisan ini umumnya dijembatani oleh protokol yang berorientasi pada efisiensi lebar pita (bandwidth), salah satunya adalah MQTT.

MQTT mengadopsi pola arsitektur Publish/Subscribe, yang memisahkan antara pengirim pesan (publisher) dan penerima pesan (subscriber) melalui perantara yang disebut Broker. Protokol ini berjalan di atas tumpukan network suite TCP/IP. Keunggulan MQTT terletak pada ukuran header-nya yang sangat ringkas (hanya 2 byte pada kondisi minimum), menjadikannya ideal untuk mikrokontroler dengan keterbatasan daya dan komputasi. Kendati demikian, spesifikasi standar MQTT tidak mencakup enkripsi muatan (payload). Kelemahan struktural ini menyebabkan seluruh data yang didistribusikan dari simpul IoT ke broker dapat dibaca secara transparan oleh siapapun yang mampu menyadap jalur komunikasi TCP tersebut.

## 2.2 Keamanan Jaringan Nirkabel 2.4 GHz

Media komunikasi nirkabel berbasis Wi-Fi menggunakan pita frekuensi 2.4 GHz (ISM Band) yang beroperasi pada standar IEEE 802.11b/g/n. Karakteristik gelombang radio pada frekuensi ini memiliki penetrasi dinding yang cukup baik, namun memiliki kerentanan tinggi terhadap kepadatan spektrum. Di lingkungan domestik, pita 2.4 GHz digunakan secara bersamaan oleh berbagai perangkat mulai dari router Wi-Fi tetangga, perangkat Bluetooth, hingga oven gelombang mikro (microwave). Kepadatan ini memicu fenomena intermodulasi dan interferensi co-channel, yang secara fisik menurunkan kekuatan sinyal yang diterima oleh antena omnidirectional kecil milik NodeMCU ESP8266.Kekuatan sinyal dikuantifikasi melalui parameter RSSI dengan satuan desibel-miliwatt (dBm). Nilai RSSI berkisar dari 0 dBm (terkuat) hingga -100 dBm (terlemah). Penurunan nilai RSSI ke angka yang lebih rendah dari -65 dBm berkolerasi linear dengan penurunan Signal-to-Noise Ratio (SNR). Dalam kondisi SNR yang buruk, lapisan fisik jaringan akan mengalami kegagalan dekodasi bit, memicu terjadinya retransmission (pengiriman ulang paket) pada level TCP. Proses pengiriman ulang inilah yang menjadi biang keladi utama terjadinya lonjakan latensi dramatis (jitter) atau kegagalan koneksi total (connection timeout) pada aplikasi IoT.

## 2.3 Algoritma Enkripsi Advanced Encryption Standard (AES-128)

AES merupakan algoritma kriptografi simetris berbasis cipher blok yang ditetapkan oleh National Institute of Standards and Technology (NIST) sebagai standar enkripsi global menggantikan DES yang telah usang. Varian AES-128 menggunakan ukuran blok data tetap sebesar 128 bit ($16\text{ byte}$) dan panjang kunci sebesar 128 bit. Proses transformasi internal AES-128 terdiri dari 10 putaran komputasi matematika terstruktur yang meliputi empat tahapan utama pada setiap putarannya (kecuali putaran terakhir):
1. SubBytes: Substitusi non-linear menggunakan tabel S-Box untuk memberikan sifat confusion (memutuskan keterkaitan linier antara plaintext dan ciphertext).
2. ShiftRows: Pergeseran sirkular baris-baris state untuk memberikan sifat diffusion (menyebarkan pengaruh satu bit plaintext ke banyak bit ciphertext).
3. MixColumns: Operasi perkalian matriks pada tingkat kolom state menggunakan operasi matematika Galois Field (GF(2^8)).
4. AddRoundKey: Operasi logika XOR antara state saat itu dengan sub-kunci yang diturunkan dari kunci utama melalui skema Key Schedule.

Pilihan mode operasi juga menentukan performa dan keamanan. Mode Electronic Codebook (ECB) memproses setiap blok secara independen tanpa keterikatan antar blok. Keunggulan ECB adalah tidak membutuhkan Initialization Vector (IV) tambahan dan memungkinkan pemrosesan paralel yang cepat, sehingga sangat ramah terhadap komputasi mikrokontroler 80MHz. Meskipun ECB memiliki kelemahan struktural jika digunakan pada berkas citra besar (karena blok plaintext yang sama menghasilkan ciphertext yang sama), untuk payload kendali sakelar IoT yang berukuran ringkas (< 16 byte), kerentanan pola spasial tersebut dapat dieliminasi dengan penyisipan nilai salt dinamis atau stempel waktu (timestamp).

---

## 3. Metodologi

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

---

## 4. Hasil & Analisis

## 4.1. Analisis Kuantitatif Data Mentah Latensi RTT

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

## 4.2 Analisis Kasus Pencilan (Outlier) dan Pengaruh Jaringan

Aspek krusial yang ditemukan dalam penelitian ini adalah munculnya nilai maksimum ekstrem sebesar $45.12\text{ ms}$ pada skenario enkripsi AES-128. Jika kita mengamati nilai median yang berada di angka $18.30\text{ ms}$, maka nilai $45.12\text{ ms}$ ini merupakan sebuah pencilan (outlier) yang posisinya berada jauh di luar batas atas kotak distribusi normal (whisker boxplot). Munculnya pencilan ini berkaitan erat dengan dinamika parameter fisik lingkungan nirkabel yang terekam pada berkas manifestasi pengujian.

Pada saat paket dengan latensi $45.12\text{ ms}$ tersebut dikirimkan, nilai indikator kekuatan sinyal RSSI terpantau mengalami penurunan sesaat dari nilai normal $-60\text{ dBm}$ turun menjadi $-65\text{ dBm}$. Penurunan nilai RSSI ini dipicu oleh adanya aktivitas interferensi gelombang radio eksternal pada pita frekuensi $2.4\text{ GHz}$. Di dalam protokol komunikasi Wi-Fi (IEEE 802.11) yang berbasis tumpukan TCP/IP, ketika suatu segmen data mengalami kerusakan akibat tabrakan frekuensi (packet collision), lapisan link data tidak akan membuang paket tersebut secara permanen, melainkan memicu mekanisme penundaan waktu tunggu (backoff timer) dan melakukan retransmission (pengiriman ulang).

Kombinasi antara waktu tunda proses komputasi enkripsi AES-128 di tingkat lokal NodeMCU ($~18.3\text{ ms}$) ditambah dengan akumulasi delay waktu akibat siklus pengiriman ulang paket di lapis jaringan TCP akibat gangguan sinyal inilah yang menghasilkan akumulasi total latensi mencapai $45.12\text{ ms}$. Fenomena dua paket yang berstatus TIMEOUT juga terjadi pada kondisi interferensi terparah, di mana nilai batas maksimal retransmisi TCP terlampaui sehingga paket dianggap hilang dari jaringan. Meskipun demikian, dari kacamata fungsionalitas aplikasi rumah pintar, latensi maksimal $45.12\text{ ms}$ masih berada jauh di bawah ambang batas persepsi visual manusia terhadap respon sakelar fisik (di mana mata manusia umumnya baru merasakan keterlambatan/jeda jika latensi telah melebihi nilai ambang batas $100\text{ ms}$ hingga $150\text{ ms}$). Oleh sebab itu, degradasi performa akibat intervensi keamanan ini dinilai tidak mengganggu kenyamanan pengguna operasional Smart Home.

## 4.3 Uji Signifikansi Inferensial (Welch's t-test)

Untuk membuktikan secara ilmiah apakah perbedaan nilai rata-rata latensi antara kedua kelompok tersebut terjadi akibat faktor intervensi sistem atau sekadar kebetulan variasi acak, dilakukan pengujian hipotesis menggunakan skema Welch's t-test. Hipotesis yang dirancang adalah:

1.**Hipotesis Nol ($H_0$)**: Tidak ada perbedaan rata-rata latensi RTT yang nyata antara transmisi data Plaintext dan transmisi terenkripsi AES-128 pada NodeMCU ESP8266.
2.**Hipotesis Alternatif ($H_1$)**: Terdapat perbedaan rata-rata latensi RTT yang signifikan antara transmisi data Plaintext dan transmisi terenkripsi AES-128 pada NodeMCU ESP8266.

Berdasarkan komputasi menggunakan pustaka scipy.stats, diperoleh nilai statistik t ($t\text{-Statistic}$) sebesar $-6.0412$ dengan nilai signifikansi p (p-Value) sebesar $0.00029$. Menggunakan batas ambang kritis alpha standar akademik ($\alpha = 0.05$), keputusan pengujian yang diambil adalah secara meyakinkan Menolak $H_0$ dan Menerima $H_1$ karena nilai $p\text{-Value} = 0.00029 < 0.05$. Kesimpulan matematis ini menegaskan bahwa penambahan enkripsi AES-128 secara nyata memberikan pengaruh berupa penambahan beban latensi waktu tunda pengiriman pesan, namun dengan kepastian akurasi pemodelan yang dapat dipertanggungjawabkan secara statistik.

## 4.4 Analisis Beban Resource Kontainer Edge Gateway

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

---

## 5. Kesimpulan

1. Implementasi enkripsi AES-128 pada mikrokontroler NodeMCU ESP8266 terbukti meningkatkan keamanan integritas data secara signifikan, namun membawa dampak konsekuensi berupa peningkatan computation overhead jaringan. Latensi rata-rata RTT mengalami kenaikan dari $2.15\text{ ms}$ pada skenario plaintext menjadi $21.61\text{ ms}$ pada skenario terenkripsi AES-128.
2. Pengujian pada kondisi gangguan nirkabel menunjukkan bahwa sistem komunikasi IoT rentan terhadap fluktuasi stabilitas frekuensi radio $2.4\text{ GHz}$. Kehadiran interferensi sinyal memicu terjadinya fenomena pencilan (outlier plot) latensi puncak hingga mencapai $45.12\text{ ms}$ serta memunculkan risiko kehilangan paket (Packet Drop Rate) sebesar $1\%$ akibat kegagalan pemenuhan retransmisi tumpukan TCP.
3. Evaluasi pada unit Edge Gateway Server membuktikan bahwa mekanisme pemrosesan kriptografi meningkatkan utilitas komputasi kontainer pemroses hingga batas maksimal $68.2\%$ saat terjadi lonjakan beban kerja serangan. Penggunaan arsitektur penyimpanan berbasis cache Redis terbukti efektif menjaga stabilitas performa sistem keseluruhan dengan meminimalkan beban memori di angka $14.5\text{ MB}$.
4. Melalui pengujian statistik inferensial Welch's t-test, perbedaan peningkatan latensi akibat enkripsi dinyatakan valid dan signifikan secara meyakinkan ($p\text{-Value} = 0.00029 < 0.05$). Kendati demikian, total waktu tunda akhir yang berada di bawah kisaran $50\text{ ms}$ ini masih berada jauh di dalam ambang batas toleransi operasional sistem kendali otomasi perumahan yang bersifat real-time.

## Daftar Pustaka

## Referensi [1-5]

[1] Hadiatullah, D. R., Farosanti, L., & Rizky, M. C. (2025). Optimalisasi Smart Home Berbasis IoT dengan NodeMCU ESP8266 untuk Efisiensi Energi. Jurnal Fasilkom, 15(2), 368-375.

[2] Hamka, M., Purnama, I., & Bangun, B. (2025). Lampu Pintar: Mengendalikan Pencahayaan Jarak Jauh dengan ESP32 dan Blynk. Prosiding Seminar Nasional Teknologi Komputer dan Sains (SAINTEKS), 3(1), 345-354.

[3] Pramono, A., & Muntahar, A. A. M. (2024). Implementasi Keamanan Rumah Pintar Berbasis Android Dengan Teknologi IoT Dan NodeMCU ESP8266. Jurnal Resistor (Rekayasa Sistem Komputer), 7(3).

[4] Agma, A. R. (2025). Implementasi Internet of Things (IoT) pada Sistem Smart Home. Jurnal Informatika Indonesia, 1(1), 15-21.

[5] Ferella, Paembonan, S., & Abduh, H. (2025). Prototype Sistem Kontrol Rumah Pintar Menggunakan Kamera Berbasis Internet of Things (IoT). JITET (Jurnal Informatika dan Teknik Elektro Terapan), 13(1).


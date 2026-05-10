c# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : "Apakah penggunaan algoritma enkripsi AES-128 pada NodeMCU meningkatkan latensi secara signifikan dibandingkan dengan sistem tanpa enkripsi?"
Hypothesis        : Penerapan enkripsi AES-128 meningkatkan response time (latensi) lebih dari 50ms dibandingkan sistem tanpa enkripsi.
Tipe Eksperimen   : [ * ] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control |  Pengiriman data tanpa keamanan |  No Encryption | Payload 128 bit, Jarak 5m, Wifi RSSI -60dBm |
| Treatment | Pengiriman data dengan enkripsi | AES-128 | Payload 128 bit, Jarak 5m, Wifi RSSI -60dBm |

Fairness Checklist:
  [ *] Dataset (payload data uji) identik untuk semua kondisi
  [ *] Preprocessing (skema parsing data) setara
  [ *] Tuning effort setara (clock speed mikrokontroler dikunci pada 80 MHz)
  [ *] Environment identik (router, jarak, interferensi diuji pada kondisi sama)
  [ *] Metrik evaluasi sama (End-to-End Latency dalam milidetik)

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Fluktuasi delay akibat interferensi Wi-Fi | Menggunakan router khusus LAN terisolasi tanpa beban |
| External    | Hasil hanya berlaku untuk NodeMCU (ESP8266) | Menggunakan library standar yang kompatibel ke ESP32 |
| Construct   | Latensi mencakup waktu respons server cloud | Pengukuran dilakukan di server lokal (Local Broker) |
| Conclusion  | Jumlah sampel terlalu kecil untuk uji statistik | Mengambil 100 kali sampel uji (trial) per kondisi |

Statistical Plan:
  Uji statistik   : Independent Samples t-Test
  Justifikasi      : Membandingkan rata-rata latensi dari 2 kelompok independen (AES vs Off)
  Alpha            : 0.05
  Effect size min  : 0.5 (Medium effect size berdasarkan analisis Cohen's d)

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah penggunaan algoritma enkripsi AES-128 pada NodeMCU meningkatkan latensi secara signifikan dibandingkan tanpa enkripsi?
**Tipe eksperimen:** [ * ] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Sistem transmisi data default tanpa enkripsi (baseline umum IoT). | No Encryption (Plaintext) | NodeMCU ESP8266, ukuran payload 128-bit, jarak router 5 meter tanpa penghalang. |
| Treatment |Sistem transmisi data yang menerapkan komputasi enkripsi sebelum dikirim. | AES-128 Enabled |NodeMCU ESP8266, ukuran payload 128-bit, jarak router 5 meter tanpa penghalang. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ |Menggunakan data sensor sintetis tiruan dengan ukuran payload konstan sebesar 128-bit untuk kedua kondisi. |
| Preprocessing setara | ✅ |Format data sebelum dikirimkan oleh sensor ke mikrokontroler menggunakan tipe JSON string yang sama |
| Tuning effort setara | ✅ |Frekuensi kerja CPU (clock speed) NodeMCU diatur tetap pada 80 MHz pada saat kompilasi kode di kedua skenario.|
| Environment identik | ✅ |Pengujian dilakukan menggunakan router Wi-Fi lokal yang sama dengan jarak perangkat dan kondisi hambatan ruang fisik yang seragam. |
| Metrik evaluasi sama | ✅ | Kedua kondisi diukur menggunakan metrik End-to-End Latency (selisih milidetik waktu kirim dan terima ACK).|

**Ada yang tidak fair?** [ ] Ya / [ * ] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Terjadi fluktuasi bandwidth akibat perangkat lain terhubung ke router yang sama selama pengujian. | Memutus semua perangkat lain dari router (dedicated testbed network) saat eksperimen berjalan. |
| External | Karakteristik transmisi jaringan rumahan yang sesungguhnya memiliki banyak dinding pembatas (real-world attenuation).|Melakukan eksperimen tambahan pada skenario bertingkat (Loss of Sight/penghalang tembok). |
| Construct | Fungsi pengukuran waktu (millis()) di mikrokontroler mengalami overflow atau tidak presisi dalam skala mikrosekon.| Menggunakan modul RTC (Real-Time Clock) eksternal berpresisi tinggi atau fungsi micros() untuk mencatat timestamp.|
| Conclusion |Nilai deviasi standar latensi sangat tinggi sehingga hasil analisis statistik t-test tidak konprensif. |Meningkatkan jumlah pengulangan (trial) dari 30 kali menjadi 100 kali per skenario guna meminimalkan bias fluktuasi acak. |

**Ancaman mana yang paling sulit dimitigasi?** Ancaman Internal (Interferensi Sinyal Jaringan Nirkabel).
**Mengapa?**
> Karena sinyal Wi-Fi 2.4 GHz sangat rentan terhadap gangguan eksternal di luar kontrol peneliti, seperti sinyal Wi-Fi dari rumah tetangga atau radiasi alat elektronik lain, yang dapat secara acak mengubah latensi transmisi data di luar pengaruh algoritma AES-128 itu sendiri.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Bagaimana kondisi pengujian baselinenya? Apakah parameter baseline telah dioptimalkan (tuned) secara adil, atau baseline dibiarkan menggunakan konfigurasi default yang lemah sehingga metode baru tampak jauh lebih baik (straw man comparison)?
2. Apakah lingkungan pengujian benar-benar identik? Apakah metode baru dan baseline diuji pada spesifikasi perangkat keras (CPU, RAM, versi library IoT) dan kondisi jaringan yang benar-benar sama?
3. Seberapa signifikan perbedaannya secara statistik? Apakah klaim "mengalahkan" tersebut didukung oleh uji signifikansi statistik (seperti p-value < 0.05 dan pengukuran effect size) yang valid, ataukah selisih performa tersebut hanya riak margin galat (noise) eksperimen biasa?

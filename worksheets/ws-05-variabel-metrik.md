# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: "Apakah implementasi protokol MQTT dengan enkripsi TLS/SSL pada ESP32 menghasilkan latency dan packet loss yang secara signifikan berbeda dibandingkan dengan protokol HTTP standar pada sistem smart home?"

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|  Protokol Komunikasi  | IV   | Metode pengiriman data aman  |  MQTT+TLS vs HTTP   |  Nominal  |    -  |  Pengaturan perangkat lunak pada mikrokontroler   |    Variabel ini adalah intervensi utama untuk melihat efek keamanan         |
|     Latensi (Response Time)     | DV   | Kecepatan sistem       |  Round Trip Time (RTT)      |  Ratio     |   ms     |     Selisih waktu kirim perintah hingga terima ACK          |     Mewakili kenyamanan pengguna (user experience) dalam mengontrol rumah.        |
|  Kekuatan Sinyal Wi-Fi        | CV   |    Stabilitas medium    | RSSI       |    Interval   |     dBm   |    Dibaca melalui fungsi WiFi.RSSI() pada ESP32           |    Memastikan hasil bukan karena perbedaan jarak router.         |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [ *] Setiap langkah terdokumentasi
  [ *] Tidak ada "lompatan logis"
  [ *] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** "Apakah penggunaan algoritma enkripsi AES-128 pada NodeMCU meningkatkan latensi secara signifikan dibandingkan tanpa enkripsi?"

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Keamanan Data | IV | Proteksi pesan | Status Enkripsi (On/Off) | Nominal| —|
| VariabelTipeKonsep AbstrakMetrik KonkretSkala (NOIR)SatuanKeamanan DataIVProteksi pesanStatus Enkripsi (On/Off)Nominal—Kecepatan Sistem| DV | Waktu proses| End-to-End Latency| Ratio| Milidetik (ms)|
| Beban Komputasi| CV |Konsumsi Resource | RAM Usage|Ratio | KB|

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [ *] Tidak
> Jika ya, di mana? (Rantai sudah selaras dari konsep keamanan ke metrik waktu).
---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Waktu respon adalah representasi paling akurat untuk konsep "kecepatan" dalam IoT.|
| Sensitive | 4 | Sangat peka terhadap perubahan kecil dalam ukuran paket atau overhead enkripsi.|
| Feasible | 5 |Sangat mudah diukur menggunakan fungsi timestamping (millis()) pada mikrokontroler. |

**Apakah perlu secondary metric?** [ * ] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Jitter (variasi latensi), untuk melihat konsistensi performa sistem dari waktu ke waktu.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika pengujian dilakukan pada jaringan lokal yang sangat kosong dan cepat, perbedaan enkripsi mungkin tidak terlihat karena performa jaringan mencapai batas maksimum (ceiling), sehingga semua hasil terlihat "sangat cepat" meskipun ada beban tambahan.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point (log transaksi) dapat terkumpul tanpa ada yang terlewat? | Data mungkin hilang jika koneksi Wi-Fi terputus di tengah jalan saat pengiriman ke cloud.| Menggunakan logging lokal di SD Card pada NodeMCU/ESP32 sebagai cadangan data jika kiriman gagal.|
| Consistency | Apakah terdapat kontradiksi internal atau perbedaan standar waktu antara perangkat? | Alat ukur (timer) mungkin berbeda antara server dan client karena perbedaan clock speed.| Melakukan sinkronisasi waktu menggunakan protokol NTP (Network Time Protocol) secara berkala.|
| Validity | Apakah metrik yang diukur benar-benar mencerminkan variabel yang diteliti? | Latensi yang diukur bisa tercampur dengan delay eksternal dari aplikasi Blynk atau server Cloud.| Melakukan pengujian awal di jaringan lokal (LAN) untuk isolasi variabel overhead enkripsi.|
| Representativeness | Apakah sampel data yang diambil sudah mewakili berbagai kondisi populasi/lingkungan?| Sampel data awal hanya diambil dari satu skenario (satu model rumah/satu ruangan).| Melakukan pengujian pada 3 skenario jarak yang berbeda dari router (1m, 5m, dan 10m) serta kondisi penghalang (tembok).|

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap p-hacking karena peneliti secara sengaja mencari metrik yang hanya memberikan hasil signifikan (p < 0.05) untuk mendukung hipotesisnya, sementara mengabaikan metrik lain yang gagal. Ini adalah bentuk bias yang menyesatkan.

> Perbedaannya dengan eksplorasi data yang sah:
Eksplorasi Data: Dilakukan untuk mencari pola baru tanpa membuat klaim pembuktian akhir. Hasilnya digunakan untuk membangun hipotesis baru di riset mendatang.
P-hacking: Dilakukan untuk memanipulasi kesimpulan riset yang sedang berjalan agar terlihat sukses, padahal hasil tersebut bisa jadi hanya kebetulan belaka.
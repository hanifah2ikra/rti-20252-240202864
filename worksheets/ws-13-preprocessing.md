# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : IoT Smart Home Wireless Telemetry Log (`telemetry_log.csv`)
Jumlah data awal  : 200 baris data paket (100 Baseline Plaintext, 100 Intervensi AES-128)

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 2 Paket | Listwise Deletion (Dikeluarkan) | Paket loss alami akibat Wi-Fi congestion pada iterasi AES-128 ke-44 & ke-45. Nilai RTT tidak terbentuk (timeout) |
| Duplikat| 0 Kasus | Tidak ada tindakan | Setiap paket memiliki identitas unik berupa serial timestamps mikrodetik (`Time_Sent`) |
| Error   | 1 Kasus | Konversi Overflow biner matematis | Nilai `Time_ACK` < `Time_Sent` pada run ke-88 akibat hardware timer rollover (32-bit overflow). Dikompensasi via script parser |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Skala Waktu | `Time_Sent` & `Time_ACK` | Mengubah satuan dari mikrodetik ke milidetik dengan membagi nilai selisih sebesar 1000 | Statistik deskriptif dan uji hipotesis *t-test* standar industri IoT menggunakan satuan milidetik untuk kemudahan interpretasi |

Normalization:
  Metode    : Tidak Melakukan Normalisasi (Raw Feature Kept)
  Alasan    : Nilai asli RTT dalam milidetik merepresentasikan metrik fisik riil yang langsung diujikan ke t-test. Normalisasi ke [0,1] justru akan menghilangkan arti fisis dari overhead waktu nyata enkripsi
  Parameter : (dihitung dari: Tidak menggunakan normalisasi)

Leakage Check:
  [x] Parameter normalisasi dari training set saja
  [x] Tidak ada informasi test set dalam preprocessing
  [x] Cross-validation dilakukan setelah split

Jumlah data akhir : 198 baris data paket valid (100 Plaintext, 98 AES-128)
Script tersedia   : [x] Ya → path: `/scripts/telemetry_cleaner.py` | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing RTT value (Timeout) | 2 dari 200 paket (1.0%) | Listwise deletion | < 5% dari total populasi paket, terjadi acak karena interferensi frekuensi radio Wi-Fi |
| Hardware Timer Overflow | 1 dari 200 paket (0.5%) | Rekonstruksi biner (Delta T = ((4294967295 - T sent) + T ack)/1000) | Data bernilai valid, kesalahan hanya pada batasan tampung tipe data unsigned long pada chip mikro |
| | | | |
| | | | |

**Jumlah data sebelum cleaning:** 200 paket
**Jumlah data setelah cleaning:** 198 paket
**Persentase data yang hilang/berubah:** 1,0% data hilang, 0,5% data ditransformasikan

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| RTT (ms) | 14.81 – 45.12 ms | Right-skewed (Kepadatan tinggi di 15-18 ms) | Ya (1 data bernilai 45.12 ms) | Tidak Perlu Normalisasi | Nilai RTT mencerminkan satuan waktu fisik (milidetik). Mengubah skala data akan merusak interpretasi nilai overhead kriptografi riil yang dicari dalam uji t-test. || *Contoh: accuracy_score* | *0.72 – 0.95* | *Normal, narrow* | *Tidak* | *Tidak perlu* | *Sudah dalam [0,1], metode berbasis distance tidak digunakan* || | | | | | |
| | | | | | |

**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
> Normalisasi (seperti Min-Max atau Z-score) umumnya mutlak diperlukan pada algoritma berbasis jarak seperti K-Means atau Neural Networks agar fitur ber-skala besar tidak mendominasi fitur kecil. Namun, untuk penelitian ini, metode analisis yang digunakan adalah uji beda rerata kuantitatif Independent Samples t-Test pada variabel tunggal. Mempertahankan nilai asli RTT dalam milidetik sangat krusial agar pembaca riset mengetahui secara langsung delay fisik yang dirasakan oleh perangkat smart home.

**Leakage check:**
- [x] Parameter dihitung dari training set saja (N/A)
- [x] Normalisasi diterapkan setelah train-test split (N/A)

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: IoT Smart Home Wireless Telemetry Log (`telemetry_log.csv`)
2. Data awal: 200 records, 5 features (Run_ID, Group_ID, Time_Sent, Time_ACK, RTT)
3. Cleaning:
   - Missing values: 2 kasus packet drop, metode: Listwise deletion (dikeluarkan dari sampel kelompok AES)
   - Duplikat: 0 kasus, tindakan: ____
   - Error: 1 kasus hardware timer overflow, tindakan: Rekonstruksi rumus inversi mikrodetik biner 32-bit
4. Transformation: Konversi timestamps mikrodetik (μs) ke bentuk durasi Round Trip Time milidetik (ms)
5. Normalisasi:Tidak diterapkan (mempertahankan interpretasi fisis metrik waktu riil) (metode), parameter dari ____
6. Data akhir: 198 records, 5 features
7. Leakage check: [x] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, pada pengerjaan analisis data tingkat awal sebelumnya, saya sering menerapkan fungsi pencorakan data MinMaxScaler() atau StandardScaler() secara otomatis karena "biasa dilakukan" di tutorial pemrograman Python, tanpa menganalisis secara mendalam model statistik apa yang akan digunakan di akhir pengerjaan.
> Risiko dari tindakan over-preprocessing (memproses data secara berlebihan) adalah terjadinya distorsi fisis data asli (minimal distortion violation). Pada riset sistem tertanam (IoT) ini, jika nilai RTT dinormalisasi menjadi skala 0 hingga 1, maka esensi dan kejelasan angka penalti waktu riil (misal, selisih beban $3.18\text{ ms}$) akan terkubur di balik angka desimal abstrak. Hal tersebut justru mempersulit pembaca riset dalam menilai apakah sistem smart home yang terenkripsi tersebut masih memenuhi batas toleransi fungsional real-time siber atau tidak.

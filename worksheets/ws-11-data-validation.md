# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [X] Semua skenario tercakup
  [X] Jumlah run sesuai rencana
  [X] Tidak ada file output hilang
  Missing:2 dari 200 data points

Format Consistency:
  [X] Semua file format sama (CSV/JSON/...)
  [X] Header konsisten
  [X] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [X] Nilai dalam range masuk akal
  [X] Tidak ada waktu negatif
  [X] Metrik 0–100%, tidak di luar range
  Anomali ditemukan:2 data point mengalami packet loss (timeout) pada skenario AES-128.

Cross-Validation:
  [X] Run identik → hasil mendekati (Variansi mikrodetik akibat jitter nirkabel)
  [X] Trend konsisten dengan ekspektasi teori (AES-128 memiliki RTT rata-rata lebih tinggi)

Keputusan:
  [X] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Baseline (Plaintext) | 100 | 100 | 0 | — |
| Intervensi (AES-128) | 100 | 98 | 2 | Perangkat NodeMCU mengalami interferensi saluran frekuensi radio (Wi-Fi congestion) pada iterasi ke-44 dan ke-45, menyebabkan broker MQTT menjatuhkan paket (packet drop/timeout). |
| | | | | |
| | | | | |

**Total expected:** 200 | **Total actual:** 198 | **Missing:** 2

**Keputusan untuk data missing:**
> Dua data point yang hilang tidak akan dilakukan imputasi nilai (tidak diisi nilai rata-rata buatan) maupun di-re-run paksa, melainkan dikeluarkan dari perhitungan rata-rata t-test (N=98 untuk kelompok intervensi). Kondisi packet drop ini akan didokumentasikan secara formal pada bab pembahasan sebagai bukti empiris efek nyata dari fluktuasi stabilitas jaringan Wi-Fi lokal 2.4 GHz.
---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score. Pada sampel distribusi metrik Round Trip Time (RTT) milidetik (ms).

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | 18.21 |
| 2 | 18.54 |
| 3 | 18.42 |
| 4 | 45.12 |
| 5 | 18.38 |

**Deteksi outlier:**
- Q1 = 18.30 ms | Q3 = 18.48 ms | IQR = Q3 - Q1 = 0.18 ms
- Batas bawah (Q1 - 1.5×IQR) = 18.30 - 0.27 = 18.03 ms
- Batas atas (Q3 + 1.5×IQR) = 8.48 + 0.27 = 18.75 ms
- Outlier terdeteksi: Run 4 (45.12 ms) karena nilai > 18.75 ms

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| *Run 4* | 45.12 ms | Terjadi antrean jabat tangan nirkabel (MAC layer retransmission delay) akibat interupsi internal sub-rutin Wi-Fi background task dari chip ESP8266 saat memproses buffer data.| Tetap Dipertahankan. Nilai ini tidak dihapus karena merepresentasikan contextual anomaly yang valid dari perilaku sistem tertanam nirkabel riil dan akan memperkaya visualisasi batas galat (error bar). |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 99.0% data terkumpul (198 dari 200 data points)
**2. Format:** [X] Konsisten / [ ] Ada inkonsistensi: ____
**3. Range check (anomali):**1 data point terdeteksi sebagai statistical outlier (45.12 ms) akibat penalti jaringan nirkabel alami, namun nilainya masih berada dalam batas logis kerja mikrokontroler ( <1000 ms )
**4. Logic check:** [X] Parameter sesuai plan / [ ] Ada ketidaksesuaian: ____

**Kesimpulan:** [X] Data siap analisis (Pipa validasi data terpenuhi, dataset siap dimasukkan ke dalam pengerjaan pengujian statistik Independent Samples t-Test). / [ ] Perlu tindakan: ____

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar vs Data yang dipercaya:
"Data yang benar" hanyalah data yang direkam secara mentah oleh skrip otomatis karena tidak mengalami eror sintaksis program saat disimpan. Namun, data tersebut belum tentu bisa dipercaya. "Data yang dipercaya" (trusted data) adalah data yang telah melalui proses pembuktian integritas logis, di mana strukturnya lengkap sesuai rencana, parameter eksperimennya terisolasi secara adil (fair), formatnya seragam, dan anomali di dalamnya telah diinvestigasi secara ilmiah, bukan sekadar diasumsikan tanpa bukti.

> Urgensi validasi formal pada logging otomatis:
Validasi formal mutlak diperlukan karena logger otomatis sekalipun tetap rentan terhadap bias sistemis (systemic bugs). Sebagai contoh, jika fungsi pewaktu mikrokontroler NodeMCU mengalami overflow biner, atau jika ada fluktuasi arus listrik yang memperlambat jam internal chip, modul otomatis akan terus memproduksi angka koordinat waktu yang salah tanpa memunculkan pesan eror (silent error). Tanpa adanya pemeriksaan pilar kualitas data (accuracy, consistency, completeness, validity) secara berkala, peneliti dapat terjebak melakukan analisis statistik di atas dataset cacat yang menghasilkan kesimpulan riset yang keliru.
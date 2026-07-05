# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   | Baseline (Plaintext) | 15.24 ms | 0.42 ms | 15.20 ms | 14.81 ms | 16.12 ms | 100 |
   | Intervensi (AES-128) | 18.42 ms | 1.15 ms | 18.25 ms | 17.92 ms | 45.12 ms | 98 |

2. Uji Hipotesis:
   Uji yang digunakan  : Independent Samples t-Test
   Justifikasi          : Membandingkan nilai rata-rata dari dua kelompok sampel yang saling bebas (Plaintext vs AES-128) dengan ukuran sampel besar (N > 30) yang memenuhi teorema limit pusat
   Hasil: p <0.001, effect size (d/r/η²) : (Cohen's d) = 3.65
   CI 95%               : [2.94 ms, 3.42 ms]

3. Keputusan:
   [x] H₀ ditolak → H₁ diterima (Penerapan AES-128 terbukti secara statistik meningkatkan RTT)
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : Penerapan enkripsi AES-128 meningkatkan RTT secara signifikan sebesar 3.18 ms dibandingkan Plaintext
   Practical significance: Secara praktis, penambahan tunda sebesar 3.18 ms sangat tidak berarti bagi pengguna manusia (jauh di bawah ambang batas real-time 10 detik), sehingga sistem tetap responsif dan aman dijalankan
   Perbandingan literatur: Sejalan dengan Pramono & Muntahar (2024), beban enkripsi simetris pada chip 80 MHz sangat minimal dan layak diterapkan di smart home

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   |External validity | Pengujian terisolasi di jaringan lokal (LAN) | Belum mencerminkan tunda akibat internet publik (cloud delay) | Dibatasi cakupannya hanya pada ranah transmisi nirkabel lokal |
   | Statistical | Adanya 2 packet drop (timeout) | Mengurangi ukuran sampel kelompok intervensi menjadi n=98 | Menggunakan uji t-test variansi tidak sama (Welch's t-test) |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : N/A (H₀ ditolak)
   Boundary condition   : N/A 
   Insight              : N/A 
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 grup (Baseline/Plaintext vs Intervensi/AES-128) |
| Apakah data berpasangan (paired)? | Tidak, data bersifat independen antara paket teks biasa dan paket terenkripsi |
| Apakah distribusi normal? (uji normalitas) | Ya, berdasarkan Teorema Limit Pusat, jumlah sampel besar (N≥30, di mana NA=100 dan NB=98) membuat distribusi nilai rata-rata sampel mendekati normal |
| **Uji yang dipilih:** | Independent Samples t-Test (menggunakan variansi terpisah/Welch's t-test) |
| **Justifikasi:** | Digunakan karena membandingkan dua kelompok data kontinu yang tidak berpasangan dan memiliki jumlah sampel yang sedikit berbeda akibat hilangnya 2 titik data (missing data) pada kelompok intervensi |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 15.24 ± 0.42 ms | 100 |
| B | 18.42 ± 1.15 ms | 98 |

p < 0.001, Cohen's d = 3.65, CI 95% = [2.94 ms, 3.42 ms]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p < 0.001 → signifikan secara sangat kuat pada α=0.05 |
| Effect size | d=3.65 → efek intervensi masuk kategori ekstrem/sangat besar (>0.8). Ini membuktikan bahwa penambahan fungsi enkripsi memberikan dampak pembeda yang nyata dan masif terhadap karakteristik waktu kerja CPU. |
| Practical significance | Meskipun secara statistik sangat signifikan, peningkatan tunda riil hanya sebesar 3.18 ms. Secara praktis, penalti ini tidak akan disadari oleh penghuni rumah saat menekan sakelar lampu nirkabel, sehingga peningkatan keamanan ini sangat efisien |
| Hubungan ke RQ | Menjawab RQ secara langsung: Penerapan AES-128 terbukti meningkatkan durasi waktu RTT paket data, namun nilai total tunda (18.42 ms) tetap berada jauh di bawah ambang batas responsivitas waktu nyata |
| Perbandingan literatur | Mengonfirmasi temuan Hamka dkk. (2025) bahwa fungsionalitas NodeMCU tidak terganggu oleh pengamanan siber, sekaligus mematahkan ketakutan subjektif pengembang IoT yang sering menghindari enkripsi karena takut memicu latensi besar |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?
Latih kemampuan failure analysis untuk skenario Contextual Anomaly (Run ke-4 pada kelompok AES-128 bernilai ekstrem:45.12 ms)
**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan kegagalan eksperimen. Lonjakan ini adalah contoh anomali kontekstual nirkabel yang valid. Sistem tidak mengalami crash, melainkan mengalami tunda transmisi pada lapisan fisik |
| Kemungkinan penyebab? | Terjadi antrean jabat tangan radio Wi-Fi (MAC layer retransmission) akibat interferensi sesaat dari perangkat lain pada kanal frekuensi radio 2.4 GHz yang sama di sekitar laboratorium |
| Boundary condition? | Overhead komputasi matematika AES-128 tetap stabil di kisaran 3 ms, namun performa total RTT menjadi rentan melonjak ketika stabilitas medium transmisi nirkabel lokal mengalami gangguan/kongesti |
| Insight yang bisa diambil? | Latensi total sistem IoT tidak hanya dipengaruhi oleh kompleksitas algoritma pada firmware, melainkan digerakkan oleh kombinasi antara beban CPU dan fluktuasi kualitas sinyal nirkabel (jitter) |
| Apakah layak dilaporkan? Mengapa? | Sangat layak dilaporkan. Mencantumkan data ekstrem ini beserta penyebabnya membuktikan kejujuran akademis riset (data integrity) dan memberikan gambaran performa sistem yang jujur di lingkungan operasional nyata |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical limitation | 2 paket drop mengalami timeout total akibat gangguan sinyal parah | Mengurangi kekuatan uji statistik (power test) karena sampel tidak lagi seimbang ($100$ vs $98$), namun pengaruhnya dapat diredam dengan penyesuaian derajat kebebasan pada rumus Welch's t-test |
| | | |
| | | |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Refleksi Hasil Negatif dan Anomali sebagai Kontribusi: Menemukan hasil negatif, anomali, atau hipotesis yang tidak didukung dalam riset ilmiah bukanlah sebuah kegagalan total, melainkan bentuk kontribusi pengetahuan yang sangat berharga. Melalui proses Failure Analysis yang mendalam terhadap data outlier (seperti kasus lonjakan latensi 45.12 ms atau packet drop akibat interferensi Wi-Fi), kita dapat memetakan boundary condition (batas kemampuan operasional) dari mikrokontroler NodeMCU ESP8266 secara objektif.Proses ini mengubah cara pandang saya secara mendasar: riset yang jujur tidak harus selalu menampilkan kurva performa yang sempurna dan mulus. Mendokumentasikan dan menganalisis mengapa suatu kegagalan atau lonjakan tunda terjadi justru menyelamatkan komunitas peneliti lain dari duplikasi kesalahan yang sama, serta memberikan landasan yang kokoh untuk perancangan arsitektur mitigasi sistem siber IoT yang lebih tangguh di masa depan.


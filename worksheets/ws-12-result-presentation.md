# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Apakah penerapan enkripsi AES-128 pada   firmware NodeMCU ESP8266 meningkatkan durasi waktu Round Trip Time (RTT) paket data secara signifikan dibandingkan dengan pengiriman data tanpa enkripsi (plaintext)?
Metrik Utama      : Round Trip Time (RTT) dalam satuan milidetik (ms)

Tabel Hasil:
| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
| Baseline (Plaintext) | 15.24 ± 0.42 ms | 100% (100/100) | 100 |
| Intervensi (AES-128) | 18.42 ± 1.15 ms | 98% (98/100) | 98 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar Chart + Error Bar | Memperlihatkan biaya performa (overhead) rata-rata akibat proses enkripsi matematika AES-128 dibanding Plaintext. | RTT (Mean ± Std) |
| 2 | Box Plot / Violin Plot | Menampilkan sebaran data, kepadatan distorsi jitter, dan visualisasi outlier ekstrem akibat interferensi nirkabel nyata | Distribusi RTT seluruh run |

Bias Check:
  [X] Y-axis mulai dari 0 (atau dijustifikasi)
  [X] Error bar/CI ditampilkan
  [X] Semua data disertakan (tidak cherry-picked)
  [X] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Metrik 1 Round Trip Time / RTT (mean ± std) | Metrik 2 Packet Loss Rate (%) (mean ± std) | n |
|----------|----------------------|----------------------|---|
| Baseline (Plaintext) | 15.24 ± 0.42ms | 0%(0/100) | 100 |
| Intervensi (AES-128) | 18.42 ± 1.15ms | 2%(2/100) | 98 |
| | | | |

**Checklist tabel:**
- [X] Self-contained (judul jelas, satuan ada, N tercantum)
- [X] Mean ± std (bukan single number)
- [X] Diurutkan berdasarkan metrik utama
- [X] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar chart + error bar | Menunjukkan peningkatan rata-rata delay yang konvergen dan stabil, membuktikan hipotesis bahwa overhead enkripsi ringan bagi CPU 80MHz (<5ms) | Nilai Mean RTT dan Standard Deviation dari kedua kelompok. |
| 2 | Box plot | Menunjukkan variabilitas data nirkabel asli, rentang interkuartil, serta memperlihatkan posisi pencanduan titik data ekstrem (contextual anomaly) 45.12 ms pada pengujian AES-128. | Seluruh sebaran baris data RTT (100 data Baseline, 98 data Intervensi). |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A (Plaintext) = 15.24 ms, Metode B = (AES-128) = 18.42 ms. Bar chart dengan Y-axis mulai dari 14 ms hingga 19 ms.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya. Pemotongan sumbu Y dari 14 ms akan secara visual mendistorsi grafik, membuat balok AES-128 (18.42 ms) terlihat seolah-olah 3 hingga 4 kali lipat lebih lambat dan berat daripada Plaintext, padahal selisih riilnya hanya 3.18 ms. |
| Apakah error bar ditampilkan? | Tidak, pada visualisasi yang bias, error bar sering sengaja dihilangkan untuk menyembunyikan fakta bahwa variansi kedua data sebenarnya saling beririsan (overlapping). |
| Apakah semua kondisi ditampilkan? | Ya, namun distorsinya terletak pada aspek skala sumbu vertikal (truncated axis). |
| Apa solusinya? | Sumbu Y wajib dipetakan secara jujur mulai dari angka 0 ms. Dengan demikian, pembaca dapat melihat secara proporsional bahwa penambahan enkripsi AES-128 sebenarnya sangat aman dan tidak merusak batas responsivitas waktu nyata (real-time).|

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [X] Semua bias check lulus
- [X] Ada yang perlu diperbaiki: Tidak ada, sumbu Y dipastikan dimulai dari 0 ms dan error bar standard deviasi wajib dilekatkan pada puncak setiap balok diagram.

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Urgensi kombinasi Tabel dan Grafik:
Tabel dan grafik tidak bisa dipisahkan karena melayani fungsi kognitif yang berbeda dalam laporan ilmiah. Tabel menyediakan aspek presisi numerik yang absolut, memungkinan peneliti lain menyalin angka rata-rata desimal secara tepat untuk keperluan komparasi di masa depan. Di sisi lain, grafik memberikan kecepatan penangkapan pola makro. Melalui grafik, pembaca secara instan dapat memahami struktur distribusi data, melihat ketimpangan deviasi standar, dan mendeteksi anomali tanpa harus membaca baris angka satu per satu.
> Pengalaman visualisasi menyesatkan:
Dalam pengerjaan tugas infografis dahulu, saya pernah secara tidak sengaja membuat grafik batang dengan sumbu Y yang tidak dimulai dari angka nol agar perbedaan performa antar-sistem terlihat mencolok di presentasi. Saya menyadari bahwa tindakan tersebut keliru dalam ranah riset siber akademis, karena mengubah visualisasi data demi mengejar efek dramatis melanggar prinsip kejujuran data (data integrity) dan menghasilkan kesimpulan bias yang dapat menyesatkan penilai atau pembaca.

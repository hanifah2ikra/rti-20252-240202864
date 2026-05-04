# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Mayoritas sistem smart home berbasis NodeMCU/ESP32 saat ini memiliki kerentanan pada keamanan data (lack of encryption) dan penurunan reliabilitas (latensi tinggi) saat koneksi internet tidak stabil.

Research Question:
  Tipe         : [ * ] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : "Apakah implementasi protokol MQTT dengan enkripsi TLS/SSL pada ESP32 menghasilkan latency dan packet loss yang secara signifikan berbeda dibandingkan dengan protokol HTTP standar pada sistem smart home?"
  Variabel IV  : Jenis Protokol Komunikasi (MQTT + TLS vs. HTTP standar).
  Variabel DV  : Network Performance (Latency & Packet Loss).
  Metrik       : Milidetik (ms) untuk latensi dan persentase (%) untuk packet loss.
  Dataset      : Pengujian pada jaringan Wi-Fi lokal dengan simulasi beban bandwidth.
  Baseline     : Sistem IoT berbasis HTTP tanpa enkripsi (seperti pada model umum Hamka dkk., 2025).
Quality Check RQ:
  [ * ] Variabel spesifik
  [ * ] Metrik jelas
  [ * ] Baseline ada
  [ * ] Konteks disebutkan
  [ * ] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Karakteristik performa keamanan data pada mikrokontroler daya rendah (ESP32) saat menggunakan enkripsi berlapis.
  Jenis kontribusi        : [ ] Improvement  [ * ] Comparison  [ ] Novel approach
  Gap yang diisi          : Mengisi celah keamanan (method gap) dan reliabilitas performa (performance gap) yang diidentifikasi di WS-03.

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan pada rata-rata latensi antara penggunaan protokol MQTT+TLS dan HTTP standar pada ESP32.
  H₁ : Penggunaan MQTT+TLS memberikan latensi yang lebih tinggi secara signifikan dibandingkan HTTP standar, namun tetap berada di bawah ambang batas toleransi real-time.
  Threshold              : p-value < 0.05 (Signifikansi statistik) dan Latensi < 200ms (Batas nyaman user).
  Justifikasi threshold  : Latensi di atas 200ms dianggap tidak lagi real-time untuk kontrol perangkat rumah (ITU-T G.114).
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Kurangnya aspek keamanan enkripsi pada kontrol jarak jauh IoT dan ketergantungan pada stabilitas internet.

**RQ versi pertama (tulis bebas):**
> Bagaimana pengaruh keamanan enkripsi terhadap kecepatan respon lampu pintar?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Belum ada (perlu sebutkan jenis enkripsi/protokol).| |
| Metrik terukur | Sudah ada (kecepatan respon). | |
| Baseline | Belum ada. | |
| Dataset/konteks | | |

**Tipe RQ:** [ ]*  Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> "Apakah penggunaan algoritma enkripsi AES-128 pada komunikasi NodeMCU-Blynk meningkatkan latensi secara signifikan dibandingkan dengan sistem tanpa enkripsi?"
---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan pada response time (ms) antara sistem kontrol dengan AES-128 dan tanpa enkripsi. |
| H₁ | Penerapan enkripsi AES-128 meningkatkan response time lebih dari 50ms dibandingkan tanpa enkripsi. |
| Metrik | Response Time (Milidetik). |
| Threshold | 50ms (Alpha 0.05). |
| Justifikasi threshold | Tambahan waktu 50ms adalah batas maksimal overhead komputasi agar user tidak merasakan jeda (perceived lag). |

**Apakah hipotesis ini falsifiable?** [ *] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Melakukan eksperimen sebanyak 100 kali percobaan; jika rata-rata selisih waktu ternyata kurang dari 50ms, maka H₁ ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah AES-128 meningkatkan latensi secara signifikan pada NodeMCU? |
| Variable (IV) | Penggunaan Algoritma Enkripsi (Off vs AES-128). |
| Variable (DV) | Latensi transmisi data. |
| Metric | Rata-rata waktu (ms) dari tekan tombol hingga lampu menyala. |
| Data source | Log dari serial monitor Arduino IDE dan Timestamp aplikasi Blynk. |
| Analysis method | Independent T-Test (untuk membandingkan dua rata-rata kelompok data). |

**Apakah rantai lengkap?** [* ] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Implementasi Keamanan Rumah Pintar Berbasis Android Dengan Teknologi IoT Dan NodeMCU ESP8266 (Pramono & Muntahar, 2024)
**RQ yang diekstrak:** Bagaimana merancang sistem keamanan rumah dengan akurasi deteksi tinggi menggunakan metode Extreme Programming?
**Komponen yang hilang:** Baseline dan Metrik Perbandingan. Paper tersebut lebih bersifat Engineering (membangun sistem) daripada Research karena tidak membandingkan efektivitas metodenya dengan metode atau sistem lain secara eksperimental (Comparison).

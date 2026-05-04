# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Internet of Things (IoT) Smart Home 
  Konteks  : Sistem rumah pintar berbasis IoT untuk meningkatkan efisiensi energi dan keamanan rumah
System Context
  Input       : Data dari sensor (gerak, suhu), perintah dari aplikasi mobile
  Process     : Pengolahan data oleh microcontroller (ESP32) dan pengiriman melalui jaringan internet
  Output      : Kontrol perangkat (lampu, pintu, kipas) dan notifikasi real-time
  Outcome     : Peningkatan kenyamanan, efisiensi energi (12–15%), dan keamanan rumah
  Constraints : Koneksi internet tidak stabil, risiko keamanan data, biaya implementasi tinggi
  Stakeholders: Pengguna rumah, pengembang sistem IoT, penyedia layanan internet

Fenomena → Problem
  Fenomena yang diamati             : Sistem smart home berbasis IoT mampu meningkatkan efisiensi energi dan keamanan rumah
  Gejala (symptom) yang terukur     : Penurunan konsumsi listrik sebesar 12–15%. Respon sistem melambat saat koneksi internet tidak stabil
  Masalah yang didiagnosis          : Ketergantungan sistem terhadap koneksi internet menyebabkan performa dan keandalan sistem tidak stabil
  Masalah riset (researchable)      : Belum ada pendekatan optimal untuk meningkatkan keandalan sistem smart home IoT agar tetap responsif dan stabil pada kondisi jaringan internet yang tidak stabil
  Variabel yang terukur             : Waktu respon sistem (detik), Stabilitas koneksi (%), Tingkat keberhasilan pengiriman notifikasi (%), Konsumsi energi (%)

Problem Quality Check
  [*] Clarity — jelas membahas keandalan sistem IoT
  [*] Measurability — ada metrik (respon, energi, notifikasi)
  [*] Relevance — penting dalam pengembangan IoT smart home
  [*] Testability — bisa diuji dengan eksperimen jaringan
  [*] Impact — berdampak pada penggunaan luas teknologi

Problem Statement (1 paragraf):
  Sistem smart home berbasis Internet of Things (IoT) telah terbukti mampu meningkatkan efisiensi energi dan keamanan rumah melalui otomatisasi dan kontrol jarak jauh, dengan penghematan energi mencapai 12–15%. Namun, kinerja sistem masih sangat bergantung pada kestabilan koneksi internet, sehingga menyebabkan keterlambatan respon dan notifikasi ketika jaringan tidak stabil. Hal ini menunjukkan adanya keterbatasan dalam keandalan sistem yang dapat menghambat adopsi secara luas. Oleh karena itu, diperlukan penelitian untuk mengidentifikasi dan menguji pendekatan yang dapat meningkatkan stabilitas dan responsivitas sistem smart home IoT dalam kondisi jaringan yang tidak optimal dengan menggunakan metrik seperti waktu respon, keberhasilan notifikasi, dan efisiensi energi
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Smart Home Berbasis IoT 

| Tahap | Hasil |
|-------|-------|
| Reality | Sistem smart home digunakan untuk otomatisasi rumah |
| Observed Issue (Symptom) | Sistem lambat saat internet tidak stabil|
| Diagnosed Problem (Root Cause) | Ketergantungan tinggi pada jaringan internet|
| Researchable Problem | Belum ada solusi untuk menjaga performa sistem saat jaringan tidak stabil |
| Measurable Variable | Waktu respon, stabilitas sistem, notifikasi |

**Apakah terjebak solution-first thinking?** [ ] Ya / [ * ] Tidak
> Jika ya, kembali ke tahap mana? Tidak ada 

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data sensor & perintah user|
| Process | Pengolahan oleh microcontroller & jaringan |
| Output | Kontrol perangkat & notifikasi|
| Outcome | Efisiensi energi & keamanan |
| Constraints | Internet, keamanan data, biaya|
| Stakeholders | User, developer, provider|

**Komponen mana yang paling relevan dengan masalah riset?** Process & Constraints (karena masalah ada di jaringan/internet)

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 4 | Sudah jelas, bisa diperjelas pada skenario jaringan |
| Measurability | 5 | Ada metrik kuantitatif |
| Relevance | 5 | Sangat penting di IoT |
| Testability | 5 | Bisa diuji eksperimen|
| Impact | 4 | Berdampak besar pada adopsi teknologi|

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Ketergantungan sistem smart home berbasis IoT terhadap koneksi internet yang tidak stabil menyebabkan penurunan kinerja berupa keterlambatan respon dan notifikasi, sehingga diperlukan penelitian untuk mengembangkan dan menguji pendekatan yang mampu meningkatkan keandalan sistem dalam kondisi jaringan terbatas menggunakan metrik waktu respon, stabilitas sistem, dan efisiensi energi.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Engineering (coding):
Fokus pada memperbaiki error
Contoh: “lampu tidak menyala → perbaiki program”
Research:
Fokus pada mencari penyebab mendasar
Contoh: “Mengapa sistem gagal saat jaringan tidak stabil?”. “Bagaimana meningkatkan keandalan sistem?”
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
  Konteks  : Sistem lampu otomatis rumah menggunakan sensor RIP DAN LDR berbasis mikrokontroler 
System Context
  Input       : Sensor RIP untuk deteksi gerakan dan sensor LDR untuk deteksi intensitas cahaya 
  Process     : Mikrokontroler membaca data sensor dan menentukan kondisi lampu ON/OFF 
  Output      : Lampu otomatis menyala atau mati
  Outcome     : Penghematan energi listrik dan kemudahan pengguna 
  Constraints : Akurasi sensor, delay respon sistem, kondisi lingkungan cahaya
  Stakeholders: Pengguna rumah, teknisi IoT, dan peneliti

Fenomena → Problem
  Fenomena yang diamati             : Lampu rumah sering menyala terus meskipun tidak ada aktivitas
  Gejala (symptom) yang terukur     : Konsumsi listrik meningkat dan lampu aktif lebih dari 12 jam per hari
  Masalah yang didiagnosis          : Sistem lampu masih manual dan sensor belum bekerja secara optimal 
  Masalah riset (researchable)      : Belum diketahui tingkat akurasi dan waktu respon kombinasi sensor PIR dan LDR pada sistem smart home lampu otomatis
  Variabel yang terukur             : Akurasi deteksi sensor, waktu respon sistem, konsumsi energi listrik

Problem Quality Check
  [*] Clarity — Apakah satu orang membaca akan paham?
  [*] Measurability — Apakah ada metrik kuantitatif?
  [*] Relevance — Apakah penting untuk domain?
  [*] Testability — Apakah bisa gagal?
  [*] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Penggunaan lampu rumah yang manual menyebabkan pemborosan listrik karena lampu sering dibiarkan menyala meskipun tidak ada aktivitas. Sistem smart home berbasis IoT ini dapat digunakan untuk otomatisasi lampu, namun kinerja sistem dalam mendeteksi gerakan dan kondisi cahaya belum diketahui pasti. Oleh karena itu dilakukan penelitian yang bertujuan menganalisis tingkat akurasi dan waktu respon kombinassi sensor RIP dan LDR pada sistem smart home lampu otomatis berdasarkan parametr akurasi deteksi, waktu respon, dan konsumsi energi listrik untuk meningkatkan efisiensi penggunaan energi pada rumah pintar. 
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Smart Home Lampu Otomatis Berbasis IoT 

| Tahap | Hasil |
|-------|-------|
| Reality | Lampu rumah sering lupa dimatikan saat tidak ada aktivitas  |
| Observed Issue (Symptom) | Lampu menyala lebih dari 12 jam per hari |
| Diagnosed Problem (Root Cause) | Tidak ada sistem otomatis berbasis sensor untuk mengontrol lampu |
| Researchable Problem | Belum ada analisis akurasi sensor RIP dan LDR pada smart home lampu otomatis |
| Measurable Variable | Akurasi deteksi, waktu respon, konsumsi listrik |

**Apakah terjebak solution-first thinking?** [ ] Ya / [ * ] Tidak
> Jika ya, kembali ke tahap mana? Tidak ada 

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data sensor RIP dan LDR |
| Process | Mikrokontroler mengolah data sensor dan menentukan kondisi lampu |
| Output | Lampu otomatis ON/OFF|
| Outcome | Penghematan energi listrik |
| Constraints | Sensitivitas sensor, delay sistem, kondisi lingkungan |
| Stakeholders | Pengguna rumah dan peneliti sistem IoT|

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Input Sensor 

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Masalah dijelaskan dengan jelas dan spesifik |
| Measurability | 5 | Variabel dapat diukur secara kuantitatif |
| Relevance | 5 | Berkaitan langsung dengan smart home IoT|
| Testability | 4 | Dapat diuji melalui ekperimen sistem |
| Impact | 5 | Memberikan manfaat penghematan energi|

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Penggunaan lampu rumah yang manual menyebabkan pemborosan energi listrik karena lampu lupa dimatikan. Sistem smart home berbasis IoT dengan sensor RIP dan LDR dapat mengatasi permasalahan tersebut, namun tingkat akurasi deteksi waktu respon sistem belum diketahui secara pesti. Penelitian ini bertujuan untuk menganalisis kinerja sistem smart home berdasarkan parameter akurasi deteksi sensor, waktu respon sistem, dan konsumsi energi listrik untuk meningkatkan efisiensi penggunaan energi pada lingkungan rumah.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah pada saat coding biasanya berupa bug, error sintaks, atau fitur yang tidak berjalan sesuai fungsi sehingga fokusnya adalah memperbaiki sistem agar dapat berjalan dengan benar.Dalam coding, solusi biasanya langsung diterapkan untuk memperbaiki kesalahan
> Masalah riset berfokus pada menemukan kesenjangan pengetahuan yang belum diketahui dan harus dibuktikan melalui eksperimen. Dalam riset diperlukan proses analisis mulai dari fenomena, gejala, akar masalah, hingga variabel terukur sebelum menentukan solusi. Oleh karena itu, masalah riset lebih terstruktur, terukur, dan harus dapat diuji secara ilmiah.
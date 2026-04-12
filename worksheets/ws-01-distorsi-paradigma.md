# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Hanifah
Tanggal          : 12 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Apakah akurasi 95% dihitung menggunakan dataset yang sama atau data di uji berbeda?
   - Data yang dibutuhkan untuk verifikasi: Metode validasi (cross validation), confusion matrix, dan perbandingan dengan metode lain. 

2. Posisi paradigma:
   - Pendekatan: [*] Positivis  [ ] Interpretivis  [*] Design Science  [ ] Mixed
   - Alasan: Penelitian menguji metode secara kuantitatif dan membangun model algoritma untuk meningkatkan performa.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Dataset mewakili kondisi nyata 
   - Sumber bias potensial: Dataset kecil dan hanya satu sumber data
   - Langkah mitigasi: Menggunakan cross validation dan dataset berbeda untuk pengujian 

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Data hasil eksperimen dan nilai akurasi
   - Batasan yang diakui sejak awal: Dataset terbatas dan belum diuji pada data real time
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Peningkatan Performa Naïve Bayes dengan Information Gain untuk Klasifikasi Kanker Payudara
> Penulis (Tahun): Mardiana, Jasmir, Sharipuddin (2025)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengambil dataset kanker payudara Wisconsin | Dataset tidak mewakili semua pasien |
| Data → Processing | Seleksi fitur menggunakan Information Gain | Fitur tertentu dibuang tanpa analisis mendalam |
| Processing → Analysis | Melatih model Naïve Bayes | Tidak dibandingkan dengan banyak algoritma |
| Analysis → Inference | Akurasi meningkat setelah seleksi fitur | Peningkatan kecil dianggap signifikan |
| Inference → Knowledge | Menyimpulkan metode lebih baik | Generalisasi terlalu luas |

**Distorsi paling besar di tahap:**  Inference → Knowledge

**Dua distorsi spesifik yang teridentifikasi:**
1. Generalisasi hasil dari satu dataset ke semua kasus 
2. Menganggap peningkatan kecil sebagai peningkatan signifikan

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Laporkan hasil dengan dan tanpa outlier |
| Transparansi | Jelaskan alasan penghapusan outlier |
| Peer review | Reviewer harus meminta data mentah |

**Keputusan akhir dan justifikasi:**
> Outlier tidak boleh dihapus tanpa alasan metodologis, kedua hasil harus dilaporkan agar penelitian tetap objekti

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** ________________________________________

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 1 | 5 |
| Jenis data yang dikumpulkan | Data numerik akurasi | Tidak relevan | Data performa algoritma |
| Limitasi paradigma | Fokus angka saja | Tidak cocok untuk algoritma | Bergantung data set |

**Paradigma yang dipilih:** Design Science
**Alasan:** Penelitian bertujuan membangun model algoritma baru untuk meningkatkan performa sistem
---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum membaca materi ini, saya belum mempertanyakan klaim "95% akurat" dan langsung menganggap metode tersebut lebih baik. Setelah memahami rantai distorsi, saya akan menanyakan dataset yang digunakan, metode validasi, ukuran data, serta apakah hasil tersebut dibandingkan dengan metode lain. Saya juga akan mempertanyakan apakah peningkatan performa benar-benar signifikan atau hanya terjadi pada dataset tertentu saja.

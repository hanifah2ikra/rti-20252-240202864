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
   - Pertanyaan pertama saya: Apakah peningkatan efisiensi energi benar disebabkan oleh sistem IoT atau faktor lain (misalnya perilaku pengguna)?
   - Data yang dibutuhkan untuk verifikasi: Data konsumsi listrik sebelum dan sesudah implementasi
Jumlah sampel rumah yang diuji
Kondisi lingkungan (internet, penggunaan perangkat) 

2. Posisi paradigma:
   - Pendekatan: [*] Positivis  [ ] Interpretivis  [*] Design Science  [ ] Mixed
   - Alasan: Positivis karena ada pengukuran kuantitatif (penurunan energi 12–15%)
   Design Science karena penelitian membangun artefak berupa sistem smart home IoT

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Semua rumah memiliki kondisi penggunaan energi yang sama. Koneksi internet stabil
   - Sumber bias potensial: Pengujian hanya dilakukan dalam waktu singkat (±1 minggu). Tidak ada variasi banyak pengguna/rumah
   - Langkah mitigasi: Gunakan dataset lebih besar (lebih banyak rumah). Uji dalam jangka waktu lebih lama. Bandingkan dengan baseline yang jelas

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Data konsumsi listrik dan Data hasil pengujian sistem
   - Batasan yang diakui sejak awal: Ketergantungan pada internet dan Risiko keamanan data
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Implementasi Internet of Things (IoT) pada Sistem Smart Home
> Penulis (Tahun): Asty Raisha Agma (2025)
> Sumber: Jurnal Informatika Indonesia

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengambil data dari sistem smart home dan sensor |Hanya diuji pada satu rumah / skenario |
| Data → Processing | Data sensor diproses oleh microcontroller & aplikasi | Noise sensor tidak dijelaskan |
| Processing → Analysis | Analisis efisiensi energi & respon sistem | Tidak ada uji statistik mendalam|
| Analysis → Inference | Disimpulkan terjadi penghematan 12–15% | Bisa dipengaruhi faktor lain |
| Inference → Knowledge | Klaim IoT meningkatkan efisiensi & keamanan | Generalisasi terlalu luas|

**Distorsi paling besar di tahap:**  Analysis → Inference

**Dua distorsi spesifik yang teridentifikasi:**
1. Sampling bias → hanya diuji pada skala kecil
2. Confounding variable → penghematan energi bisa karena perilaku pengguna 


---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Harus melaporkan hasil dengan dan tanpa outlier |
| Transparansi | Jelaskan alasan penghapusan data outlier
Sertakan metode deteksi outlier |
| Peer review | Reviewer harus mengecek apakah penghapusan data valid |

**Keputusan akhir dan justifikasi:**
> Laporkan kedua hasil (dengan dan tanpa outlier)
Karena menghapus data tanpa alasan kuat termasuk manipulasi (melanggar etika penelitian)

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** ________________________________________

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 2 | 5 |
| Jenis data yang dikumpulkan | Data sensor, konsumsi energi| TTidak dominan | Hasil uji sistem |
| Limitasi paradigma | Tidak menangkap perilaku user | TTidak relevan | Fokus artefak, bukan teori murni |

**Paradigma yang dipilih:** Positivis dan Design Science
**Alasan:** Ada pengukuran kuantitatif (energi, respon sistem). Ada pembangunan sistem (artefak IoT smart home)
---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum membaca materi ini, saya cenderung belum terlalu mempertanyakan klaim seperti “95% akurat” dan langsung menganggap bahwa hasil tersebut benar serta dapat dipercaya.
Namun, setelah memahami konsep Research Trust Model dan rantai distorsi, saya menjadi lebih kritis. Saat membaca paper (termasuk jurnal IoT smart home yang saya gunakan), saya akan mengajukan beberapa pertanyaan penting seperti:
Data: Apakah data yang digunakan cukup representatif atau hanya berasal dari satu skenario saja? (misalnya hanya satu rumah atau satu kondisi uji)
Metodologi: Bagaimana proses pengujian dilakukan? Apakah durasi pengujian cukup panjang atau hanya dalam waktu singkat (misalnya 1 minggu)?
Analisis: Apakah hasil sudah diuji secara statistik atau hanya berdasarkan observasi sederhana?
Inference (kesimpulan): Apakah peningkatan performa benar disebabkan oleh sistem (IoT), atau ada faktor lain seperti perilaku pengguna atau kondisi lingkungan?
Generalisasi: Apakah hasil tersebut bisa diterapkan secara luas, atau hanya berlaku pada kondisi tertentu (misalnya bergantung pada koneksi internet)?
Kesimpulan: Sekarang saya tidak langsung percaya pada angka seperti “95% akurat”, tetapi akan melihat bagaimana data dikumpulkan, diproses, dan dianalisis, serta mempertimbangkan kemungkinan distorsi di setiap tahap penelitian.

# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 11 Slides (target: 9 konten inti + title/closing)
  Time per slide : ~1.5 - 2 menit
  Total time     : 15 menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title : Evaluasi Latensi AES-128 vs Plaintext | Foto Perangkat NodeMCU ESP8266 | 1.0 min  |
| 2 | Problem : Kerentanan Plaintext Smart Home | Diagram Sniffing Serangan Man-in-the-Middle | 2 min  |
| 3 | Gap + RQ : Ketakutan Subjektif Latensi Enkripsi | Matriks Literatur Celah Penelitian | 1.5 min  |
| 4 | Method Overview: Skema Eksperimen Terkontrol | Flowchart Protokol MQTT & Penanda Waktu | 2 min |
| 5 | Key Result: Tabel Statistik Deskriptif RTT | Tabel Performa (Mean ± Std, n=200) | 2 min |
| 6 | Key Result: Deteksi Tren Jitter & Pola Makro | Bar Chart RTT + Box Plot Distribusi Data | 2 min |
| 7 | Interpretation: Dampak Riil Kriptografi Xtensa | Formula Overhead & Justifikasi Fungsional | 2 min |
| 8 | Limitation: Batasan Arsitektur Jaringan LAN | Peta Topologi Laboratorium Terisolasi | 1.5 min |
| 9 | Conclusion: Enkripsi AES Ringan & Layak Pakai | Rekomendasi Teknis Penyusunan Firmware | 1 min |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Mengapa fokus pada RTT, bukan aspek konsumsi daya baterai? | Cepat lambatnya respons kendali fisik adalah parameter vital kenyamanan smart home [C]. Data pengujian mengukur RTT dalam satuan milidetik [E]. Latensi nirkabel yang buruk merusak pengalaman real-time pengguna [R] |
| Gap      | Apa pembeda riset ini dengan tulisan Pramono dkk.? | Riset terdahulu hanya menguji fungsionalitas kirim [C]. Tabel gap menunjukkan tidak adanya metrik kuantitatif overhead [E]. Penambahan data mikrodetik mengisi data gap teoretis industri [R] |
| Method   | Mengapa memakai Welch's t-test, bukan t-test biasa? |Ukuran sampel kedua kelompok tidak seimbang akibat packet drop [C]. Kelompok Plaintext berukuran n=100 sedangkan AES n=98 [E]. Welch's t-test robust meredam bias variansi tidak sama [R] |
| Results  |                     |               |
| Generalization |               |               |

Latihan:
  Latihan 1: [tanggal] — [catatan timing & feedback]
  Latihan 2: [tanggal] — [catatan timing & feedback]
  Latihan 3: [tanggal] — [catatan timing & feedback]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Title: Dampak Enkripsi AES-128 pada NodeMCU ESP8266 | Slide judul formal, logo kampus, foto miniatur alat | 1 min |
| 2 | Problem: Data IoT dikirim plaintext memicu sniffing siber | Ilustrasi intersepsi paket data sakelar lampu via Wireshark | 2 min |
| 3 | Gap + RQ: Apakah enkripsi memperlambat sistem secara ekstrem? | Matriks komparasi studi terdahulu untuk menegaskan posisi riset | 1.5 min |
| 4 | Method Overview: Setup pengujian terisolasi (N=200 paket) | Skema topologi Wi-Fi lokal, kode fungsi micros() firmware | 2 min|
| 5 | Key Result: Tabel performa komparatif statistik| Tabel ringkasan data RTT (Mean ± Std) dan Packet Loss Rate| 2 min|
| 6 | Key Result: Grafik sebaran seimbang vs anomali nirkabel | Kombinasi Bar Chart (+error bar) berdampingan dengan Box plot | 2 min |
| 7 | Interpretation: Beban komputasi aman bagi kenyamanan manusia | Visualisasi perbandingan penalti $3.18\text{ ms}$ vs ambang batas waktu nyata | 2 min |
| 8 | Limitation: Eksperimen terisolasi di LAN tanpa cloud delay | Diagram batasan ruang lingkup uji laboratorium | 1.5 min |
| 9 | Conclusion: Hambatan psikologis enkripsi IoT terpatahkan | Teks poin utama kontribusi data empiris, foto penutup | 1 min |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Problem | Mengapa latensi 3.18 ms dianggap penting untuk diteliti? | Selisih kecil ini mematahkan dogma ketakutan pengembang IoT. | Rerata RTT naik dari 15.24 ms ke 18.42 ms (p< 0.001). | Angka absolut 18.42 ms membuktikan enkripsi siber tidak merusak fungsi real-time. |
| 2 | Method | Mengapa sampel dikurangi dari 200 menjadi 198? | Terjadi packet loss alami yang tidak bisa dihindari. | Deteksi log menunjukkan ada 2 paket timeout pada kelompok AES | Menghapus data missing via listwise deletion demi akurasi uji t-test|
| 3 | Results | Bagaimana Anda menjelaskan lonjakan data 45.12 ms? | Itu adalah anomali kontekstual akibat gangguan frekuensi Wi-Fi | Grafik box plot memisahkan data tersebut sebagai titik pencanduan terisolasi| Karakteristik fisik gelombang radio 2.4 GHz rentan terhadap interferensi sesaat |
| 4 | Method | Mengapa tidak menggunakan enkripsi asimetris seperti RSA? | Chip mikro Xtensa LX106 tidak memiliki unit komputasi yang cukup kuat | Kajian literatur menunjukkan RSA membutuhkan waktu proses detik, bukan milidetik | Komputasi berat RSA akan membuat sistem membeku (freeze), tidak cocok untuk IoT |
| 5 | Generalization | Apakah hasil ini berlaku jika alat dipasang di luar lab? | Tidak sepenuhnya, performa luar lab akan dipengaruhi internet publik | Bab batasan menegaskan bahwa pengujian dikunci pada arsitektur LAN lokal | Jaringan internet global membawa variabel cloud delay yang fluktuatif |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|| *1* | *Contoh: "Mengapa tidak membandingkan dengan metode Y?"* | *Contoh: "Karena Y memerlukan dataset labeled yang tidak tersedia. Disebutkan sebagai limitasi di halaman X."* | *[✓] Direct [✓] Data-based [✓] Honest* |
| 1 | "Mengapa Anda tidak menormalisasikan data RTT Anda ke skala [0,1]?" | "Tidak dinormalisasi karena metrik RTT mencerminkan satuan fisik milidetik riil yang bermakna fisis langsung. Jika diubah ke skala desimal abstrak, interpretasi beban overhead siber asli justru akan hilang." | [x] Direct [x] Data-based [x] Honest |
| 2 | "Apakah jumlah sampel 100 per kelompok sudah memenuhi syarat?" | "Sudah memadai. Merujuk pada Teorema Limit Pusat (Central Limit Theorem), ukuran sampel N > 30 membuat nilai rerata sampel berdistribusi normal, sehingga uji parametrik t-test valid digunakan." | [x] Direct [x] Data-based [ ] Honest |
| 3 | "Riset Anda gagal membuktikan enkripsi itu bebas tunda, lalu apa gunanya?" | "Benar bahwa enkripsi menambah tunda. Namun, penelitian ini berhasil membuktikan bahwa penambahan tunda tersebut secara praktis sangat kecil ($3.18\text{ ms}$), sehingga mengamankan sistem tanpa mengorbankan performa." | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Menjustifikasi mengapa pengujian tidak langsung dilakukan pada jaringan internet global (Cloud), melainkan dibatasi pada jaringan lokal (LAN)

**Apa yang perlu disiapkan lebih baik:**
> Menyiapkan slide lampiran (backup slides) tambahan yang memuat grafik perbandingan literatur eksternal untuk memperkokoh argumen interpretasi performa mikrokontroler

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Pemahaman fundamental bahwa riset adalah sebuah bangunan argumen logis yang utuh, bukan sekadar aktivitas mengetik laporan atau merakit alat di laboratorium. Mulai dari perumusan masalah, pencarian celah literatur (gap), preprocessing data, hingga teknik menjawab pertanyaan penguji, seluruhnya harus terikat oleh satu benang merah (red thread) yang konsisten. Keberhasilan riset tidak diukur dari seberapa canggih sistem yang dibuat, melainkan dari kejujuran data, kejelasan metodologi, serta ketajaman analisis dalam memetakan batas kemampuan (boundary condition) dari objek yang diteliti

**Yang akan selalu diterapkan:**
> Saya akan selalu menerapkan Urutan Penulisan Terbalik (Method → Results → Discussion → Introduction) dan menggunakan pendekatan Claim-Evidence-Reasoning (CER) dalam menyajikan argumen ilmiah. Pendekatan ini terbukti sangat ampuh dalam menjaga objektivitas berpikir, mencegah terjadinya manipulasi visualisasi (visualization bias), serta memastikan bahwa setiap klaim yang saya utarakan di hadapan publik selalu berdiri kokoh di atas fondasi bukti empiris data laboratorium yang valid

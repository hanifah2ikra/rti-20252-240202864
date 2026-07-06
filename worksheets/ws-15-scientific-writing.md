# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Evaluasi Komparatif Dampak Enkripsi AES-128 Terhadap Latensi Jaringan Nirkabel Lokal pada Mikrokontroler NodeMCU ESP8266
Target  : [x] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata) (Masalah plaintext, metode eksperimen, penalti RTT 3.18 ms,)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper (Urgensi smart home → celah fungsionalitas vs siber → RQ latensi → kontribusi data riil)
  [x] Related Work — concept-centric, gap positioning (Pemetaan literatur Pramono & Muntahar (2024) serta Hamka dkk. (2025))
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur (Reproducible: NodeMCU 80 MHz, payload 16 Byte, MQTT Mosquitto, fungsi micros())
  [x] Results — tabel + grafik + observasi (tanpa interpretasi) (Tabel statistik deskriptif + grafik bar chart RTT (Plaintext 15.24 ms vs AES 18.42 ms).)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation (Interpretasi komputasi Xtensa, pengujian Welch's t-test, batasan LAN terisolasi.)
  [x] Conclusion — jawaban RQ, kontribusi, future work ada penalti signifikan secara statistik, namun aman secara fungsional)

Consistency Matrix:
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [x] Clarity — mudah dipahami tanpa re-read
  [x] Precision — tidak ada istilah ambigu
  [x] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Transmisi data nirkabel smart home saat ini mayoritas dikirim dalam format plaintext tanpa proteksi kriptografi karena kekhawatiran subjektif pengembang terhadap penalti latensi CPU berdaya rendah. Penelitian ini menguji secara kuantitatif dampak penerapan enkripsi AES-128 terhadap durasi Round Trip Time (RTT) paket data pada chip NodeMCU ESP8266 melalui 200 kali uji coba terisolasi. Hasil uji statistik Welch's t-test menunjukkan peningkatan delay rata-rata sebesar 3.18 ms (< 0.001), membuktikan bahwa sistem tetap responsif di bawah batas fungsional real-time. | 200-250 |
| Introduction | Eskalasi adopsi perangkat IoT rumah pintar tidak dibarengi dengan kesadaran keamanan yang memadai pada level firmware. Pengembang kerap menghindari enkripsi simetris standar industri (AES-128) karena mengasumsikan kalkulasi matematika akan membebani siklus jam CPU mikroprosesor Xtensa LX106 secara masif. Penelitian ini bertujuan memberikan pembuktian empiris untuk menjawab dilema trade-off antara aspek kerahasiaan data dengan efisiensi hantar paket nirkabel | 500-700 |
| Related Work | Bagian ini memetakan penelitian terdahulu mengenai implementasi fungsional NodeMCU ESP8266 oleh Pramono & Muntahar (2024) serta analisis integrasi relay nirkabel oleh Hamka dkk. (25). Posisi riset ini diplot untuk mengisi kekosongan data (data gap) kuantitatif terkait pengujian performa mikrodetik pasca-integrasi pustaka kriptografi siber pada firmware bersangkutan | 700-1000 |
| Method | Eksperimen laboratorium terkontrol membandingkan Kelompok Baseline (Plaintext, n=100) dan Kelompok Intervensi (AES-128 Enabled, n=98). Parameter dikunci konstan pada ukuran payload data 16 Byte, jarak router 5 meter, RSSI -60 dBm, dan protokol MQTT. Pengumpulan data metrik RTT memanfaatkan fungsi penanda waktu internal perangkat lunak micros() sebelum dianalisis menggunakan Independent Samples t-Test | 800-1200 |
| Results | Penyajian data deskriptif menunjukkan nilai rata-rata RTT untuk kelompok Plaintext adalah 15.24 ± 0.42 ms dan kelompok AES-128 adalah 18.42 ± 1.15 ms. Data disajikan terperinci menggunakan format tabel ringkas berdampingan dengan diagram bar chart yang dilengkapi bilah ketidakpastian (error bar), serta menampilkan 1 titik anomali kontekstual bernilai 45.12 ms | 500-800 |
| Discussion | Hasil kalkulasi membuktikan adanya overhead tambahan sebesar 3.18 ms akibat transformasi matematis internal chip. Efek intervensi tercatat sangat masif (Cohen's d = 3.65), namun secara fungsional tunda ini tidak mengganggu responsivitas aksi sakelar fisik. Batasan penelitian ini terletak pada isolasi arsitektur jaringan lokal (LAN) tanpa melibatkan variabel cloud delay.| 600-900 |
| Conclusion | Penerapan enkripsi AES-128 terbukti menaikkan latensi transmisi secara signifikan secara statistik, namun kinerjanya secara praktis sangat aman bagi efisiensi sistem IoT. Kontribusi utama riset ini adalah runtuhnya kekhawatiran subjektif mengenai beban enkripsi pada mikrokontroler kelas rendah. Penelitian masa depan disarankan mengevaluasi protokol TLS/MQTT pada jaringan internet global | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| *Contoh: RQ1* | *✓* | *✓* | *✓* | *✓* | *✓* |
| *Contoh: Metrik-X* | *✗ ←* | *✗ ←* | *✓* | *✗ ←* | *✗ ←* |
| RQ1 (Apakah AES menaikkan RTT?) | ✓ | ✓ | ✓ | ✓ | ✓ |
| RQ2 | | | | | |
| Metrik utama (RTT dalam ms) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel IV (Status Enkripsi) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel DV (Kecepatan Hantar) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Klaim/kontribusi (Overhead Aman) | ✓ | ~ | ✓ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Pada bagian Method, klaim kontribusi akhir riset mengenai efisiensi fungsional sistem IoT masih berstatus parsial (~), karena fokus bab tersebut murni menjelaskan prosedur operasional pengumpulan data tanpa mengaitkan narasi dengan implikasi praktis industri.

**Tindakan perbaikan:**
> Menambahkan kalimat transisi penutup pada bagian akhir sub-bab Method/Analysis Technique untuk menegaskan bahwa batas nilai pengujian statistik beda rerata ini nantinya akan dikonfrontasikan dengan ambang batas fungsional waktu nyata (real-time threshold) siber.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Pengujian dilakukan dengan mengirimkan data ke broker. Setelah dicoba berkali-kali, performa dari sistem pintar ini kelihatan mengalami sedikit penurunan kecepatan hantar data yang lumayan berasa pas enkripsinya dinyalain di software alat. Hal ini terjadi karena mikrokontroler harus mikir dulu buat memproses rumus matematika enkripsinya sebelum dipancarin lewat antena Wi-Fi yang ada di modul NodeMCU ESP8266.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Istilah "sedikit penurunan kecepatan hantar" dan "lumayan berasa" bersifat abstrak, sangat subjektif, dan tidak informatif bagi pembaca teknis | Mengubah kalimat menjadi pernyataan kuantitatif berbasis angka riil rata-rata hasil eksperimen (15.24 ms ke 18.42 ms) |
| Precision | Kata "mengirimkan data" dan "mikir dulu buat memproses rumus" tidak standar, ambigu, serta tidak mencerminkan terminologi ilmiah teknik siber | Mengganti frasa dengan istilah eksak spesifik IT: "transmisi instruksi kendali 16 Byte via protokol MQTT" dan "siklus eksekusi transformasi kriptografi" |
| Conciseness | Kalimat menggunakan kata-kata non-baku dan pemborosan struktur pengisi (filler) seperti "pas enkripsinya", "kelihatan mengalami", "yang ada di" | Menyederhanakan kalimat, membuang kata mubazir, dan menyusunnya kembali dengan struktur kalimat pasif formal |

**Paragraf setelah perbaikan:**
> Pengujian komparatif transmisi instruksi kendali sebesar 16 Byte melalui protokol MQTT menunjukkan adanya peningkatan nilai rata-rata Round Trip Time (RTT) dari 15.24 ms pada kondisi plaintext menjadi 18.42 ms saat fungsi enkripsi diaktifkan. Penalti latensi sebesar 3.18 ms ini disebabkan oleh alokasi siklus kerja CPU Xtensa LX106 untuk mengeksekusi tahapan transformasi kriptografi simetris AES-128 sebelum paket dimodulasikan ke transceiver Wi-Fi

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset sekadar mengubah catatan harian laboratorium menjadi teks naratif, di mana peneliti hanya melaporkan kronologi aktivitas tanpa arah pembuktian yang jelas (misal: "kami memasang modul, lalu kami mengambil data"). Sebaliknya, menulis sebagai sebuah "argumen" riset berarti memosisikan seluruh struktur tulisan sebagai senjata logis yang koheren untuk mempertahankan atau membuktikan validitas sebuah klaim ilmiah. Setiap kalimat, tabel, dan metodologi diarahkan secara ketat untuk menjawab pertanyaan penelitian (Research Question) dan meruntuhkan keraguan di celah riset (gap).
> Mengubah urutan penulisan dengan mendahulukan penyusunan bab Method dan Results berdampak masif pada peningkatan objektivitas dan kualitas karya ilmiah. Ketika kita menulis bagian Method dan Results terlebih dahulu, kita sedang membangun fondasi berbasis kebenaran data riil yang paling stabil di laboratorium. Dari pijakan data yang konkret tersebut, bab Discussion dapat dirumuskan secara tajam tanpa spekulasi berlebih. Pada akhirnya, bab Introduction dapat dibingkai (framed) secara jujur dan presisi, menghindari jebakan penulisan janji-janji teoretis yang bombastis di awal namun ternyata tidak mampu dibuktikan oleh data hasil eksperimen nyata di akhir paper

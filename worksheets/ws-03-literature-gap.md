# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Implementasi dan Optimalisasi Sistem Smart Home & Keamanan Berbasis IoT
Database   : Google Scholar
Query      : ("smart home" OR "rumah pintar") AND ("IoT" OR "Internet of Things") AND ("NodeMCU" OR "ESP32")
Tahun      : 2024-2025
Hasil awal : 20 paper → Screening → 6 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|Agma|2025 | Implementasi IoT Terintegrasi |	Sensor suhu, kelembaban, gerak, aplikasi mobile |Meningkatkan kenyamanan & efisiensi energi|Belum merinci detail waktu respons sistem|
|Hadiatullah dkk.|2025 |Research & Development (R&D) |NodeMCU ESP8266, Relay, Jaringan Wi-Fi |Koneksi stabil, respons < 10 detik, operasional 24 jam |Antarmuka aplikasi (UI) perlu perbaikan |
|Ferella dkk.|2025 |Prototyping (Kamera IoT) |Modul Kamera, NodeMCU, Web/Mobile App|Respons cepat, notifikasi otomatis aktivitas mencurigakan |Fokus terbatas pada keamanan visual |
|Pramono & Muntahar|2024 |Extreme Programming (XP)|NodeMCU ESP8266, CCTV, ATS Power |Akurasi deteksi 95%, delay rata-rata 2 detik|Belum mencakup optimalisasi konsumsi daya perangkat|
|Hamka dkk.|2025 |Research & Development (R&D)|ESP32, Blynk Cloud, Smart Lighting|Sistem responsif (rata-rata 73,4 ms), hemat energi|Isu keamanan privasi dan keterbatasan akses internet|
|Sari dkk.|2024 |Literature Review|Arduino Uno, Sensor, IoT di Pertanian|Identifikasi potensi IoT untuk efisiensi operasional|Kurangnya implementasi hardware secara langsung|

Pola yang ditemukan:
  Metode dominan     : Research and Development (R&D) dan Prototyping.
  Dataset umum       : NodeMCU (ESP8266/ESP32), Modul Relay, dan sensor lingkungan (suhu/gerak).
  Limitasi berulang  : Ketergantungan tinggi pada koneksi internet (Wi-Fi), masalah latensi pada jaringan buruk, dan kurangnya fitur enkripsi data yang mendalam.

GAP IDENTIFICATION

Gap 1: [Jenis : Performance/ Method Gap
  Deskripsi    : Kurangnya standarisasi pada protokol keamanan data (enkripsi) untuk mencegah peretasan akses kontrol rumah.
  Bukti        : Mayoritas jurnal (Pramono 2024, Hamka 2025) fokus pada fungsionalitas kendali, namun belum mendemonstrasikan proteksi terhadap serangan cyber.
  Signifikansi : Keamanan adalah aspek krusial; tanpa enkripsi, sistem kendali rumah pintar bisa disalahgunakan oleh pihak luar.
Gap 2: [Jenis: Context Gap]
  Deskripsi    : Kesenjangan efektivitas sistem saat terjadi gangguan bandwidth atau di wilayah dengan konektivitas rendah.
  Bukti        : Hadiatullah (2025) menyebutkan interferensi Wi-Fi sebagai kendala, namun belum ada solusi mekanisme offline atau low-bandwidth mode.
  Signifikansi : Sistem IoT harus tetap andal (reliable) bahkan dalam kondisi jaringan tidak stabil agar dapat digunakan di berbagai wilayah (termasuk pelosok).

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|Sistem Smart Lighting (ESP32)|Sangat relevan untuk efisiensi energi.|Mewakili penggunaan framework Blynk yang populer.|Hamka dkk. (2025)|
|Sistem Keamanan Android (XP) |Relevan untuk kontrol keamanan rumah. |Menggunakan metode pengembangan perangkat lunak terstruktur (XP). | Pramono & Muntahar (2024)|
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Implementasi dan Optimalisasi Sistem Smart Home & Security berbasis IoT
**Query pencarian:** ("smart home" OR "rumah pintar") AND ("IoT" OR "Internet of Things") AND ("NodeMCU" OR "ESP32")
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
| 1 | Hamka dkk. | 2025 | R&D (ESP32 + Blynk) | Lampu, ESP32, Cloud Blynk | Respons cepat (73,4ms), kendali jarak jauh stabil.| Tergantung penuh pada internet & keamanan data minim. |
| 2 | Hadiatullah dkk.|2025 |R&D (NodeMCU) |Relay, Wi-Fi, Mobile App |Respons < 10 detik, operasional 24 jam stabil. |UI aplikasi perlu perbaikan & isu interferensi Wi-Fi. |
| 3 |Pramono & Muntahar |2024 |Extreme Programming (XP) |NodeMCU, CCTV, Android |Akurasi deteksi 95%, delay rata-rata 2 detik. |Belum optimal dalam manajemen konsumsi daya. |
| 4 |Ferella dkk.|2025|Prototyping (Kamera)|ESP32-Cam, MQTT/HTTP |Deteksi gerakan & monitoring real-time berhasil. |Sudut pandang kamera terbatas (static).|
| 5 |Agma |2025 |Implementasi Integrasi |Sensor DHT11, PIR, LDR |Otomasi suhu & lampu berhasil meningkatkan efisiensi.|Tidak merinci detail parameter latensi sistem.|

**Pola yang terlihat — Metode dominan:** Research and Development (R&D) dengan pengujian prototipe fungsional.
**Limitasi yang berulang:** Keamanan privasi data (enkripsi), ketergantungan pada stabilitas sinyal Wi-Fi, dan optimasi daya perangkat.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ * ] Ya / [ ] Tidak | Sebagian besar sistem mengalami peningkatan delay (latensi) saat beban jaringan tinggi atau sinyal lemah. |
| Method Gap | [ * ] Ya / [ ] Tidak | Belum adanya penerapan algoritma keamanan (seperti AES atau Two-Factor Authentication) pada akses kontrol pintu/lampu. |
| Data Gap | [ ] Ya / [ ] Tidak | |
| Context Gap | [ * ] Ya / [ ] Tidak | Implementasi lebih banyak diuji pada lingkungan ideal (kampus/lab), belum pada rumah dengan kendala listrik tidak stabil.|

**Gap utama yang dipilih:** Method Gap (Security & Reliability)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena sistem rumah pintar mengontrol akses fisik (pintu/kamera). Jika hanya fokus pada fungsionalitas tanpa enkripsi kuat, sistem ini justru menjadi celah keamanan baru bagi peretas untuk menyusup ke privasi penghuni.
---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Smart Lighting ESP32| Fokus pada kecepatan respons kendali lampu.| Menggunakan Blynk, platform paling umum di riset IoT. | Ya (2025) | Hamka dkk., 2025|
| 2 |Security System NodeMCU (XP) |Fokus pada akurasi deteksi keamanan. |Mewakili metode pengembangan software terstruktur (XP). |Ya (2024)|Pramono & Muntahar, 2024 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [*] Tidak
> Justifikasi: Baseline yang dipilih adalah penelitian terbaru (2024-2025) dengan tingkat akurasi tinggi (95%). Membandingkan riset baru dengan standar ini merupakan tantangan yang jujur, bukan membandingkan dengan teknologi usang.
---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Perbedaan antara klaim tanpa bukti dengan research gap yang valid terletak pada penelusuran literatur yang terdokumentasi. Klaim "belum ada" tanpa data adalah asumsi, sedangkan gap yang valid dibuktikan dengan tabel perbandingan (Latihan 1) yang menunjukkan bahwa meskipun banyak penelitian dilakukan, ada aspek tertentu (seperti keamanan enkripsi) yang secara konsisten belum dipecahkan atau diabaikan oleh peneliti-peneliti sebelumnya.
> ___________________________________________________

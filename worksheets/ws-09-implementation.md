# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Tensilica Xtensa LX106 (32-bit RISC), Clock Speed 80 MHz
  RAM     : 160 KB System RAM (Internal SRAM NodeMCU ESP8266)
  GPU     : CPU-only (Tidak menggunakan akselerasi grafis/GPU)
  Storage : 4 MB External SPI Flash Memory (W25Q32)

Software:
  OS        : Windows 11 Pro 64-bit (Host OS untuk development & Python data logging)
  Runtime   : Arduino IDE v2.3.2 / ESP8266 Board Core for Arduino v3.1.2
  Framework : Local MQTT Network Architecture (Mosquitto MQTT Broker v2.0.18)

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| ESP8266WiFi | 1.0.0 | Built-in ESP8266 Core | sha256:d41d8cd98f00b204e9800998ecf8427e |
|PubSubClient (by Nick O'Leary)|2.8.0|Arduino Library Manager|sha256:a6b28f7311c81ef8d4b31e9c20a842b1|
|Crypto (by Rhys Weatherley) | 0.4.0 |GitHub (rweather/arduinolibs) |sha256:7f81b32d12e84cf91cb21b043901a1d2|
|ArduinoJson|7.0.4|Arduino Library Manager|sha256:e3b0c44298fc1c149afbf4c8996fb924|
|Pyserial (Python Host Side) |3.5 |PyPI (pip install pyserial) |sha256:8f421a118f12ef4b3c149afbf4c889a6 |

Konfigurasi:
  Config file     : config.h (C++ header file) & settings.json (Python telemetry logger config)
  Random seed     : 42 (Di-set pada fungsi inisialisasi Initialization Vector / IV untuk enkripsi blok AES-128)
  Hyperparameters : MQTT_QOS = 0 (At-most-once delivery
  PAYLOAD_SIZE = 16 Byte (128-bit konstan)
  WIFI_RSSI_THRESHOLD = -60 dBm
  EXPERIMENT_TRIALS = 100 pengulangan transmisi per kondisi

Reproducibility Check:
  [x] Dependency terdokumentasi (platformio.ini / requirements.txt untuk script logging Python))
  [x] Seed ditetapkan di semua level (Inisialisasi IV pada modul Crypto C++ dan random generator Python)
  [x] Config di version control (File config.h terbebas dari hardcode kredensial Wi-Fi dan masuk Git)
  [x] README instruksi reproduksi lengkap (Termasuk prosedur flashing firmware dan skenario uji laboratorium)
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Tensilica Xtensa LX106 (32-bit RISC), Clock Speed 80 MHz |
| RAM | 160 KB System RAM (Internal SRAM NodeMCU) |
| GPU | CPU-only (Tidak menggunakan pemrosesan akselerasi grafis/GPU) |
| OS | Windows 11 Pro 64-bit (Host OS untuk development & log parsing) |
| Runtime |Arduino IDE v2.3.2 / ESP8266 Core for Arduino v3.1.2 |
| Framework |MQTT Architecture (menggunakan Local Mosquitto Broker v2.0.18) |
| Random Seed |42 (Digunakan pada inisialisasi Initialization Vector / IV untuk enkripsi AES-128) |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| ESP8266WiFi | 1.0.0 | Menyediakan fungsi tumpukan protokol (protocol stack) Wi-Fi 802.11 b/g/n untuk NodeMCU. |
| PubSubClient | 2.8.0 | Mengelola koneksi, publikasi, dan langganan (subscribe) paket pesan kontrol melalui protokol MQTT. |
| Crypto (by Rhys Weatherley) | 0.4.0 | Menyediakan mesin kriptografi (encryption engine) objek AES-128 blok 16-byte pada level firmware. |
| ArduinoJson | 7.0.4 | Melakukan serialisasi payload data sensor (128-bit) sebelum dienkripsi menjadi string cipher. |
| Pyserial | 3.5 | Pustaka eksternal pada komputer host untuk membaca dan menangkap log telemetri dari port serial NodeMCU ke format CSV. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 |42| End-to-End Latency (RTT) | — |
| 2 |42| End-to-End Latency (RTT)| [ x ] Ya / [ ] Tidak |
| 3 |42| End-to-End Latency (RTT) | [ x ] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> 1. Terjadinya interferensi frekuensi radio (RF) pada kanal 2.4 GHz dari perangkat luar (Wi-Fi tetangga atau Bluetooth) yang memicu retransmisi paket di lapisan MAC.

2. Munculnya tunda latensi sistemik (systemic jitter) akibat proses latar belakang (background task) internal dari tumpukan protokol Wi-Fi non-OS pada ESP8266.

3. Terjadinya fluktuasi panas (thermal throttling) pada chip NodeMCU yang mempengaruhi kestabilan clock internal saat melakukan eksekusi fungsi perulangan matematika enkripsi secara masif.

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level
- [x] Tidak ada background process yang mengganggu
- [x] Cache dibersihkan antar-run
- [x] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Analisis Perbandingan Performa Jaringan dan Latensi pada Sistem Smart Home Berbasis IoT Menggunakan Enkripsi AES-128 dan Komunikasi Tanpa Enkripsi

## 1. Environment
> Hardware: NodeMCU ESP8266 (Tensilica LX106 80MHz, 160KB RAM), Local PC Router Testbed.
OS & Runtime: Windows 11 Host, Arduino IDE v2.3.2, ESP8266 Core v3.1.2.
Network Platform: Mosquitto MQTT Broker v2.0.18 (Local LAN Setup).

## 2. Installation
> 1. Unduh dan pasang Arduino IDE v2.3.2.
2. Tambahkan URL Board Manager ESP8266 dan pasang ESP8266 Core v3.1.2.
3. Pasang pustaka 'Crypto' oleh Rhys Weatherley dan 'PubSubClient' via Library Manager.
4. Install Python 3.11 dan jalankan perintah: pip install pyserial untuk script log collector.

## 3. Data
> Jenis Data: Log telemetri performa nirkabel berformat CSV (`telemetry_log.csv`).
Atribut Data: Iterasi Uji (1-100), Status Enkripsi (0=Plaintext, 1=AES-128), Timestamp Kirim (μs), Timestamp ACK (μs), Round Trip Time (ms).
Ukuran Payload Data: Paket kontrol biner konstan berukuran 128-bit (16 Byte).

## 4. Execution
> 1. Nyalakan Broker MQTT Lokal pada komputer host.
2. Unggah file firmware `baseline_plaintext.ino` ke NodeMCU, jalankan script Python logger, dan biarkan mentransmisikan 100 paket.
3. Unggah file firmware `intervention_aes128.ino` ke NodeMCU, jalankan kembali script Python logger untuk merekam 100 paket kedua.
4. Jalankan script analisa `t_test_analyzer.py` untuk mengolah data CSV hasil tangkapan.

## 5. Configuration
> Seluruh parameter operasional dikunci melalui file konfigurasi header `config.h`:
#define WIFI_RSSI_THRESHOLD -60
#define MQTT_PAYLOAD_SIZE 16
#define AES_KEY_SIZE 128
#define EXPERIMENT_TRIALS 100

## 6. Expected Output
> File CSV berisi rekaman presisi durasi waktu hantar, dengan output ringkasan statistik pada konsol berupa:
Mean Latency Plaintext: ~15.2 ms
Mean Latency AES-128: ~18.5 ms
P-Value (Independent t-Test): < 0.05 (Menunjukkan pengaruh overhead enkripsi signifikan secara statistik namun secara praktis masih di bawah batas toleransi real-time 200 ms).
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [ x ] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Komponen yang belum terdokumentasi secara penuh adalah spesifikasi topologi penempatan fisik ruang uji laboratorium (jarak absolut dan redaman dinding pemisah) serta nilai konfigurasi parameter Quality of Service (QoS level 0, 1, atau 2) pada broker MQTT lokal yang dapat mempengaruhi perilaku jabat tangan (handshake) pengiriman paket data konfirmasi ACK.
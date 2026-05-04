# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: "Apakah implementasi protokol MQTT dengan enkripsi TLS/SSL pada ESP32 menghasilkan latency dan packet loss yang secara signifikan berbeda dibandingkan dengan protokol HTTP standar pada sistem smart home?"

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Protokol Komunikasi | IV | Communication Wrapper Module | Mengganti header file atau class antara WiFiClient (HTTP) dan WiFiClientSecure (MQTT+TLS). |
| Latensi & Packet Loss | DV | Telemetry/Logger Module | Fungsi millis() yang mencatat waktu kirim dan terima di dalam kode program.|
| Stabilitas Wi-Fi (RSSI)| CV | Environment Handler | Pembacaan statis melalui fungsi WiFi.RSSI() yang dicatat setiap sesi.|

4 Prinsip Desain:
  [ *] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [ *] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [ *] Measurement Integration — Pengukuran DV built-in
  [ *] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Perintah kontrol (misal: "ON/OFF") yang dikirim sebanyak 100 kali per protokol.
  Parameter      : Frekuensi Wi-Fi 2.4GHz, Jarak 5 meter, ESP32 Clock 160MHz.
  Output format  : Tabel CSV (Timestamp, Protocol_Type, Latency_ms, Success_Status).
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** "Apakah penggunaan algoritma enkripsi AES-128 pada NodeMCU meningkatkan latensi secara signifikan dibandingkan tanpa enkripsi?"

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
|Enkripsi AES-128| IV | Encryption Engine (Library) | Menggunakan Feature Toggle (Boolean isEncrypted = true/false) dalam kode.|
|Latensi | DV |Execution Timer Module |Mencatat selisih waktu sebelum fungsi encrypt() dan sesudah decrypt(). |
|Payload Size | CV |Data Generator |Ukuran pesan dikunci pada 128 bit untuk semua percobaan. |

**Apakah semua variabel bisa di-map?** [ *] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Modul enkripsi dipisahkan dari modul koneksi, memudahkan pelacakan asal delay.|
| Modularity | ✅ | Algoritma AES bisa diganti ke ChaCha20 atau Off tanpa membongkar seluruh program.|
| Controllability | ✅ | Parameter kunci (key) dan ukuran data diatur di bagian config.h.|
| Measurability | ✅ |Sistem mencatat waktu eksekusi dalam mikrosekon (µs) untuk akurasi tinggi. |

**Prinsip mana yang paling sulit dipenuhi?** Variable Isolation.
**Strategi untuk mengatasinya:**
> Menggunakan lingkungan jaringan yang terisolasi (Router khusus tanpa perangkat lain) agar noise jaringan tidak dianggap sebagai delay dari enkripsi.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full |  ✅ Aktif| ✅Aktif | ✅ Aktif| Keamanan maksimal, namun latensi tertinggi |
| – A | ❌ Matikan | ✅Aktif | ✅Aktif |Latensi turun drastis (membuktikan beban AES).|
| – B | ✅Aktif | ❌ Matikan | ✅ Aktif| Bandwidth naik, namun beban CPU turun.|
| – C | ✅ Aktif| ✅Aktif | ❌Matikan| Penghematan waktu handshake awal.|

**Komponen mana yang diprediksi paling berkontribusi?** Komponen A (AES).
**Mengapa?**
> Karena proses enkripsi/dekripsi melibatkan perhitungan matematis intensif pada CPU mikrokontroler yang memiliki resource terbatas.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko utama dari sistem monolitik adalah Confounding Variables (variabel pengganggu). Jika sistem monolitik terasa lambat, peneliti akan sulit menentukan apakah kelambatan itu disebabkan oleh enkripsi, antarmuka grafis (UI), atau proses latar belakang lainnya karena semuanya saling mengunci (tightly coupled).
> Arsitektur modular penting karena:
Isolasi Variabel: Kita bisa mematikan fitur non-riset (misal: tampilan LCD) agar tidak mengganggu pengukuran variabel utama.
Reproduktifitas: Peneliti lain bisa mengambil modul eksperimen Anda saja tanpa harus mengunduh seluruh "produk" Anda yang kompleks.
Fleksibilitas: Memungkinkan Ablation Study (Latihan 3) untuk melihat kontribusi tiap bagian secara adil.
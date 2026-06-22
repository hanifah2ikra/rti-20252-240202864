# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1-100     |Baseline (Plaintext)  | 42 | Payload=16B, QoS=0, RSSI=-60dBm  | Planned |09:00 WIB|log_baseline_plaintext.csv|
| 101-200     | Intervensi (AES-128) | 42| Payload=16B, QoS=0, RSSI=-60dBm | Planned |10:00 WIB| log_intervensi_aes128.csv |
|     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : 100
Total runs               : 200

DATA LOG (per run):
  Run ID    : TX-AES128-045
  Timestamp : 2026-06-21T10:15:32.451Z
  Skenario  : Intervensi (AES-128 Enabled)
  Input     : 0x41 0x42 0x43 0x44 0x45 0x46 0x47 0x48 0x49 0x4A 0x4B 0x4C 0x4D 0x4E 0x4F 0x50 (16-Byte data string "ABCDEFGHIJKLMNOP" dalam bentuk array heksadesimal)
  Output    : RTT = 18.42 ms (Hasil kalkulasi konversi dari selisih waktu balik sinyal konfirmasi: 18420 mikro secon)
  Anomali   : None (Normal Transmission)
  Catatan   : Kestabilan daya tangkap antena Wi-Fi tercatat konstan pada indikator RSSI -59 dBm.
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Baseline (Plaintext)|  42 | Payload = 16B, QoS = 0, Wi-Fi Ch = 11 | Completed|
| 100 | Baseline (Plaintext) | 42 | Payload = 16B, QoS = 0, Wi-Fi Ch = 11 | Completed |
| 101 | Intervensi (AES-128)| 42 | Payload = 16B, QoS = 0, Wi-Fi Ch = 11, Key Length = 128-bit | Completed |
| 200 | Intervensi (AES-128) | 42 | Payload = 16B, QoS = 0, Wi-Fi Ch = 11, Key Length = 128-bit | Completed |
|  | | | | |

**Total skenario:** 2 (Plaintext vs AES-128)
**Run per skenario:** 100 kali pengiriman paket data
**Total run keseluruhan:** 200 rangkaian data hantar

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | TRIAL-087 |
| Timestamp | 2026-06-21T09:22:15.102Z |
| Group ID | 0 (untuk Baseline/Plaintext) atau 1 (untuk Intervensi/AES-128) |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 (Digunakan sebagai static Initialization Vector / IV pada blok cipher) |
| Code version | firmware-v1.0.4-commit-8ab43e |
| RSSI Level | -60 dBm (Indikator kekuatan sinyal Wi-Fi lokal) |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Time_Sent | unsigned long | 0 - 4.294.967.295 |
| Time_ACK | unsigned long| 0 - 4.294.967.295|
| Round Trip Time (RTT) | float | 1.0 ms - 1000.0 ms |

**Format output:** [ x ] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Perangkat NodeMCU mengalami Hardware Watchdog Timer (WDT) Reset di tengah jalan akibat kegagalan alokasi memori dinamis (pointer leak) saat fungsi enkripsi diulang terus menerus. | Dokumentasikan pesan kesalahan (stack trace) dari serial monitor, lakukan pembersihan heap memory pada kode program, lakukan hard reset hardware, lalu ulangi pengerjaan dari baris data ke-1 untuk skenario tersebut. |
| Hasil ekstrem | Durasi RTT melompat secara acak hingga 2450 ms pada satu paket data (rata-rata normal berada di kisaran 15 - 20 ms) | Jangan dihapus secara sepihak. Periksa log pada broker Mosquitto. Jika lonjakan terjadi akibat intervensi retransmisi paket Wi-Fi pada lapisan MAC (packet drop), tetap simpan data tersebut dan beri label penanda INTERFERENCE_ANOMALY untuk dijelaskan sebagai variabilitas alami pada bab analisis. |
| Waktu eksekusi anomali | Nilai penanda waktu micros() mengalami kondisi batas overflow (kembali ke angka 0 karena melewati batas tampung variabel 32-bit setelah menyala aktif kurang lebih 71 menit). | Terapkan logika penanganan overflow pada script parser Python host: jika Time_ACK < Time_Sent, maka rumus diubah menjadi: Delta T = ((4.294.967.295 Time_Sent) + Time_ACK) / 1000.0 Catat kejadian konversi ini ke log metadata.|
| Inkonsistensi dengan run lain | Nilai deviasi standar (standard deviation) pada pengujian kelompok AES-128 bernilai lebih kecil secara tidak wajar dibandingkan kelompok Plaintext. | Lakukan pengecekan fisik terhadap suhu operasional chip NodeMCU ESP8266 dan pastikan voltase catu daya dari port USB PC host konstan berada di angka 4.9V - 5.0V. Lakukan re-run skenario jika terbukti ada ketimpangan daya listrik selama eksekusi. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya, pada pengerjaan proyek sistem tertanam (embedded system) fungsional sebelumnya, saya sering kali hanya menguji pengiriman data kendali satu kali saja. Jika perintah "Lampu ON" dikirim sekali dan relay berbunyi klik, maka sistem langsung saya klaim berhasil dan responsif. Risikonya adalah angka performa tersebut sangat bias dan tidak valid secara ilmiah, karena mengabaikan faktor fluktuasi stabilitas gelombang radio, beban komputasi mikroprosesor, dan potensi penumpukan memori (memory overflow) yang baru muncul setelah ratusan kali iterasi eksekusi.
**Yang akan dilakukan berbeda:**
> Untuk riset komparatif keamanan siber ini, saya menerapkan prinsip Multiple Runs dengan mengirimkan 100 paket data per skenario secara berkelanjutan. Pendekatan pengumpulan data dalam jumlah sampel besar ini mengubah total tingkat kepercayaan riset. Reviewer dan pembaca tidak hanya disajikan satu angka mutlak, melainkan distribusi data yang valid berupa nilai rata-rata (Mean), variabilitas deviasi standar, serta visualisasi batas galat (error bar), sehingga pembuktian overhead penalti latensi akibat enkripsi AES-128 dapat dipertanggungjawabkan secara matematis melalui uji statistik t-test.

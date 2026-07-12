# Arsitektur dan Skema Sistem — Evaluasi Komparatif Express.js vs Gin

## 1. Diagram Arsitektur Komponen (Gateway, Redis, PostgreSQL)

Pada sistem IoT, API Gateway diwakili oleh sebuah IoT Gateway/Broker MQTT Proxy, Redis digunakan untuk mencatat state intervensi serta data log latensi cepat, sedangkan PostgreSQL menyimpan riwayat benchmark RTT utuh.

```
+-------------------------------------------------------------+
       |             TRAFIK PERANGKAT (NodeMCU ESP8266 / MQTT)        |
       +-------------------------------------------------------------+
                                      |
                                      v
                        +---------------------------+
                        |   Mosquitto MQTT Broker   |
                        |   & IoT Gateway Proxy     |
                        +---------------------------+
                          /                       \
        (1. Ambil Kebijakan / \                       / (3. Penyimpanan Log
           State Enkripsi)     \                     /      Kuantitatif RTT)
                                v                     v
                +-----------------+       +-----------------------+
                |   Redis Cache   |       | PostgreSQL Database   |
                | (In-Memory K/V) |       |  (Persistent Store)   |
                +-----------------+       +-----------------------+
```

## 2. Mekanisme Interaksi Komponen

### 2.1. IoT Gateway / Broker MQTT
Menerima pesan publish instan berisi payload kendali sakelar pintar (baik Plaintext maupun Ciphertext AES-128) dari NodeMCU.

### 2.2. Redis Cache
Menyimpan flag state status enkripsi perangkat saat ini secara instan, mengelola rate-limiting paket untuk mencegah flooding dari node rusak, serta menjadi buffer log mikrodetik sementara.

### 2.3. PostgreSQL Engine
Menyimpan data 200 sampel eksperimen secara utuh untuk keperluan agregasi data statistik, pemrosesan rumus Welch's t-test, dan analisis pencilan jangka panjang.

## 3. Diagram Alur Resolusi Kunci (Mitigasi Paket Flooding & Validasi Enkripsi)

Diagram alur ini menggambarkan bagaimana sistem memproses setiap paket data sensor/sakelar yang dikirim oleh NodeMCU untuk memitigasi flooding akibat kegagalan transmisi (MAC layer retransmission).

[ Paket MQTT Masuk dari NodeMCU ESP8266 ]
                                    |
                                    v
               +-------------------------------------------+
               | Cek Rate-Limit Koneksi Node di Redis      |
               +-------------------------------------------+
                                    |
                           (Apakah Melebihi?)
                           /                \
                     [Ya] /                  \ [Tidak]
                         v                    v
             +------------------------+   +----------------------------------+
             | Drop Paket (Muted/Timeout) |   | Cek Status Validasi Struktur Data|
             +------------------------+   +----------------------------------+
                                                   |
                                            (Apakah Malformed?)
                                            /                \
                                      [Ya] /                  \ [Tidak]
                                          v                    v
                              +--------------------+   +--------------------------------+
                              | Masuk ke Redis     |   | Cek Tipe Payload (Plain/Cipher)|
                              | Negative Cache     |   +--------------------------------+
                              +--------------------+                    |
                                                                        v
                                                            (Apakah AES-128 Aktif?)
                                                            /                     \
                                                      [Ya] /                       \ [Tidak]
                                                          v                         v
                                              +-----------------------+  +----------------------+
                                              | Dekripsi dengan Kunci  |  | Langsung Eksekusi    |
                                              | AES di Gateway Layer  |  | Perintah Sakelar     |
                                              +-----------------------+  +----------------------+
                                                          |                         |
                                                          +------------+------------+
                                                                       |
                                                                       v
                                                           [ Catat T1 & T2 di Redis ]
                                                                       |
                                                                       v
                                                           [ Simpan Permanen ke PG ]

### 3.1. Skema Database PostgreSQL
Skema basis data relasional ini digunakan untuk menampung riwayat data Round Trip Time (RTT) kuantitatif dari 40 replikasi hingga 200 total sampel guna mendeteksi signifikansi statistik.

-- Tabel untuk menyimpan riwayat performa uji coba RTT secara presisi
CREATE TABLE rtt_experiments (
    id BIGSERIAL PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,            -- Identitas NodeMCU
    scenario_type VARCHAR(20) NOT NULL,        -- 'plaintext' atau 'aes128'
    t1_timestamp BIGINT NOT NULL,              -- Waktu kirim (dalam mikrodetik)
    t2_timestamp BIGINT NOT NULL,              -- Waktu terima ACK (dalam mikrodetik)
    rtt_latency_ms NUMERIC(8,3) NOT NULL,       -- Hasil (t2 - t1) / 1000
    is_outlier BOOLEAN DEFAULT FALSE,          -- Penanda paket anomali (misal: > 40 ms)
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tabel untuk mencatat kegagalan paket (2 paket drop/timeout)
CREATE TABLE packet_failures (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,
    error_reason TEXT NOT NULL,                 -- 'Timeout', 'MAC Retransmission', 'RF Interference'
    occurred_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexing untuk kebutuhan kalkulasi statistik Welch's t-test
CREATE INDEX idx_scenario_rtt ON rtt_experiments(scenario_type, rtt_latency_ms);

## 4. Skema Penyimpanan Redis (Key-Value Design untuk IoT)
Penerapan cache tingkat tinggi pada Redis disesuaikan untuk melacak kondisi real-time perangkat nirkabel.

### 4.1. Positive Cache (Menyimpan State Node Valid)

```
Format Key: iot:pos:node:<device_id>:config

Value: {"encryption": "AES-128", "key_version": "v1", "status": "authorized"}

TTL (Time to Live): 86400 detik (24 Jam).

Tujuan: Mempercepat verifikasi apakah NodeMCU yang terhubung wajib mengirimkan data terenkripsi atau teks biasa tanpa perlu membebani basis data relasional.
```

### 4.2. Negative Cache (Meredam Node Rusak / Ancaman Sniffing)

```
Format Key: iot:neg:node:<device_id>:malformed

Value: {"fail_count": 5, "last_error": "Decryption Failed"}

TTL (Time to Live): 300 detik (5 Menit).

Tujuan: Jika sebuah node IoT mengirimkan data terenkripsi yang salah (kunci tidak cocok/serangan injeksi paket), broker langsung memblokir komunikasi node tersebut di lapisan cache memory selama 5 menit.
```

### 4.3. Rate Limit Counter (Sliding Window untuk Wi-Fi Flooding)

```
Format Key: iot:rl:node:<device_id>:burst

Value: Integer (Counter frekuensi kirim pesan).

TTL (Time to Live): 10 detik.

Tujuan: Mencegah terjadinya flooding jaringan radio 2.4 GHz akibat malfungsi perulangan (infinite loop) pada kode program NodeMCU, menjaga batas kirim maksimal 10 messages per 10 detik.
```

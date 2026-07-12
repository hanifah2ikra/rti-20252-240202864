# Arsitektur dan Skema Sistem — Evaluasi Komparatif Express.js vs Gin

## 1. Gambaran Umum Arsitektur

Sistem penelitian ini terdiri dari empat komponen utama yang berjalan dalam lingkungan Docker Compose yang terisolasi:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Docker Compose Network                        │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐  │
│  │   Express.js │    │      Gin     │    │    PostgreSQL 15     │  │
│  │   (Node.js)  │    │   (Go)       │    │   (port 5432)        │  │
│  │   :3000      │    │   :8080      │    │                      │  │
│  └──────┬───────┘    └──────┬───────┘    └──────────┬───────────┘  │
│         │                    │                      │                │
│         └────────────────────┼──────────────────────┘                │
│                              │                                       │
│                    ┌─────────▼──────────┐                            │
│                    │       Redis        │  (opsional, untuk caching) │
│                    │       :6379        │                            │
│                    └───────────────────┘                            │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Komponen Aplikasi

### 2.1. Express.js API

- **Framework**: Express 4.x dengan TypeScript
- **Runtime**: Node.js 20.x
- **Database**: PostgreSQL via Prisma ORM
- **Port**: 3000
- **Endpoints**:
  - `GET /api/simple` — handler sederhana tanpa database
  - `GET /api/users/:id` — single database query
  - `GET /api/users/stats` — complex database query (agregasi)
  - `GET /health` — health check

### 2.2. Gin API

- **Framework**: Gin (Go)
- **Runtime**: Go 1.24.x
- **Database**: PostgreSQL via GORM
- **Port**: 8080
- **Endpoints**: sama persis dengan Express untuk memastikan perbandingan valid
- **Konfigurasi**: `gin.SetMode(gin.ReleaseMode)` untuk menghilangkan overhead debug

## 3. Skema Database

Kedua aplikasi menggunakan database PostgreSQL yang sama dengan skema berikut:

### 3.1. Tabel `users`

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 3.2. Tabel `orders`

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    amount DECIMAL(10,2),
    status VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 3.3. Query Patterns

| Skenario | Query yang Dijalankan |
|---|---|
| `baseline` | Tidak ada query — hanya `res.json({ ok: true })` |
| `db_single` | `SELECT * FROM users WHERE id = $1` |
| `db_complex` | `SELECT u.id, u.name, COUNT(o.id) as order_count, SUM(o.amount) as total_amount FROM users u LEFT JOIN orders o ON u.id = o.user_id GROUP BY u.id, u.name ORDER BY order_count DESC LIMIT 100` |

## 4. Alur Request

### 4.1. Baseline (tanpa database)

```
Client → API Gateway (k6) → Express/Gin → Handler → Response JSON (tanpa DB)
```

### 4.2. Single Query

```
Client → API Gateway (k6) → Express/Gin → Prisma/GORM → PostgreSQL → Result → Response JSON
```

### 4.3. Complex Query

```
Client → API Gateway (k6) → Express/Gin → Prisma/GORM → PostgreSQL (JOIN + GROUP BY + aggregasi) → Result → Response JSON
```

## 5. Konfigurasi Lingkungan

### 5.1. Docker Compose

```yaml
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: benchmark
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5433:5432"
    volumes:
      - ./seed.sql:/docker-entrypoint-initdb.d/seed.sql

  express-api:
    build: ./apps/express-api
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://user:password@postgres:5432/benchmark
    depends_on:
      postgres:
        condition: service_healthy

  gin-api:
    build: ./apps/gin-api
    ports:
      - "8080:8080"
    environment:
      DATABASE_URL: postgresql://user:password@postgres:5432/benchmark
    depends_on:
      postgres:
        condition: service_healthy
```

### 5.2. Database Seeding

- **Users**: 10.000 baris data
- **Orders**: 50.000 baris data (relasi ke users)
- Data di-generate via SQL seed script sebelum pengujian

## 6. Proses Pengujian

### 6.1. Workflow Eksperimen

```
1. Setup: docker compose up -d
2. Seed database: docker exec -i postgres psql -U user -d benchmark -f /docker-entrypoint-initdb.d/seed.sql
3. Warm-up: Jalankan kedua API selama 30 detik
4. Baseline test: k6 run --vus 50 --duration 60s legitimate.js (target Express:3000 atau Gin:8080)
5. DB Single test: k6 run --vus 50 --duration 60s db_single.js
6. DB Complex test: k6 run --vus 50 --duration 60s db_complex.js
7. Repeat: Ulangi 40 replikasi per kombinasi
8. Collect: Simpan k6-summary.json per run ke 04-data/
```

### 6.2. Metrik yang Dikumpulkan

| Metrik | Sumber | Deskripsi |
|---|---|---|
| `http_req_duration` | k6 | Latensi per request (avg, min, max, p90, p95, p99) |
| `http_reqs` | k6 | Total request yang berhasil |
| `http_req_failed` | k6 | Request yang gagal |
| `iteration_duration` | k6 | Durasi seluruh iterasi script |

## 7. Variabel Eksperimen

### 7.1. Variabel Independen

- **Framework**: Express.js (Node.js), Gin (Go)
- **Skenario**: baseline, db_single, db_complex

### 7.2. Variabel Dependen

- Latensi request (ms)
- Distribusi latency (mean, median, persentil)
- Jumlah outlier
- Error rate

### 7.3. Kontrol Variabel

- Sumber daya Docker (CPU, RAM) — sama untuk kedua framework
- Dataset database — identik untuk kedua framework
- Endpoint implementasi — sama persis
- Jaringan — dalam satu Docker network
- Versi framework — terkunci (Express 4.x, Gin latest stable)

## 8. Diagram Arsitektur (Mermaid)

```mermaid
graph TB
    subgraph "Host Machine"
        K6[k6 Load Generator]
    end

    subgraph "Docker Compose"
        subgraph "Application Layer"
            EXPRESS[Express.js API<br/>:3000]
            GIN[Gin API<br/>:8080]
        end

        subgraph "Data Layer"
            PG[(PostgreSQL 15<br/>:5433)]
        end
    end

    K6 -->|HTTP Request| EXPRESS
    K6 -->|HTTP Request| GIN
    EXPRESS -->|Query| PG
    GIN -->|Query| PG

    style EXPRESS fill:#e1f5fe
    style GIN fill:#e8f5e9
    style PG fill:#fff3e0
```

## 9. Expected Outcomes (Hipotesis)

1. **Baseline**: Gin akan menunjukkan latency median ~3–5 ms, sedangkan Express ~50–100 ms. Rasio performa diharapkan ~15–30x.
2. **DB Single**: Perbedaan akan menyempit karena latency database mendominasi. Rasio diharapkan ~5–10x.
3. **DB Complex**: Gin tetap lebih cepat, namun dengan rasio yang lebih kecil (~3–5x) karena agregasi database menjadi bottleneck utama.
4. **Distribusi**: Express akan menunjukkan lebih banyak outlier karena event loop blockage, sedangkan Gin akan menunjukkan distribusi yang lebih konsisten.

## 10. Keterbatasan

1. Hanya satu representative workload JSON REST API diuji.
2. Docker Desktop pada Windows memperkenalkan overhead virtualization.
3. Versi tertentu dari setiap framework digunakan; upgrade major dapat mengubah perbandingan.
4. Sumber daya server (CPU, RAM, I/O) tidak di-isolate secara ketat antar run.

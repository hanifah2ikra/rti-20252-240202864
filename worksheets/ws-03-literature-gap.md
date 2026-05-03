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

Topik      : Smart Home Lampu Otomatis Berbasis IoT (Sensor PIR & LDR)
Database   : Google Scholar
Query      : IoT Smart Home PIR LDR Lampu Otomatis, Smart Lighting IoT PIR LDR energy efficiency
Tahun      : 2019-2024
Hasil awal : 50 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|Rahmat et al.|2021 | IoT+PIR sensor |Data Gerakan |Lampu Otomatis berjalan baik |Tidak mempertimbangkan cahaya|
|Sari et al.|2020 |LDR-based control |Intensitas cahaya |Hemat listrik 20% |Tidak deteksi manusia |
|Putra et al.|2022 |PIR + LDR |Data sensor real-time|Sistem lebih akurat |Delay respon masih tinggi |
|Chen et al.|2023 |Smart lighting IoT |Dataset smart home |Efisiensi meningkat|Tidak diuji di rumah nyata |
|Kumar et al.|2021 |MQTT smart home|Data IoT |Sistem stabil|Latency komunikasi tinggi|

Pola yang ditemukan:
  Metode dominan     : Sensor PIR dan LDR berbasis IoT
  Dataset umum       : Data sensor real-time skala kecil
  Limitasi berulang  : Delay respon, akurasi sensor belum optimal, pengujian terbatas

GAP IDENTIFICATION

Gap 1: [Jenis : Performance Gap
  Deskripsi    : Akurasi deteksi dan waktu respon sistem masih belum optimal
  Bukti        : Beberapa studi menunjukkan delay tinggi dan kesalahan deteksi sensor
  Signifikansi : Berpengaruh langsung terhadap kenyamanan dan efisiensi energi
Gap 2: [Jenis: Context Gap]
  Deskripsi    : Sistem belum banyak diuji pada kondisi rumah nyata dengan variasi cahaya
  Bukti        : Banyak penelitian hanya menggunakan simulasi atau skala kecil
  Signifikansi : Hasil penelitian belum tentu berlaku di kondisi nyata

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|PIR-based smart lighting|PIR-based smart lighting|Banyak digunakan pada smart home|Rahman et al., 2021|
|LDR-based lighting control |Mengatur lampu berdasarkan cahaya |Metode umum untuk efisiensi energi | Sari et al., 2020|
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Smart Home Lampu Otomatis IoT
**Query pencarian:** "smart home IoT PIR LDR lighting"
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
| 1 | Rahman et al. | 2021 | PIR sensor | Data gerakan| Lampu otomatis| Tidak terdeteksi cahaya |
| 2 | Sari et al.|2020 |LDR sensor |Intensitas cahaya |Hemat energi |Tidak deteksi manusia |
| 3 |Putra et al. |2022 |PIR+LDR |Sensor real-time |Lebih akurat |Delay tinggi |
| 4 |chen et al.|2023|IoT Smart Lighting |Data smart home |Efisien |Tidak Real-world |
| 5 |Kumar et al. |2021 |MQTT IoT |Data komunikasi |Stabil |Latency tinggi |

**Pola yang terlihat — Metode dominan:** Sensor PIR dan LDR
**Limitasi yang berulang:** Delay sistem dan akurasi sensor

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ * ] Ya / [ ] Tidak | Waktu respon sistem masih lambat dan akurasi deteksi belum optimal |
| Method Gap | [ ] Ya / [ ] Tidak | |
| Data Gap | [ ] Ya / [ ] Tidak | |
| Context Gap | [ * ] Ya / [ ] Tidak | Sistem belum diuji secara luas pada kondisi rumah nyata|

**Gap utama yang dipilih:** Performance Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena kinerja sistem seperti akurasi dan waktu respon sangat mempengaruhi keberhasilan smart home dalam menghemat energi dan kenyamanan pengguna. Jika sistem lambat atau salah deteksi, maka tujuan otomatisasi tidak tercapai.
---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | PIR-based system| Deteksi gerakan langsung | Digunakan di banyak penelitian | Tidak | Rahmat et al., 2021 |
| 2 |LDR-based system |Deteksi cahaya |Metode umum smart lighting |Tidak |Sari et al., 2020 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [*] Tidak
> Justifikasi: Baseline dipilih dari metode yang umum digunakan dan relevan dengan masalah, bukan metode yang sengaja dilemahkan.
---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim "belum ada yang meneliti ini" seringkali tidak valid jika tidak didukung oleh pencarian literatur yang sistematis. Sedangkan research gap yang valid harus didasarkan pada bukti dari beberapa penelitian yang menunjukkan adanya keterbatasan atau kekurangan tertentu. Cara membuktikannya adalah dengan melakukan pencarian menggunakan database ilmiah, membandingkan beberapa paper, dan menunjukkan pola limitasi yang konsisten sehingga gap yang diambil benar-benar nyata dan dapat dipertanggungjawabkan secara ilmiah.
> ___________________________________________________

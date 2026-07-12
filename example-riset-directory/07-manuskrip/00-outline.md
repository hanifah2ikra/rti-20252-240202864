# Outline Naskah Jurnal

## Judul
Performance Evaluation of Express.js vs Gin Framework for REST API with Database Query Complexity Workloads

## Penulis
[Placeholder: Nama Penulis, Afiliasi, Email]

## Struktur & Panjang Target
- Abstrak: ~200 kata (ID + EN)
- §1 Pendahuluan: ~1.500 kata
- §2 Tinjauan Pustaka: ~2.000 kata
- §3 Metodologi: ~2.000 kata
- §4 Hasil & Analisis: ~2.500 kata
- §5 Kesimpulan: ~800 kata
- Daftar Pustaka: minimal 15 referensi IEEE

## Peta Sumber Per Bagian

| Bagian | Sumber utama | Referensi silang |
|---|---|---|
| Abstrak | Data 04-data/, 06-output/tables/, 06-output/figures/ | §4 tabel hasil |
| Pendahuluan | README.md, 05-kode/ | §3 metodologi |
| Tinjauan Pustaka | Literatur umum benchmark web framework, Node.js vs Go | §4 hasil |
| Metodologi | 05-kode/ (Express & Gin source), 06-output/README.md | §4 tabel/figur |
| Hasil & Analisis | 06-output/tables/, 06-output/figures/ | §3 metodologi |
| Kesimpulan | §4 temuan | Semua bagian |

## Daftar Klaim Kunci (harus konsisten)

1. Gin (Go) menghasilkan latency median **4,0 ms** pada baseline dibanding Express **52,0 ms** — **~15x lebih cepat**.
2. Pada skenario database single query, Gin menghasilkan median **7,3 ms** vs Express **55,0 ms** — **~7,5x lebih cepat**.
3. Pada skenario database complex query, Gin menghasilkan median **7,3 ms** vs Express **35,0 ms** — **~4,8x lebih cepat**.
4. Semakin kompleks beban database, perbedaan performa kedua framework menyempit, namun Gin tetap unggul secara signifikan di semua skenario.
5. Distribusi latency Express menunjukkan outlier yang lebih ekstrem (hingga 22 detik pada baseline) dibanding Gin (maks 44 ms), mengindikasikan lebih banyak variabilitas pada runtime Node.js.

## Referensi Gambar & Tabel

| Label | File | Bagian |
|---|---|---|
| Fig. 1 | [../06-output/figures/baseline_comparison.png](../06-output/figures/baseline_comparison.png) | §4 Hasil |
| Fig. 2 | [../06-output/figures/db_single_comparison.png](../06-output/figures/db_single_comparison.png) | §4 Hasil |
| Fig. 3 | [../06-output/figures/db_complex_comparison.png](../06-output/figures/db_complex_comparison.png) | §4 Hasil |
| Fig. 4 | [../06-output/figures/benchmark_comparison.png](../06-output/figures/benchmark_comparison.png) | §4 Hasil |
| Tab. 1 | [../06-output/tables/descriptive_stats.csv](../06-output/tables/descriptive_stats.csv) | §4 Hasil |
| Tab. 2 | [../06-output/tables/speedup_ratio.csv](../06-output/tables/speedup_ratio.csv) | §4 Hasil |
| Tab. 3 | [../06-output/tables/resource_usage.csv](../06-output/tables/resource_usage.csv) | §4 Hasil |

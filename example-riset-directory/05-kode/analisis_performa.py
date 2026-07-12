import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Definisikan Jalur Direktori Berkas
DATA_DIR = "../05-data/"
OUTPUT_DIR = "../06-output/"

# Pastikan folder output sudah tersedia
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=== MEMULAI PROSES PEMBERSIHAN & ANALISIS DATA IOT ===")

# 2. Muat Data Mentah CSV
df_plain_raw = pd.read_csv(os.path.join(DATA_DIR, "plaintext_legitimate.csv"))
df_aes_raw = pd.read_csv(os.path.join(DATA_DIR, "aes128_attack.csv"))

# 3. Penanganan Data Hilang (Listwise Deletion untuk status TIMEOUT)
df_plain = df_plain_raw[df_plain_raw['status'] == 'SUCCESS'].copy()
df_aes = df_aes_raw[df_aes_raw['status'] == 'SUCCESS'].copy()

# Konversi metrik dari Mikrodetik (micros) ke Milidetik (ms)
df_plain['rtt_ms'] = df_plain['rtt_latency_micros'] / 1000.0
df_aes['rtt_ms'] = df_aes['rtt_latency_micros'] / 1000.0

print(f"Data Plaintext Berhasil Dimuat: {len(df_plain)} sampel (0 drop)")
print(f"Data AES-128 Berhasil Dimuat: {len(df_aes)} sampel (2 drop dieliminasi)")

# 4. Kalkulasi Statistik Deskriptif
stats_plain = {
    "Mean (ms)": round(df_plain['rtt_ms'].mean(), 2),
    "Median (ms)": round(df_plain['rtt_ms'].median(), 2),
    "Min (ms)": round(df_plain['rtt_ms'].min(), 2),
    "Max (ms)": round(df_plain['rtt_ms'].max(), 2),
    "Sampel Valid": len(df_plain)
}

stats_aes = {
    "Mean (ms)": round(df_aes['rtt_ms'].mean(), 2),
    "Median (ms)": round(df_aes['rtt_ms'].median(), 2),
    "Min (ms)": round(df_aes['rtt_ms'].min(), 2),
    "Max (ms)": round(df_aes['rtt_ms'].max(), 2),
    "Sampel Valid": len(df_aes)
}

# Tampilkan Hasil Deskriptif di Console
print("\n[Statistik Deskriptif - Plaintext Baseline]")
print(json.dumps(stats_plain, indent=2))
print("\n[Statistik Deskriptif - AES-128 Intervensi]")
print(json.dumps(stats_aes, indent=2))

# 5. Uji Signifikansi Inferensial (Welch's t-test)
# Menggunakan Welch's t-test karena jumlah sampel berbeda (100 vs 98) dan variansi tidak sama
t_stat, p_val = stats.ttest_ind(df_plain['rtt_ms'], df_aes['rtt_ms'], equal_var=False)

print("\n=== HASIL UJI INFERENSIAL (WELCH'S T-TEST) ===")
print(f"t-Statistic : {round(t_stat, 4)}")
print(f"p-Value     : {p_val}")
if p_val < 0.05:
    print("Kesimpulan  : Signifikan! Penambahan Enkripsi AES-128 mempengaruhi Latensi RTT secara Nyata.")
else:
    print("Kesimpulan  : Tidak Signifikan! Perbedaan RTT berada dalam batas toleransi wajar.")

# 6. Pembuatan Grafik Komparasi (Boxplot) untuk Bab 4
plt.figure(figsize=(8, 6))
plt.boxplot([df_plain['rtt_ms'], df_aes['rtt_ms']], labels=['Plaintext (Baseline)', 'AES-128 (Intervensi)'])
plt.title('Evaluasi Komparatif Latensi RTT Perangkat Smart Home IoT')
plt.ylabel('Round Trip Time / Latensi (ms)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Simpan Grafik Secara Bersih ke Folder Output
chart_path = os.path.join(OUTPUT_DIR, "komparasi_latensi_boxplot.png")
plt.savefig(chart_path, dpi=300)
plt.close()

print(f"\n[SUKSES] Grafik boxplot performa telah diexport ke: {chart_path}")
print("=== PROSES SELESAI ===")
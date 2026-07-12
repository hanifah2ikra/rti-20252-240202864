# Proposal Penelitian: Analisis Performa dan Keamanan Transmisi Data Nirkabel Smart Home menggunakan Enkripsi AES-128 pada Mikrokontroler NodeMCU ESP8266

## 1. Latar Belakang

Perkembangan teknologi smart home berbasis Internet of Things (IoT) telah mengubah cara manusia berinteraksi dengan lingkungan tempat tinggalnya melalui sistem otomatisasi nirkabel. Namun, pesatnya adopsi perangkat pintar ini sering kali tidak diimbangi dengan kesadaran keamanan siber pada level firmware. Mayoritas data instruksi kendali nirkabel (seperti perintah untuk mematikan atau menghidupkan relay sakelar pintar) saat ini masih dikirim dalam format teks biasa (plaintext). Kondisi ini membuka celah keamanan yang sangat rentan terhadap serangan penyingkapan informasi (sniffing), modifikasi data, hingga pembajakan sesi kendali oleh pihak ketiga.

Di sisi lain, para pengembang perangkat pintar dan praktisi IoT kerap kali menghindari implementasi algoritma kriptografi standar industri, seperti AES-128. Keengganan ini didasari oleh asumsi subjektif bahwa operasi matematika enkripsi simetris akan memuji siklus kerja prosesor kelas rendah secara berlebihan. Ketakutan akan munculnya penalti latensi (network delay) yang tinggi dianggap dapat merusak kenyamanan pengguna dalam mengendalikan perangkat rumah tangga secara real-time. Oleh karena itu, diperlukan sebuah pengujian empiris yang rigor di laboratorium untuk mengukur seberapa besar dampak matematis algoritma enkripsi terhadap performa hantar paket pada arsitektur mikrokontroler berdaya rendah.

## 2. Rumusan Masalah

Berdasarkan latar belakang di atas, rumusan masalah penelitian ini adalah:

1. Apakah penerapan enkripsi simetris AES-128 pada firmware NodeMCU ESP8266 meningkatkan nilai latensi hantar paket (Round Trip Time) secara signifikan?
2. Berapa penalti waktu komputasi riil (dalam milidetik) yang dihasilkan oleh enkripsi AES-128 pada arsitektur CPU Xtensa LX106 80 MHz?
3. Apakah peningkatan latensi akibat enkripsi tersebut mengganggu aspek kenyamanan dan batas responsivitas kendali operasional smart home dalam koridor waktu nyata (real-time)?

## 3. Tujuan Penelitian

Tujuan utama dari penelitian ini adalah mengevaluasi secara kuantitatif dampak penambahan fitur keamanan AES-128 terhadap performa transmisi data nirkabel IoT. Secara spesifik:

1. Mengimplementasikan dua varian firmware isomorfik pada mikrokontroler NodeMCU ESP8266: satu menggunakan mode tanpa pengamanan (Plaintext) dan satu menggunakan enkripsi simetris AES-128.
2. Mengukur metrik Round Trip Time (RTT) secara tertanam (embedded microsecond logging) memanfaatkan fungsi lokal micros() dalam lingkungan laboratorium terisolasi.
3. Membuktikan signifikansi perbedaan rata-rata latensi kedua kelompok operasional menggunakan uji statistik komparatif parametrik Welch's t-test.
4. Memetakan variabilitas distribusi latensi, termasuk mengidentifikasi pencilan (outlier) serta melakukan analisis kegagalan (failure analysis) pada lapisan fisik nirkabel.

## 4. urgensi

Penelitian ini memiliki urgensi tinggi untuk mematahkan hambatan psikologis dan paradigma keliru di kalangan pengembang IoT mengenai implementasi pengamanan siber. Dengan menyajikan data kuantitatif yang valid dari 200 sampel eksperimen, penelitian ini memberikan kepastian empiris apakah pengamanan enkripsi AES-128 bersifat ramah sumber daya atau tidak untuk mikrokontroler kelas rendah. Hasil evaluasi ini dapat dijadikan acuan arsitektural yang kuat bagi industri maupun akademisi dalam merancang sistem smart home yang tidak hanya responsif, tetapi juga tangguh terhadap ancaman intersepsi data.

## 5. Metodologi (Ringkasan)

### 5.1. Skenario Eksperimen

| Skenario | Kondisi Transmisi | Deskripsi |
|---|---|---|
| `Baseline` | `Plaintext (n=100)` | Pengiriman data instruksi kendali 16 Byte via MQTT dalam bentuk teks biasa tanpa enkripsi. |
| `Intervensi` | `AES-128 Enabled (n=98)` | Pengiriman data instruksi kendali 16 Byte yang telah dienkripsi menggunakan algoritma AES-128 sebelum dikirim ke broker. |

Dari total 200 sampel data awal, terdapat 2 paket drop (timeout) pada kelompok intervensi akibat interferensi transien dan dieliminasi menggunakan metode listwise deletion.

### 5.2. Konfigurasi Pengujian

- **Perangkat Keras**: Mikrokontroler NodeMCU ESP8266 (CPU Xtensa LX106 80 MHz), Router Wi-Fi 2.4 GHz, Relay Sakelar Pintar.
- **Replikasi**: 100 replikasi per kondisi operasional untuk menjamin pemenuhan asumsi sebaran statistik.
- **Protokol Jaringan**: Message Queuing Telemetry Transport (MQTT) melalui jaringan lokal (LAN) dengan jarak konstan 5 meter dan RSSI dijaga pada -60 dBm.
- **Metode Pencatatangan**: Timestamping presisi tinggi berbasis mikrodetik menggunakan fungsi bawan perangkat lunak micros() tepat sebelum paket dikirim dan sesaat setelah konfirmasi balasan (acknowledgement) diterima.

### 5.3. Metrik Evaluasi

1. **Rata-rata (Mean RTT)** — Indikator utama kecepatan hantar paket (Plaintext mencatatkan 15,24 ms vs AES-128 mencatatkan 18,42 ms).
2. **Uji Signifikansi (Welch's t-test)** — Membuktikan signifikansi penalti latensi komputasi sebesar 3,18 ms (p < 0,001).
3. **Ukuran Efek (Cohen's d)** — Mengukur kekuatan efek intervensi keamanan (mencapai nilai ekstrem 3,65).
4. **Analisis Pencilan (Outlier Analysis)** — Mengidentifikasi data ekstrim maksimum (45,12 ms) sebagai akibat dari interferensi frekuensi radio 2.4 GHz (MAC layer retransmission).

## 6. Daftar Pustaka (Preliminary)

[1] Hadiatullah, D. R., Farosanti, L., & Rizky, M. C. (2025). Optimalisasi Smart Home Berbasis IoT dengan NodeMCU ESP8266 untuk Efisiensi Energi. Jurnal Fasilkom, 15(2), 368-375.

[2] Hamka, M., Purnama, I., & Bangun, B. (2025). Lampu Pintar: Mengendalikan Pencahayaan Jarak Jauh dengan ESP32 dan Blynk. Prosiding Seminar Nasional Teknologi Komputer dan Sains (SAINTEKS), 3(1), 345-354.

[3] Pramono, A., & Muntahar, A. A. M. (2024). Implementasi Keamanan Rumah Pintar Berbasis Android Dengan Teknologi IoT Dan NodeMCU ESP8266. Jurnal Resistor (Rekayasa Sistem Komputer), 7(3).

[4] Agma, A. R. (2025). Implementasi Internet of Things (IoT) pada Sistem Smart Home. Jurnal Informatika Indonesia, 1(1), 15-21.

[5] Ferella, Paembonan, S., & Abduh, H. (2025). Prototype Sistem Kontrol Rumah Pintar Menggunakan Kamera Berbasis Internet of Things (IoT). JITET (Jurnal Informatika dan Teknik Elektro Terapan), 13(1).
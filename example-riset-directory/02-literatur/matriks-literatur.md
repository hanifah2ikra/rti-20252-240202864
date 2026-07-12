# Matriks Literatur

## Topik Penelitian
1. Analisis Performa dan Keamanan Transmisi Data Nirkabel Smart Home menggunakan Enkripsi AES-128 pada Mikrokontroler NodeMCU ESP8266

## Referensi dari 5 Paper di Folder `../paper/`

| # | Referensi Paper | Metodologi | Hasil |
|---|---|---|---|
| [1] | hadiatullah2025optimalisasi | Optimalisasi efisiensi energi pada ekosistem smart home menggunakan NodeMCU ESP8266 melalui pemutusan daya otomatis pada perangkat pasif. | Berhasil menghemat konsumsi daya listrik rumah tangga hingga 18,5% menggunakan skenario penjadwalan berbasis IoT.|
| [2] | hamka2025lampu | Implementasi kendali lampu pintar jarak jauh menggunakan ESP32 yang diintegrasikan dengan platform Blynk via Wi-Fi. | Sistem mampu merespons instruksi sakelar dari aplikasi Blynk dengan tingkat keberhasilan transmisi mencapai 98%. |
| [3] | pramono2024implementasi | Rancang bangun sistem keamanan fisik rumah pintar (kunci pintu/selot) berbasis Android memanfaatkan konektivitas Wi-Fi lokal NodeMCU ESP8266. | Integrasi sensor magnetik dan solenoid dapat bekerja secara real-time ketika dipicu oleh aplikasi Android di jaringan yang sama. |
| [4] | agma2025implementasi | Analisis dasar penerapan arsitektur Internet of Things pada topologi smart home berskala luas untuk kendali perangkat multi-ruangan. | Topologi mesh network lokal mampu menjaga stabilitas pengiriman data instruksi sakelar pada rumah berlantai dua. |
| [5] | ferella2025prototype | Pengembangan prototipe sistem kontrol dan monitoring smart home menggunakan modul kamera yang terhubung ke jaringan IoT. | Transmisi data gambar/video menghasilkan beban bandwidth yang besar dan memicu latency spike jika jaringan lokal tidak stabil. |

## Catatan

- Kesenjangan Riset (Research Gap): Dari kelima literatur terkini (2024–2025) di atas, mayoritas penelitian NodeMCU ESP8266 hanya berfokus pada fungsionalitas (kendali jarak jauh, Blynk, Android) dan efisiensi energi. Aspek keamanan yang dibahas masih sebatas keamanan fisik (kunci pintu), sedangkan keamanan paket data (cryptography payload) sepenuhnya diabaikan dan dibiarkan dalam bentuk plaintext.
- Posisi Penelitian (State of the Art): Penelitian ini hadir untuk mengisi celah kritis tersebut. Tidak hanya membuat sistem smart home yang berfungsi, tetapi melakukan pengujian hulu-ke-hilir mengenai dampak penalti clock CPU mikro ketika algoritma pengaman (AES-128) diaktifkan secara riil, dibuktikan secara kuantitatif melalui statistik Welch's t-test (N=198).
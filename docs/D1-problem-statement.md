# Proposal Aplikasi: Sistem Parkir Berbasis Tiket QR dan Kartu Member

## 1. Deskripsi Aplikasi

Aplikasi ini adalah sistem manajemen parkir untuk area parkir komersial seperti mal, gedung perkantoran, atau kampus. Kendaraan yang masuk dicatat melalui tiket QR (untuk pengunjung umum) atau kartu member (untuk pelanggan berlangganan). Saat keluar, sistem membaca tiket atau kartu, menghitung tarif parkir berdasarkan durasi (per jam), lalu memproses pembayaran. Selain itu, aplikasi mengelola data keanggotaan, mulai dari pendaftaran, perpanjangan, hingga penonaktifan kartu. Pengelola mendapat dashboard untuk memantau kapasitas, pendapatan, dan riwayat transaksi.

## 2. Analisis Masalah

Pengelolaan parkir secara manual atau semi-manual masih menimbulkan banyak persoalan. Tiket kertas mudah hilang, rusak, atau dipalsukan, sementara perhitungan tarif oleh petugas rawan salah hitung dan memicu sengketa dengan pengguna. Proses keluar juga lambat karena petugas harus mengecek jam masuk dan menghitung biaya satu per satu, sehingga terjadi antrean kendaraan di gerbang, terutama pada jam sibuk.

Dari sisi pengelola, pencatatan kendaraan masuk dan keluar yang tidak terintegrasi menyulitkan pengawasan. Selisih antara jumlah kendaraan, pendapatan yang tercatat, dan uang yang disetor sering tidak cocok, sehingga membuka celah kebocoran pendapatan. Pengelolaan member pun masih dilakukan dengan catatan terpisah, membuat masa berlaku kartu sulit dipantau dan member yang sudah kedaluwarsa masih bisa lolos tanpa terdeteksi.

Selain itu, pengelola tidak memiliki data yang akurat tentang tingkat okupansi, jam puncak, dan tren pendapatan. Tanpa data tersebut, keputusan seperti penyesuaian tarif, penambahan gerbang, atau penawaran paket member dilakukan berdasarkan perkiraan. Dibutuhkan sistem terpusat yang mempercepat proses keluar-masuk, menghitung tarif secara otomatis dan transparan, serta menyediakan laporan yang dapat dipercaya.

## 3. Aktor

| Aktor | Peran |
|---|---|
| **Pengguna Parkir (Pengunjung)** | Mengambil tiket QR saat masuk, menunjukkan tiket saat keluar, dan membayar tarif parkir sesuai durasi. |
| **Member** | Mendaftar dan memperpanjang keanggotaan, masuk dan keluar menggunakan kartu member tanpa tiket, serta melihat masa berlaku dan riwayat parkirnya. |
| **Petugas Parkir (Operator)** | Memindai tiket atau kartu di gerbang, membantu transaksi bermasalah (tiket hilang, pembayaran gagal), menerima pembayaran tunai, dan menutup shift. |
| **Admin / Pengelola** | Mengatur tarif, mengelola data member dan kartu, memantau kapasitas serta transaksi, dan melihat laporan pendapatan. |

## 4. Scope

### Yang dikerjakan

- Penerbitan tiket QR saat kendaraan masuk (mencatat plat nomor, waktu, dan gerbang).
- Pembacaan tiket QR dan kartu member saat masuk dan keluar.
- Perhitungan tarif parkir per jam secara otomatis, termasuk tarif maksimum harian.
- Pemrosesan pembayaran (tunai dan non-tunai seperti QRIS).
- Manajemen keanggotaan: pendaftaran, perpanjangan, penonaktifan, dan validasi masa berlaku kartu.
- Penanganan kasus khusus: tiket hilang dan denda.
- Pemantauan kapasitas dan jumlah kendaraan di dalam area secara real-time.
- Dashboard dan laporan transaksi, pendapatan, serta okupansi (harian, mingguan, bulanan).
- Manajemen akun dan hak akses per peran (pengunjung, operator, admin).

### Yang TIDAK dikerjakan

1. **Pengenalan plat nomor otomatis (ALPR/OCR kamera)**. Plat nomor diinput manual atau dibaca melalui perangkat yang sudah ada.
2. **Pengembangan perangkat keras**, seperti palang otomatis, mesin tiket, dan scanner. Sistem hanya terintegrasi dengan perangkat yang sudah tersedia.
3. **Reservasi atau pemesanan slot parkir** dari jauh, serta navigasi menuju slot kosong di dalam area parkir.
4. **Integrasi dengan sistem eksternal**, seperti akuntansi perusahaan, pajak daerah, atau kebijakan parkir pemerintah.
5. **Layanan keamanan kendaraan**, termasuk CCTV, asuransi kendaraan, dan penanganan klaim kehilangan.

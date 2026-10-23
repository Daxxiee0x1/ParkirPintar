# 01 - Autentikasi & Hak Akses

## Tujuan

Memastikan setiap pengguna sistem terverifikasi dan hanya dapat mengakses fitur sesuai perannya. Modul ini menjadi dasar bagi seluruh modul lain.

## Aktor

- Pengunjung, Member, Operator, dan Admin / Pengelola.

## Fitur Utama

- Login dan logout untuk operator dan admin.
- Pengelolaan akun pengguna oleh admin (tambah, ubah, nonaktifkan).
- Pembatasan fitur berdasarkan peran (role-based access control).
- Akses pengunjung dan member melalui tiket QR atau kartu, tanpa akun untuk transaksi biasa.
- Pencatatan identitas pengguna pada setiap transaksi yang diproses.

## Aturan Bisnis

- Operator hanya dapat memproses transaksi, menerima pembayaran, dan menutup shift miliknya.
- Admin dapat mengatur tarif, member, akun, dan melihat seluruh laporan.
- Pengunjung dan member tidak memiliki akses ke dashboard pengelola.
- Akun yang dinonaktifkan tidak dapat login, tetapi riwayat transaksinya tetap tersimpan.

## Ketergantungan Modul

- Dipakai oleh modul 02 sampai 09.
- Tidak bergantung pada modul lain.

## Data yang Dikelola

- Pengguna: id, nama, peran, status aktif, dan kredensial.
- Riwayat aktivitas login.

## Alur Utama

1. Operator atau admin membuka halaman login dan memasukkan kredensial.
2. Sistem memverifikasi akun dan status aktifnya.
3. Sistem menampilkan menu sesuai peran.
4. Setiap aksi penting dicatat dengan id pengguna.

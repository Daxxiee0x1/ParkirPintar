# 04 Memberships

## Tujuan

Mengelola kartu member dari pendaftaran hingga penonaktifan, sehingga masa berlaku kartu dapat dipantau dan member yang kedaluwarsa tidak lolos tanpa terdeteksi.

## Fitur Utama

- Pendaftaran member dengan data pemilik dan kendaraan.
- Penerbitan kartu dengan nomor unik.
- Perpanjangan masa berlaku.
- Penonaktifan kartu, misalnya karena hilang atau berhenti berlangganan.
- Validasi status dan masa berlaku saat dipanggil modul 01.

## Aturan Bisnis Kunci

- Satu kartu terkait dengan satu member dan satu kendaraan terdaftar.
- Kartu yang melewati tanggal berakhir otomatis berstatus kedaluwarsa.
- Kartu yang dinonaktifkan tidak dapat diaktifkan kembali. Penggantian dilakukan dengan kartu baru.

## Ketergantungan

- Dipanggil oleh modul 01 untuk validasi.
- Mengirim data member ke modul 06.

## Alur Utama

1. Admin mendaftarkan member dan menerbitkan kartu.
2. Saat member keluar, modul 01 meminta validasi status.
3. Admin memperpanjang masa berlaku sebelum atau sesudah kedaluwarsa.

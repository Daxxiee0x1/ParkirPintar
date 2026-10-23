# 03 - Check In & Tiket

## Tujuan

Mencatat setiap kendaraan yang masuk area parkir dan menerbitkan tiket QR sebagai bukti masuk. Data dari modul ini menjadi dasar perhitungan saat keluar.

## Aktor

- Pengunjung (menerima tiket).
- Operator (memastikan pencatatan berjalan saat ada kendala).

## Fitur Utama

- Pencatatan plat nomor kendaraan, yang diinput manual atau dibaca dari perangkat yang sudah ada.
- Pencatatan waktu masuk dan gerbang masuk.
- Penerbitan tiket QR dengan kode unik.
- Pengecekan apakah kendaraan sudah tercatat masuk dan belum keluar.
- Penolakan penerbitan tiket baru jika kapasitas area penuh (sesuai pengaturan).

## Aturan Bisnis

- Satu kendaraan hanya boleh memiliki satu transaksi parkir aktif.
- Kode QR bersifat unik dan tidak dapat digunakan ulang setelah transaksi selesai.
- Kendaraan yang sudah memiliki kartu member aktif dapat masuk tanpa tiket, dan sistem mencatat masuknya sebagai transaksi member.
- Waktu masuk dicatat oleh sistem, bukan diisi manual.

## Ketergantungan Modul

- Bergantung pada modul 01 untuk identitas operator dan gerbang.
- Mengirim data ke modul 04, 08, dan 09.

## Data yang Dikelola

- Tiket: kode QR, plat nomor, waktu masuk, gerbang masuk, status.
- Transaksi parkir (dibuat saat tiket diterbitkan).

## Alur Utama

1. Kendaraan tiba di gerbang masuk dan plat nomor dicatat.
2. Sistem memeriksa status kendaraan dan kapasitas area.
3. Sistem membuat transaksi parkir dan menerbitkan tiket QR.
4. Tiket dicetak atau ditampilkan kepada pengunjung.
5. Jumlah kendaraan di dalam area bertambah (modul 08).

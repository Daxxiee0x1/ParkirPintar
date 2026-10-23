# 01 Check In & Check Out

## Tujuan

Mencatat kendaraan yang masuk, menerbitkan tiket QR, lalu memvalidasi tiket atau kartu member saat keluar. Modul ini adalah alur inti sistem.

## Fitur Utama

- Pencatatan plat nomor, waktu masuk, dan gerbang saat masuk (waktu dicatat sistem, bukan diisi manual).
- Penerbitan tiket QR dengan kode unik.
- Pembacaan tiket QR atau kartu member saat keluar.
- Penampilan rincian biaya sebelum pembayaran.
- Pembukaan palang setelah pembayaran atau validasi member berhasil.

## Aturan Bisnis Kunci

- Satu kendaraan hanya boleh memiliki satu transaksi parkir aktif.
- Tiket yang sudah dipakai untuk keluar tidak dapat digunakan lagi.
- Member dengan kartu aktif dapat masuk tanpa tiket dan keluar tanpa biaya selama masa berlaku.
- Kartu yang nonaktif atau kedaluwarsa harus membayar seperti pengunjung biasa.
- Jika pembacaan gagal, operator memproses secara manual dan mencatat alasannya.

## Ketergantungan

| No | Terhubung ke | Arah | Keterangan |
|----|--------------|------|------------|
| 1 | [02 Tarif & Kalkulasi](02-Tarif-Kalkulasi.md) | Memanggil | Meminta perhitungan biaya saat keluar |
| 2 | [03 Pembayaran](03-Pembayaran.md) | Mengirim | Meneruskan tagihan untuk dibayar |
| 3 | [04 Memberships](04-Memberships.md) | Memanggil | Validasi status dan masa berlaku kartu |
| 4 | [05 Denda](05-Denda.md) | Memanggil | Penanganan kasus tiket hilang |
| 5 | [06 Laporan](06-Laporan.md) | Mengirim | Data kendaraan masuk dan keluar |

## Alur Utama

1. Kendaraan masuk, lalu sistem membuat transaksi dan menerbitkan tiket QR.
2. Saat keluar, sistem membaca tiket atau kartu.
3. Pengunjung umum: sistem menghitung biaya dan meneruskan tagihan ke modul 03.
4. Member aktif: biaya dibebaskan dan palang terbuka.
5. Setelah lunas, transaksi ditutup dan kendaraan dikeluarkan dari area.

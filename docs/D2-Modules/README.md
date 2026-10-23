# ParkirPintar — Dokumentasi Modul

Dokumen ini memuat daftar modul sistem parkir ParkirPintar. Sistem mencatat kendaraan masuk dan keluar melalui tiket QR atau kartu member, menghitung tarif per jam, memproses pembayaran, dan mengelola keanggotaan. Acuan kebutuhan ada di [D1-problem-statement.md](../D1-problem-statement.md).

## Struktur Folder

```
docs/
├── D1-problem-statement.md
├── D2-Modules/
│   ├── README.md
│   ├── 01-CheckIn-CheckOut.md
│   ├── 02-Tarif-Kalkulasi.md
│   ├── 03-Pembayaran.md
│   ├── 04-Memberships.md
│   ├── 05-Denda.md
│   └── 06-Laporan.md
├── D3-use-case-diagram/
├── D4-sequence-diagram/
└── images/
```

## Daftar Modul

| No | Modul | Berkas | Isi Utama |
|----|-------|--------|-----------|
| 01 | Check-In & Check-Out | [01-CheckIn-CheckOut.md](01-CheckIn-CheckOut.md) | Penerbitan tiket QR saat masuk, pembacaan tiket dan kartu saat keluar |
| 02 | Tarif & Kalkulasi | [02-Tarif-Kalkulasi.md](02-Tarif-Kalkulasi.md) | Perhitungan biaya per jam dengan batas maksimum harian |
| 03 | Pembayaran | [03-Pembayaran.md](03-Pembayaran.md) | Pembayaran tunai dan QRIS, rekonsiliasi setoran operator |
| 04 | Memberships | [04-Memberships.md](04-Memberships.md) | Pendaftaran, perpanjangan, dan penonaktifan kartu member |
| 05 | Denda | [05-Denda.md](05-Denda.md) | Penanganan tiket hilang dan penetapan denda |
| 06 | Laporan | [06-Laporan.md](06-Laporan.md) | Kapasitas real-time, dashboard, dan laporan pendapatan |

## Ketergantungan Antar Modul

Tabel berikut menunjukkan modul yang memanggil atau mengirim data ke modul lain. Klik nama modul tujuan untuk membuka dokumentasinya.

| No | Modul Asal | Terhubung ke | Keterangan Hubungan |
|----|------------|--------------|---------------------|
| 1 | [01 Check-In & Check-Out](01-CheckIn-CheckOut.md) | [02 Tarif & Kalkulasi](02-Tarif-Kalkulasi.md) | Meminta perhitungan biaya saat kendaraan keluar |
| 2 | [01 Check-In & Check-Out](01-CheckIn-CheckOut.md) | [03 Pembayaran](03-Pembayaran.md) | Meneruskan tagihan untuk diproses pembayarannya |
| 3 | [01 Check-In & Check-Out](01-CheckIn-CheckOut.md) | [04 Memberships](04-Memberships.md) | Meminta validasi status dan masa berlaku kartu member |
| 4 | [01 Check-In & Check-Out](01-CheckIn-CheckOut.md) | [05 Denda](05-Denda.md) | Meneruskan kasus tiket hilang atau rusak |
| 5 | [01 Check-In & Check-Out](01-CheckIn-CheckOut.md) | [06 Laporan](06-Laporan.md) | Mengirim data kendaraan masuk dan keluar |
| 6 | [03 Pembayaran](03-Pembayaran.md) | [06 Laporan](06-Laporan.md) | Mengirim data pembayaran lunas dan rekonsiliasi shift |
| 7 | [04 Memberships](04-Memberships.md) | [06 Laporan](06-Laporan.md) | Mengirim data member aktif, kedaluwarsa, dan nonaktif |
| 8 | [05 Denda](05-Denda.md) | [02 Tarif & Kalkulasi](02-Tarif-Kalkulasi.md) | Menggunakan tarif dasar untuk menghitung denda |
| 9 | [05 Denda](05-Denda.md) | [03 Pembayaran](03-Pembayaran.md) | Meneruskan tagihan denda untuk dibayar |

### Ringkasan per Modul

| Modul | Memanggil | Dipanggil oleh |
|-------|-----------|----------------|
| [01 Check-In & Check-Out](01-CheckIn-CheckOut.md) | [02](02-Tarif-Kalkulasi.md), [03](03-Pembayaran.md), [04](04-Memberships.md), [05](05-Denda.md), [06](06-Laporan.md) | - |
| [02 Tarif & Kalkulasi](02-Tarif-Kalkulasi.md) | - | [01](01-CheckIn-CheckOut.md), [05](05-Denda.md) |
| [03 Pembayaran](03-Pembayaran.md) | [06](06-Laporan.md) | [01](01-CheckIn-CheckOut.md), [05](05-Denda.md) |
| [04 Memberships](04-Memberships.md) | [06](06-Laporan.md) | [01](01-CheckIn-CheckOut.md) |
| [05 Denda](05-Denda.md) | [02](02-Tarif-Kalkulasi.md), [03](03-Pembayaran.md) | [01](01-CheckIn-CheckOut.md) |
| [06 Laporan](06-Laporan.md) | - | [01](01-CheckIn-CheckOut.md), [03](03-Pembayaran.md), [04](04-Memberships.md) |

## Aturan Lintas Modul

Aturan berikut berlaku untuk seluruh modul dan tidak dibuat sebagai modul tersendiri:

- **Hak akses per peran.** Pengunjung dan member hanya menggunakan tiket atau kartu. Operator memproses transaksi dan shift miliknya. Admin mengatur tarif, member, akun, dan laporan.
- **Satu transaksi aktif per kendaraan.** Angka pada laporan, kapasitas, dan setoran dibaca dari transaksi yang sama.

## Ruang Lingkup di Luar Sistem

Pengenalan plat nomor otomatis, pengembangan perangkat keras (palang, mesin tiket, scanner), reservasi slot parkir, integrasi dengan sistem akuntansi atau pajak, dan layanan keamanan kendaraan tidak termasuk dalam dokumentasi modul.

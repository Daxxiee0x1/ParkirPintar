# 05 Denda

## Tujuan

Menangani tiket hilang dengan aturan yang jelas dan tercatat, sehingga operator tidak mengambil keputusan tanpa dasar.

## Fitur Utama

- Pencatatan kasus tiket hilang atau rusak beserta alasannya.
- Pencarian transaksi aktif berdasarkan plat nomor.
- Penetapan biaya: tarif dari modul 02 ditambah denda.

## Aturan Bisnis Kunci

- Nilai denda diatur admin dan tidak tersedia di proposal.
- Kasus hanya dapat diselesaikan operator setelah plat nomor cocok dengan transaksi aktif.
- Kasus yang tidak dapat diverifikasi diteruskan ke admin, bukan diselesaikan sepihak oleh operator.
- Catatan kasus tidak dapat dihapus.

## Ketergantungan

| No | Terhubung ke | Arah | Keterangan |
|----|--------------|------|------------|
| 1 | [01 Check In & Check Out](01-CheckIn-CheckOut.md) | Dipanggil | Kasus tiket hilang atau rusak |
| 2 | [02 Tarif & Kalkulasi](02-Tarif-Kalkulasi.md) | Memanggil | Tarif dasar untuk denda |
| 3 | [03 Pembayaran](03-Pembayaran.md) | Mengirim | Tagihan denda |

## Alur Utama

1. Pengunjung melaporkan tiket hilang di gerbang keluar.
2. Operator memasukkan plat nomor, dan sistem mencari transaksi aktif yang cocok.
3. Sistem menghitung tarif dan denda, lalu meneruskan tagihan ke modul 03.

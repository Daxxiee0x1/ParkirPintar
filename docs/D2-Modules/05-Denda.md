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

- Dipanggil oleh modul 01 saat tiket hilang.
- Menggunakan modul 02 untuk tarif dasar.
- Mengirim tagihan denda ke modul 03.

## Alur Utama

1. Pengunjung melaporkan tiket hilang di gerbang keluar.
2. Operator memasukkan plat nomor, dan sistem mencari transaksi aktif yang cocok.
3. Sistem menghitung tarif dan denda, lalu meneruskan tagihan ke modul 03.

# 06 Laporan

## Tujuan

Memberikan pengelola data tentang kapasitas, pendapatan, dan okupansi, sehingga keputusan tarif atau penambahan gerbang didasarkan pada data.

## Fitur Utama

- Jumlah kendaraan di dalam area secara real-time dan persentase okupansi.
- Peringatan saat okupansi mencapai ambang yang diatur admin.
- Dashboard ringkasan: kendaraan di dalam, pendapatan hari ini, dan transaksi terakhir.
- Laporan pendapatan harian, mingguan, dan bulanan, dipisahkan per metode pembayaran.
- Laporan jam puncak dan selisih setoran per shift.

## Aturan Bisnis Kunci

- Jumlah kendaraan bertambah saat masuk dan berkurang saat keluar selesai.
- Modul ini hanya membaca data dan tidak mengubah transaksi.
- Pendapatan hanya dihitung dari pembayaran berstatus lunas.
- Laporan hanya dapat diakses admin.

## Ketergantungan

- Membaca data dari modul 01, 03, dan 04.

## Alur Utama

1. Admin membuka dashboard untuk melihat ringkasan terkini.
2. Admin memilih jenis laporan dan rentang tanggal.
3. Sistem mengagregasi data dari modul sumber dan menampilkannya.

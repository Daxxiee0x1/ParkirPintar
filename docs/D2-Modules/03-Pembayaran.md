# 03 Pembayaran

## Tujuan

Memastikan setiap pembayaran tercatat dan uang tunai yang disetor operator sesuai dengan catatan sistem. Modul ini menutup celah kebocoran pendapatan.

## Fitur Utama

- Pembayaran tunai yang dicatat operator.
- Pembayaran non-tunai melalui QRIS.
- Pembukaan dan penutupan shift oleh operator.
- Rekapitulasi shift: total tunai seharusnya, total disetor, dan selisih.

## Aturan Bisnis Kunci

- Satu transaksi hanya dapat dibayar satu kali.
- Pembayaran gagal tidak mengubah status transaksi menjadi lunas.
- Operator hanya dapat menerima pembayaran dalam shift yang sedang aktif.
- Shift tidak dapat ditutup selama masih ada transaksi tunai yang belum selesai.
- Selisih setoran tidak boleh dihapus. Admin hanya dapat menambahkan catatan penjelasan.

## Ketergantungan

- Menerima tagihan dari modul 01 dan modul 05.
- Mengirim data pembayaran ke modul 06.

## Alur Utama

1. Sistem menampilkan tagihan.
2. Pengunjung memilih tunai (dicatat operator) atau QRIS.
3. Pembayaran berhasil dicatat dan transaksi berstatus lunas.
4. Saat shift ditutup, sistem membandingkan total tunai dengan setoran dan menyimpan selisihnya.

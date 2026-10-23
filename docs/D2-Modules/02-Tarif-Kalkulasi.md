# 02 Tarif & Kalkulasi

## Tujuan

Menghitung biaya parkir secara otomatis dan konsisten, sehingga mengurangi kesalahan hitung oleh petugas dan sengketa dengan pengguna.

## Fitur Utama

- Pengaturan tarif per jam dan tarif maksimum harian oleh admin.
- Pengaturan tanggal berlaku tarif.
- Perhitungan durasi dan biaya dengan rincian yang dapat ditampilkan.

## Aturan Bisnis Kunci

- Tarif yang berlaku ditentukan oleh waktu masuk, bukan waktu keluar. Perubahan tarif tidak mengubah transaksi yang sudah berjalan.
- Biaya tidak boleh melebihi tarif maksimum harian untuk satu hari kalender.
- Input yang sama selalu menghasilkan biaya yang sama.
- Nilai tarif dan aturan pembulatan durasi tidak tersedia di proposal. Keduanya harus dikonfigurasi oleh pengelola, bukan ditulis tetap di kode.

## Ketergantungan

- Dipanggil oleh modul 01 (biaya keluar) dan modul 05 (tarif dasar denda).
- Hasilnya menjadi tagihan di modul 03.

## Alur Utama

1. Admin menyimpan tarif baru dengan tanggal berlaku.
2. Saat keluar, sistem mengambil tarif yang berlaku pada waktu masuk.
3. Sistem menghitung durasi × tarif per jam, lalu membatasi hasilnya dengan tarif maksimum harian.

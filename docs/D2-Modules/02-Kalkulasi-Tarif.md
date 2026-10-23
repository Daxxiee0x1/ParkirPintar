# 02 - Tarif & Kalkulasi

## Tujuan

Menghitung biaya parkir secara otomatis dan transparan berdasarkan durasi, sehingga mengurangi kesalahan hitung oleh petugas dan sengketa dengan pengguna.

## Aktor

- Admin (pengaturan tarif).
- Sistem (perhitungan otomatis saat keluar atau denda).

## Fitur Utama

- Pengaturan tarif per jam.
- Pengaturan tarif maksimum harian.
- Pengaturan periode berlaku tarif, termasuk perubahan tarif terjadwal.
- Perhitungan durasi dari waktu masuk hingga waktu keluar.
- Perhitungan biaya yang dapat diulang dan ditelusuri (hasil yang sama untuk input yang sama).
- Menampilkan rincian perhitungan kepada pengguna.

## Aturan Bisnis

- Durasi dibulatkan ke jam berikutnya untuk setiap jam yang sudah berjalan, kecuali kebijakan pengelola menyatakan lain. Aturan pembulatan harus dikonfigurasi, bukan ditulis tetap di kode.
- Biaya tidak boleh melebihi tarif maksimum harian untuk satu hari kalender.
- Tarif yang berlaku ditentukan oleh waktu masuk kendaraan, bukan waktu keluar. Perubahan tarif tidak mengubah transaksi yang sudah berjalan.
- Nilai tarif tidak tersedia dalam proposal dan harus diisi oleh pengelola melalui konfigurasi.

## Ketergantungan Modul

- Dipakai oleh modul 04 (biaya keluar), 05 (jumlah tagihan), dan 07 (denda).
- Bergantung pada modul 01 untuk pembatasan akses admin.

## Data yang Dikelola

- Tarif: id, nilai per jam, tarif maksimum harian, tanggal mulai, tanggal selesai.
- Aturan pembulatan durasi.

## Alur Utama

1. Admin menyimpan tarif baru dengan tanggal berlaku.
2. Saat kendaraan keluar, sistem mengambil tarif yang berlaku pada waktu masuk.
3. Sistem menghitung durasi, mengalikan dengan tarif per jam, dan membatasi hasil dengan tarif maksimum harian.
4. Hasil dikirim ke modul 05 sebagai tagihan.

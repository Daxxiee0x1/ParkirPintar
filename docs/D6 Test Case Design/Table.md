# D6. Test Case Design

## Skenario yang Dipilih

**Check-Out Kendaraan dan Pembayaran Parkir**

Skenario ini mencakup alur keluar kendaraan, mulai dari pembacaan tiket QR atau kartu member, perhitungan biaya, sampai pembayaran dan pembukaan palang. Skenario ini melibatkan modul [01 Check In & Check Out](../D2-Modules/01-CheckIn-CheckOut.md), [02 Tarif & Kalkulasi](../D2-Modules/02-Tarif-Kalkulasi.md), [03 Pembayaran](../D2-Modules/03-Pembayaran.md), dan [04 Memberships](../D2-Modules/04-Memberships.md).

## Asumsi

- Tarif Rp5.000 per jam dan maksimum Rp30.000 per hari.
- Durasi dibulatkan ke atas per jam.
- Nilai di atas hanyalah contoh untuk pengujian, karena tarif dan aturan pembulatan dikonfigurasi oleh pengelola.

## Common Cases

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
|----|-------|------|---------------|---------------|-----------------|
| TC-01 | Keluar dengan tiket QR, bayar tunai | Common | Kendaraan masuk 08:00 dengan tiket aktif; shift operator aktif | Scan tiket pukul 10:00, lalu operator mencatat pembayaran tunai Rp10.000 | Biaya Rp10.000 tampil; pembayaran tercatat; transaksi lunas dan ditutup; palang terbuka |
| TC-02 | Keluar dengan tiket QR, bayar QRIS | Common | Kendaraan masuk 08:00 dengan tiket aktif | Scan tiket pukul 11:00, pilih QRIS, bayar Rp15.000 | Pembayaran QRIS berhasil; transaksi lunas dan ditutup; palang terbuka |
| TC-03 | Member aktif keluar tanpa biaya | Common | Kartu member aktif, berlaku sampai 31 Des 2026; kendaraan sudah masuk | Tempelkan kartu di gerbang keluar | Biaya Rp0; transaksi ditutup; palang terbuka |
| TC-04 | Biaya dibatasi tarif maksimum harian | Common | Kendaraan masuk 08:00 pada hari yang sama | Scan tiket pukul 20:00 (12 jam) | Biaya Rp30.000, bukan Rp60.000 |
| TC-05 | Rincian biaya tampil sebelum pembayaran | Common | Kendaraan masuk 08:00 dengan tiket aktif | Scan tiket pukul 10:30 | Rincian tampil: durasi 2 jam 30 menit dibulatkan 3 jam, tarif Rp5.000, total Rp15.000 |

## Edge Cases

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
|----|-------|------|---------------|---------------|-----------------|
| TC-06 | Durasi tepat melewati batas jam | Edge | Kendaraan masuk 08:00 dengan tiket aktif | Scan tiket pukul 09:01 (1 jam 1 menit) | Dibulatkan menjadi 2 jam, biaya Rp10.000 (bandingkan dengan tepat 09:00 = Rp5.000) |
| TC-07 | Tiket yang sudah dipakai dipindai ulang | Edge | Tiket sudah dipakai keluar; transaksi berstatus selesai | Scan tiket yang sama sekali lagi | Ditolak dengan pesan "Tiket sudah digunakan"; palang tetap tertutup |
| TC-08 | Kartu member kedaluwarsa | Edge | Kartu berakhir 1 Okt 2026; hari ini 27 Okt 2026 | Tempelkan kartu di gerbang keluar | Tidak dibebaskan biaya; sistem menampilkan tagihan seperti pengunjung biasa dan memberi tahu operator |
| TC-09 | Pembayaran QRIS gagal atau timeout | Edge | Tagihan sudah tampil; pembayaran QRIS belum terkonfirmasi | Pengunjung memilih QRIS, tetapi pembayaran gagal | Transaksi tetap belum lunas; palang tertutup; pengunjung dapat mencoba lagi atau beralih ke tunai |
| TC-10 | Tiket hilang dengan plat nomor tidak cocok | Edge | Tiket hilang; tidak ada transaksi aktif dengan plat B 9999 ZZ | Operator memasukkan plat B 9999 ZZ | Kasus tidak dapat diselesaikan operator; diteruskan ke admin; palang tetap tertutup |

## Cara Memilih Edge Case

Edge case diturunkan langsung dari aturan bisnis di dokumentasi modul, terutama aturan yang berkaitan dengan masalah utama proposal, yaitu kebocoran pendapatan dan member kedaluwarsa yang lolos. TC-06 mewakili nilai batas, karena selisih satu menit dapat mengubah biaya satu jam penuh. TC-07 mewakili duplikasi, karena tiket hanya boleh dipakai sekali. TC-08 dan TC-10 mewakili kondisi tidak terduga dan input tidak valid, yaitu kartu yang statusnya sudah kedaluwarsa dan plat nomor yang tidak cocok dengan transaksi. TC-09 mewakili kegagalan sistem eksternal, karena pembayaran yang gagal tidak boleh menjadikan transaksi lunas.

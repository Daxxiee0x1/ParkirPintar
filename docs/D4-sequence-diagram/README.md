# D4. Sequence Diagram

Tiga skenario dipilih karena mewakili alur utama sistem dari masuk, keluar dan bayar, sampai penanganan kasus khusus. Aktor, UI, dan modul sistem menjadi lifeline, dan tiap diagram memuat fragmen `alt` atau `opt` untuk alur alternatif.

| No | Skenario | Alasan dipilih | Diagram | Pemegang |
|---|---|---|---|---|
| 1 | Check-in kendaraan (tiket QR dan kartu member) | Titik awal semua transaksi. Di sini sistem memutuskan apakah pengunjung dapat tiket QR atau masuk sebagai member, dan menolak kendaraan yang sudah tercatat di dalam. | [PNG](Check%20In.png), [sumber](Check%20In.puml) | Ataya Nafis Rizqulah |
| 2 | Check-out pengunjung umum: hitung tarif dan pembayaran | Alur yang menghasilkan pendapatan dan paling sering dipakai. Melibatkan modul tarif, pembayaran tunai dan QRIS, serta pembukaan palang, dengan jalur tiket tidak valid dan pembayaran gagal. | [PNG](Check%20out%20pembayaran.png), [sumber](Check%20out%20pembayaran.puml) | Aditya Bintoro |
| 3 | Tiket hilang dan denda | Kasus khusus yang paling rawan sengketa dan kebocoran pendapatan. Menunjukkan aturan bahwa operator tidak boleh menyelesaikan kasus yang tidak terverifikasi sepihak. | [PNG](Denda%20Tiket%20Hilang.png), [sumber](Denda%20Tiket%20Hilang.puml) | Haekal Syahputra |

Setiap anggota memegang satu diagram, dan pekerjaannya tercatat di [ACTIVITY_LOG.md](../../ACTIVITY_LOG.md).

**Penghitungan Tarif Parkir**
 
Skenario ini menguji fungsi penghitungan biaya parkir pada modul [02 Tarif & Kalkulasi](../D2-Modules/02-Tarif-Kalkulasi.md): menghitung durasi dari waktu masuk sampai keluar, mengalikannya dengan tarif per jam, lalu membatasi hasilnya dengan tarif maksimum harian.
 
## Asumsi
 
- Tarif Rp5.000 per jam dan maksimum Rp30.000 per hari.
- Durasi dibulatkan ke atas per jam.
- Nilai di atas hanyalah contoh untuk pengujian, karena tarif dan aturan pembulatan dikonfigurasi oleh pengelola.
## Common Cases
 
| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
|----|-------|------|---------------|---------------|-----------------|
| TC-01 | Durasi kurang dari 1 jam | Common | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 08:30 (30 menit) | Dibulatkan menjadi 1 jam, biaya Rp5.000 |
| TC-02 | Durasi beberapa jam penuh | Common | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 11:00 (3 jam) | Biaya Rp15.000 |
| TC-03 | Durasi tidak penuh dibulatkan ke atas | Common | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 10:30 (2 jam 30 menit) | Dibulatkan menjadi 3 jam, biaya Rp15.000 |
| TC-04 | Biaya mencapai tarif maksimum harian | Common | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 20:00 (12 jam) | Biaya Rp30.000, bukan Rp60.000 |
| TC-05 | Tarif mengikuti waktu masuk | Common | Tarif Rp5.000 berlaku sebelum 27 Okt 2026 pukul 09:00; tarif baru Rp7.000 berlaku mulai pukul 09:00 | Masuk 27 Okt 2026 08:00, keluar 10:00 | Memakai tarif lama: 2 jam × Rp5.000 = Rp10.000 |

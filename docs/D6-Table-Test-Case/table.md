# Penghitungan Tarif Parkir

Skenario ini menguji fungsi penghitungan biaya parkir pada modul **02 Tarif & Kalkulasi**. Sistem menghitung biaya berdasarkan durasi parkir sejak kendaraan masuk hingga keluar, menggunakan tarif yang berlaku saat kendaraan masuk, kemudian membatasi biaya sesuai tarif maksimum per sesi parkir.

## Asumsi

- Tarif parkir contoh: **Rp5.000 per jam**.
- Tarif maksimum: **Rp30.000 per sesi parkir**.
- Durasi kurang dari satu jam dihitung sebagai satu jam.
- Durasi yang tidak mencapai satu jam penuh dibulatkan ke atas.
- Tarif yang digunakan adalah tarif yang berlaku saat kendaraan masuk.
- Satu sesi parkir dimulai saat kendaraan masuk dan berakhir saat kendaraan keluar.
- Pergantian hari tidak memulai sesi atau batas maksimum baru.
- Tarif dan batas maksimum merupakan nilai contoh yang dapat diubah oleh pengelola melalui konfigurasi sistem.

## Common Cases

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
|---|---|---|---|---|---|
| TC-01 | Durasi parkir kurang dari satu jam | Common | Tarif Rp5.000/jam; maksimum Rp30.000/sesi | Masuk pukul 08:00, keluar pukul 08:30 | Durasi dibulatkan menjadi 1 jam. Biaya akhir Rp5.000. |
| TC-02 | Durasi parkir tidak penuh | Common | Tarif Rp5.000/jam; maksimum Rp30.000/sesi | Masuk pukul 08:00, keluar pukul 10:30 | Durasi dibulatkan menjadi 3 jam. Biaya akhir Rp15.000. |
| TC-03 | Biaya melebihi tarif maksimum | Common | Tarif Rp5.000/jam; maksimum Rp30.000/sesi | Masuk pukul 08:00, keluar pukul 18:00 | Durasi 10 jam. Biaya normal Rp50.000, sehingga biaya akhir dibatasi menjadi Rp30.000. |
| TC-04 | Parkir melewati pergantian hari | Common | Tarif Rp5.000/jam; maksimum Rp30.000/sesi | Masuk 27 Okt 2026 pukul 20:00, keluar 28 Okt 2026 pukul 04:00 | Durasi 8 jam. Biaya akhir Rp30.000. Pergantian hari tidak memulai sesi baru. |
| TC-05 | Tarif berubah setelah kendaraan masuk | Common | Tarif Rp5.000/jam berlaku sebelum 27 Okt 2026 pukul 09:00; tarif baru Rp7.000/jam berlaku mulai pukul 09:00 | Masuk 27 Okt 2026 pukul 08:00, keluar pukul 10:00 | Sistem tetap menggunakan tarif saat masuk, yaitu Rp5.000/jam. Durasi 2 jam, sehingga biaya akhir Rp10.000. |

## Aturan Perhitungan

1. Sistem mencatat waktu masuk dan waktu keluar kendaraan.
2. Sistem menghitung durasi parkir berdasarkan selisih waktu masuk dan keluar.
3. Durasi dibulatkan ke atas dalam satuan jam.
4. Biaya normal dihitung dengan mengalikan durasi yang dibulatkan dengan tarif per jam saat kendaraan masuk.
5. Jika biaya normal melebihi tarif maksimum per sesi, sistem menggunakan tarif maksimum sebagai biaya akhir.

**Rumus:**

- **Biaya normal** = Durasi parkir yang dibulatkan ke atas × Tarif per jam
- **Biaya akhir** = Nilai terkecil antara biaya normal dan tarif maksimum per sesi

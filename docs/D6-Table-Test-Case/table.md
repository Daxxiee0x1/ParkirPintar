# Penghitungan Tarif Parkir

Skenario ini menguji fungsi penghitungan biaya parkir pada modul **02 Tarif & Kalkulasi**. Sistem menghitung biaya berdasarkan durasi parkir sejak kendaraan masuk hingga keluar, menggunakan tarif yang berlaku saat kendaraan masuk, kemudian membatasi biaya sesuai tarif maksimum per sesi parkir.

## Cara Memilih Edge Case

Edge case dipilih dengan memeriksa titik-titik tempat fungsi hitung tarif paling mungkin salah, yaitu nilai batas, input tidak valid, dan aturan khusus waktu. Nilai batas diuji pada pembulatan jam (TC-08: 1 jam 1 menit dihitung 2 jam) dan pada tarif maksimum, dengan menguji tepat di batas (TC-09) dan 1 menit sesudahnya (TC-10). Input yang tidak lazim diuji lewat durasi nol (TC-06), waktu keluar sebelum masuk (TC-07), waktu masuk kosong (TC-13), dan format waktu tidak valid (TC-14), agar sistem menolaknya dengan pesan jelas dan tidak menghitung biaya yang salah. Kasus pergantian hari (TC-11 dan TC-12) dipilih karena batas maksimum dihitung per hari kalender, sehingga parkir yang melewati tengah malam bisa menghasilkan biaya berbeda dari perkiraan awal. Terakhir, TC-15 memastikan input yang sama selalu menghasilkan biaya yang sama, sesuai aturan bisnis pada modul Tarif & Kalkulasi.

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
| TC-04 | Durasi parkir tepat mencapai batas tarif maksimum | Common | Tarif Rp5.000/jam; maksimum Rp30.000/sesi | Masuk pukul 07:00, keluar pukul 13:00 | Durasi tepat 6 jam. Biaya normal Rp30.000, biaya akhir pas sesuai batas maksimum Rp30.000. |
| TC-05 | Tarif berubah setelah kendaraan masuk | Common | Tarif Rp5.000/jam berlaku sebelum 27 Okt 2026 pukul 09:00; tarif baru Rp7.000/jam berlaku mulai pukul 09:00 | Masuk 27 Okt 2026 pukul 08:00, keluar pukul 10:00 | Sistem tetap menggunakan tarif saat masuk, yaitu Rp5.000/jam. Durasi 2 jam, sehingga biaya akhir Rp10.000. |

## Edge Cases

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
|----|-------|------|---------------|---------------|-----------------|
| TC-06 | Durasi 0 menit | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 08:00 | Biaya Rp0 |
| TC-07 | Waktu keluar sebelum waktu masuk | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 10:00, keluar 08:00 | Ditolak dengan pesan kesalahan "waktu keluar tidak boleh sebelum waktu masuk", biaya tidak dihitung |
| TC-08 | Durasi 1 menit melewati batas jam | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 09:01 (1 jam 1 menit) | Dibulatkan menjadi 2 jam, biaya Rp10.000 |
| TC-09 | Biaya tepat sama dengan tarif maksimum | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 14:00 (6 jam) | Biaya Rp30.000 (6 × Rp5.000, tidak dipotong) |
| TC-10 | Durasi 1 menit melewati batas tarif maksimum | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar 14:01 (6 jam 1 menit) | Dibulatkan menjadi 7 jam = Rp35.000, dibatasi menjadi Rp30.000 |
| TC-11 | Parkir melewati tengah malam | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari (per hari kalender) | Masuk 27 Okt 23:00, keluar 28 Okt 01:00 | 1 jam di hari pertama dan 1 jam di hari kedua, biaya Rp10.000 |
| TC-12 | Parkir lebih dari satu hari kalender | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari kalender | Masuk 27 Okt 08:00, keluar 28 Okt 10:00 | Hari pertama 16 jam dibatasi Rp30.000, hari kedua 10 jam dibatasi Rp30.000, total Rp60.000 |
| TC-13 | Waktu masuk kosong atau tidak ditemukan | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Waktu masuk kosong, keluar 10:00 | Ditolak dengan pesan kesalahan "data waktu masuk tidak ditemukan", biaya tidak dihitung |
| TC-14 | Format waktu tidak valid | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Masuk 08:00, keluar "25:99" | Ditolak dengan pesan kesalahan format waktu, biaya tidak dihitung |
| TC-15 | Perhitungan yang sama dilakukan dua kali | Edge | Tarif Rp5.000 per jam, maksimum Rp30.000 per hari | Hitung biaya untuk masuk 08:00, keluar 10:00 sebanyak dua kali berturut-turut | Kedua hasil Rp10.000, input yang sama selalu menghasilkan biaya yang sama |

## Aturan Perhitungan

1. Sistem mencatat waktu masuk dan waktu keluar kendaraan.
2. Sistem menghitung durasi parkir berdasarkan selisih waktu masuk dan keluar.
3. Durasi dibulatkan ke atas dalam satuan jam.
4. Biaya normal dihitung dengan mengalikan durasi yang dibulatkan dengan tarif per jam saat kendaraan masuk.
5. Jika biaya normal melebihi tarif maksimum per sesi, sistem menggunakan tarif maksimum sebagai biaya akhir.


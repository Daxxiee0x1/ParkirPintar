# D3. Use Case Diagram

![Use case diagram](https://github.com/Daxxiee0x1/ParkirPintar/blob/docs/use-case-diagram/docs/D3-use-case-diagram/Use%20Case%20DIagram%20-%20ParkirPintar.png)
Sumber: [use-case.puml](https://github.com/Daxxiee0x1/ParkirPintar/blob/docs/use-case-diagram/docs/D3-use-case-diagram/Use%20Case%20Diagram%20-%20ParkirPintar.puml)

## Aktor
| Aktor | Peran |
|---|---|
| Pengunjung | Check-in dan check-out dengan tiket QR |
| Member | Check-in dan check-out dengan kartu member |
| Operator | Memproses gerbang, shift, dan tiket hilang |
| Admin / Pengelola | Mengatur tarif, member, laporan, dan memutuskan kasus |

## Relasi
| Relasi | Alasan |
|---|---|
| Bayar Parkir `<<include>>` Hitung Tarif | Pembayaran selalu butuh perhitungan tarif |
| Bayar Parkir `<<extend>>` Check-out | Hanya pengunjung umum yang membayar, member aktif keluar tanpa biaya |
| Tangani Tiket Hilang `<<extend>>` Check-out | Hanya jika tiket hilang atau rusak |
| Validasi Kartu Member `<<extend>>` Check-in | Hanya jika kartu member dipindai |

## Warna dan modul
Warna use case mengikuti modul D2 (lihat legenda pada gambar).

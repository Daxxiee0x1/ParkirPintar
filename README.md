# ParkirPintar

Sistem parkir berbasis tiket QR dan kartu member. Aplikasi ini mencatat kendaraan masuk dan keluar, menghitung tarif parkir per jam, memproses pembayaran, dan mengelola keanggotaan.

## Anggota Tim

| Nama | NIM | Username GitHub |
|---|---|---|
| Haekal Syahputra | 26110300015 | [@Daxxiee0x1](https://github.com/Daxxiee0x1) |
| Ataya Nafis Rizqulah | 26110300005 | [@Ataya24](https://github.com/Ataya24) |
| Aditya Bintoro | 26110300021 | [@AdityaBintoro](https://github.com/AdityaBintoro) |

## Daftar Deliverable

| Kode | Deliverable | Link |
|---|---|---|
| D1 | Topik & Problem Statement | [docs/D1-problem-statement.md](docs/D1-problem-statement.md) |
| D2 | Module Breakdown | [docs/D2-Modules/README.md](docs/D2-Modules/README.md) |
| D3 | Use Case Diagram | [docs/D3-use-case-diagram/README.md](docs/D3-use-case-diagram/README.md) |
| D4 | Sequence Diagram (3 skenario) | [docs/D4-sequence-diagram/README.md](docs/D4-sequence-diagram/README.md) |
| D5 | Kolaborasi GitHub & Activity Log | [ACTIVITY_LOG.md](ACTIVITY_LOG.md) |
| D6 | Test Case Design (skenario penghitungan tarif parkir) | [docs/D6-Table-Test-Case/table.md](docs/D6-Table-Test-Case/table.md) |
| D7 | Unit-Tested Code | Kode: [src/tarif_parkir.py](src/tarif_parkir.py) · Test: [tests/test_tarif_parkir.py](tests/test_tarif_parkir.py) · Screenshot: [hasil test](docs/images/hasil%20Unit-Tested%20Code.png) |

## Cara Menjalankan Test

```bash
# 1. Clone repo
git clone https://github.com/Daxxiee0x1/ParkirPintar.git
cd ParkirPintar

# 2. Install dependensi
pip install -r requirements.txt

# 3. Jalankan semua test (ringkas)
python -m pytest

#4. Jalankan semua test (detail)
python -m pytest -v
```

## Struktur Repo

```
ParkirPintar/
├── README.md
├── ACTIVITY_LOG.md
├── docs/
├── src/
└── tests/
```

## Penggunaan AI

from datetime import datetime
import pytest
from project_sdf.tarif_parkir import hitung_tarif_parkir

TARIF_DEFAULT = 5000
MAX_TARIF = 30000


# common cases
def test_tc01_durasi_kurang_dari_satu_jam():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T08:30:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 5000

def test_tc02_durasi_tidak_penuh():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T10:30:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 15000

def test_tc03_biaya_melebihi_tarif_maksimum():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T18:00:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 30000

def test_tc04_Durasi_parkir_tepat_mencapai_batas_tarif_maksimum():
    biaya = hitung_tarif_parkir("2026-10-27T07:00:00", "2026-10-27T13:00:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 30000

def test_tc05_tarif_berubah_setelah_kendaraan_masuk():
    tarif_historis = [
        (datetime.fromisoformat("2026-10-27T09:00:00"), 7000)
    ]
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T10:00:00", TARIF_DEFAULT, MAX_TARIF, tarif_historis)
    assert biaya == 10000 



# edge cases
def test_tc06_durasi_nol_menit():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T08:00:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 0

def test_tc07_waktu_keluar_sebelum_masuk():
    with pytest.raises(ValueError, match="waktu keluar tidak boleh sebelum waktu masuk"):
        hitung_tarif_parkir("2026-10-27T10:00:00", "2026-10-27T08:00:00", TARIF_DEFAULT, MAX_TARIF)

def test_tc08_durasi_satu_menit_melewati_batas_jam():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T09:01:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 10000

def test_tc09_biaya_tepat_sama_dengan_maksimum():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T14:00:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 30000

def test_tc10_durasi_satu_menit_melewati_maksimum():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T14:01:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 30000

def test_tc11_parkir_melewati_tengah_malam():
    biaya = hitung_tarif_parkir("2026-10-27T23:00:00", "2026-10-28T01:00:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 10000

def test_tc12_parkir_lebih_dari_satu_hari_kalender():
    biaya = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-28T10:00:00", TARIF_DEFAULT, MAX_TARIF)
    assert biaya == 60000

def test_tc13_waktu_masuk_kosong():
    with pytest.raises(ValueError, match="data waktu masuk tidak ditemukan"):
        hitung_tarif_parkir(None, "2026-10-27T10:00:00", TARIF_DEFAULT, MAX_TARIF)

def test_tc14_format_waktu_tidak_valid():
    with pytest.raises(ValueError, match="format waktu tidak valid"):
        hitung_tarif_parkir("2026-10-27T08:00:00", "25:99", TARIF_DEFAULT, MAX_TARIF)

def test_tc15_perhitungan_berulang_konsisten():
    hasil_1 = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T10:00:00", TARIF_DEFAULT, MAX_TARIF)
    hasil_2 = hitung_tarif_parkir("2026-10-27T08:00:00", "2026-10-27T10:00:00", TARIF_DEFAULT, MAX_TARIF)
    assert hasil_1 == hasil_2
    assert hasil_1 == 10000
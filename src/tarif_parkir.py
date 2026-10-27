from datetime import datetime, timedelta
import math

def hitung_tarif_parkir(waktu_masuk, waktu_keluar, tarif_per_jam=5000, max_tarif=30000, tarif_historis=None):
    """
    Menghitung biaya parkir berdasarkan waktu masuk, waktu keluar, 
    tarif per jam, dan batas maksimum tarif per sesi/hari.
    """
    if not waktu_masuk:
        raise ValueError("data waktu masuk tidak ditemukan")
        
    try:
        if isinstance(waktu_masuk, str):
            dt_masuk = datetime.fromisoformat(waktu_masuk)
        else:
            dt_masuk = waktu_masuk
            
        if isinstance(waktu_keluar, str):
            dt_keluar = datetime.fromisoformat(waktu_keluar)
        else:
            dt_keluar = waktu_keluar
    except Exception:
        raise ValueError("format waktu tidak valid")
        
    if dt_keluar < dt_masuk:
        raise ValueError("waktu keluar tidak boleh sebelum waktu masuk")
        
    tarif_aktif = tarif_per_jam
    if tarif_historis:
        for batas_waktu, nilai in sorted(tarif_historis, key=lambda x: x[0]):
            if dt_masuk >= batas_waktu:
                tarif_aktif = nilai

    if dt_keluar.date() > dt_masuk.date():
        total_biaya = 0
        current_time = dt_masuk
        
        while current_time < dt_keluar:
        
            next_day_midnight = datetime(current_time.year, current_time.month, current_time.day) + timedelta(days=1)
            end_segment = min(dt_keluar, next_day_midnight)
            
            selisih_segment = end_segment - current_time
            menit_segment = selisih_segment.total_seconds() / 60
            
            if menit_segment > 0:
                jam_segment = math.ceil(menit_segment / 60)
                biaya_segment = min(jam_segment * tarif_aktif, max_tarif)
                total_biaya += biaya_segment
                
            current_time = next_day_midnight
            
        return total_biaya
    
    selisih = dt_keluar - dt_masuk
    total_menit = selisih.total_seconds() / 60
    
    if total_menit == 0:
        return 0
        
    durasi_jam = math.ceil(total_menit / 60)
    biaya_normal = durasi_jam * tarif_aktif
    
    return min(biaya_normal, max_tarif)
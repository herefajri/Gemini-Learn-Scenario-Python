import random
import time

class SensorKota:
    def __init__(self, lokasi):
        self.lokasi = lokasi

    def cek_status_sensor(self):
        print(f'[SISTEM] Sensor di {self.lokasi} Berfungsi dengan Baik')

class KameraSensor(SensorKota):
    def __init__(self, lokasi):
        super().__init__(lokasi)
        self.jumlah_kendaraan = random.randint(0, 50)

    def dapatkan_durasi(self):
        print(f'[KAMERA] Jumlah kendaraan di {self.lokasi}: {self.jumlah_kendaraan}')
        if self.jumlah_kendaraan > 30:
            return 45
        elif 10 < self.jumlah_kendaraan <= 30:
            return 30

        return 15
    
    def hitung_mundur(self, durasi):
        print(f'[KAMERA] Menghitung mundur durasi lampu hijau selama {durasi} detik...')
        while durasi > 0:
            waktu_detik = {self.jumlah_kendaraan: 60}
            menit, detik = divmod(durasi, waktu_detik[self.jumlah_kendaraan])
            format_waktu = '{:02d}:{:02d}'.format(menit, detik)
            print(format_waktu, end='\r')
            time.sleep(1)
            durasi -= 1
        print("Lampu hijau berakhir!")
        

class EmergencySensor(SensorKota):
    def __init__(self, lokasi, sirine_emergency):
        super().__init__(lokasi)
        self.sirine_emergency = sirine_emergency

    def dapatkan_durasi(self):
        print(f'[EMERGENCY] Aktivasi lampu hijau darurat di {self.lokasi} dengan sirine {self.sirine_emergency}!')
        if self.sirine_emergency:
            return 90
        return 15
    
    def hitung_mundur(self, durasi):
        print(f'[EMERGENCY] Menghitung mundur durasi lampu hijau darurat selama {durasi} detik...')
        while durasi > 0:
            menit, detik = divmod(durasi, 60)
            format_waktu = '{:02d}:{:02d}'.format(menit, detik)
            print(format_waktu, end='\r')
            time.sleep(1)
            durasi -= 1 
        print("Lampu hijau berakhir! ")



daftar_sensor = [
    KameraSensor("Jl. Merdeka"),
    EmergencySensor("Jl. Sudirman", "Sirene 1"),
    EmergencySensor("Jl. Diponegoro", "Sirene 2")
]
print("--- SIMULASI INHERITANCE & POLYMORPHISM SMART CITY ---")
for sensor in daftar_sensor:
    sensor.cek_status_sensor()
    durasi = sensor.dapatkan_durasi()
    sensor.hitung_mundur(durasi)
    time.sleep(2)
    print("\n")
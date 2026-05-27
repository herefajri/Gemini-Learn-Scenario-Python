import random
import time

class radar:
    def __init__(self, id_radar, lokasi_radar):
        self.id_radar= id_radar
        self.lokasi_radar= lokasi_radar

    def pindai(self):
        print(f'[SYSTEM] {self.id_radar} sedang memindai di lokasi {self.lokasi_radar}')

class radar_militer(radar):
    def __init__(self, id_radar, lokasi_radar, jenis_radar, jangkauan_radar, misil):
        super().__init__(id_radar, lokasi_radar)
        self.jenis_radar = jenis_radar
        self.jangkauan_radar = jangkauan_radar
        self.misil = misil

    def deteksi_objek(self, objek, jarak_objek):
        if jarak_objek <= self.jangkauan_radar:
            print('=' * 50 + '\n Komputer Sistem Radar Militer \n' + '=' * 50)
            super().pindai()
            time.sleep(random.randint(5, 20))
            print(f'[ALERT] {self.id_radar} mendeteksi objek {objek} dalam jangkauan {self.jangkauan_radar} KM')

            while True:
                time_intersepsi = (6, 16) 
                system = input('Intersepsi target dengan sistem pertahanan? (y/n): ').lower().strip()
                if not system and not 'y' or not 'n':
                    print('[SYSTEM] Error, ulangi input Anda!')
                elif system == 'y':
                    print(f'[ACTION] {self.id_radar} mengaktifkan Sistem NASAMS untuk menghadapi objek {objek}')
                    time.sleep(5)
                    print(f'[SYSTEM] {self.misil} diluncurkan menuju target {objek}!')
                    time.sleep(random.randint(time_intersepsi[0], time_intersepsi[1]))
                    print(f'[RESULT] Target {objek} berhasil dihancurkan oleh {self.misil}!')
                    break
                elif system == 'n':
                    print(f'[SYSTEM] {self.id_radar} tidak mengintersepsi objek {objek}')
                    break
        else:
            super().pindai()
            print(f'[SYSTEM] {self.id_radar} memindai dalam jangkauan {self.jangkauan_radar}')

target = ('Drone Kamikaze Jarak Jauh', 'Jet Tempur', 'Drone Mata-Mata', 'Helikopter', 'Rudal Balistik', 'Rudal Jelajah')
jarak = (20, 50)
while True:
    radar1 = radar_militer('Radar-01', 'Pangkalan Udara', 'Radar Pertahanan Udara', random.randint(jarak[0], jarak[1]), 'AMRAAM ER')
    radar1.deteksi_objek(random.choice(target), random.randint(jarak[0], jarak[1]))
    continue_input = input('Kembali ke dasboard sensor radar? (y/n): ').lower().strip()
    if continue_input != 'y':
        print('Sistem dinonaktifkan.')
        break
    elif continue_input == 'y':
        print('Kembali ke dasboard sensor radar...')
        time.sleep(2)


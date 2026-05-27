class TraficLightAI:
    def __init__(self, lokasi, jumlah_kendaraan):
        self.lokasi = lokasi
        self.__jumlah_kendaraan = 0

    @property
    def jumlah_kendaraan(self):
        return self.__jumlah_kendaraan
    
    @jumlah_kendaraan.setter
    def jumlah_kendaraan(self, jumlah):
        if not isinstance(jumlah, int):
            raise ValueError('[SYSTEM] Error: Jumlah kendaraan harus berupa angka bulat!')
        elif jumlah < 0:
            raise ValueError('[SYSTEM] Error: Jumlah kendaraan tidak boleh negatif!')
        else:
            self.__jumlah_kendaraan=jumlah

    def hitung_durasi (self):
        if 0 <= self.__jumlah_kendaraan <= 10:
            return 15
        elif 11 <= self.__jumlah_kendaraan <= 29:
            return 30
        elif self.__jumlah_kendaraan >= 30:
            return 45

lampu_lalulintas = TraficLightAI('Persimpangan Jalan', 0)
while True:
    print(f'[SISTEM] Lokasi Lampu Lalulintas: {lampu_lalulintas.lokasi}')
    input_jumlah = input('[SISTEM] Input Jumlah Kendaraan yang Terpantau (ketik "Exit" untuk keluar dari Sistem): ').lower()
    if not input_jumlah and not input_jumlah.isdigit():
        print('[SISTEM] Sistem Tidak Menangkap Masukkan Anda, Ulangi Kembali')
        continue
    elif input_jumlah == 'exit':
        print('[SISTEM] Sistem Operasi Ditutup')
        break

    try:
        lampu_lalulintas.jumlah_kendaraan= int(input_jumlah)
        durasi_lampu  = lampu_lalulintas.hitung_durasi()
        print(f'[SISTEM] Durasi Lampu Hijau: {durasi_lampu} Detik')
    except ValueError as e:
        print(f'[SISTEM] Sistem Error: {e}')

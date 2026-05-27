class Siswa:
    def __init__(self, nama_input, nis_input, kelas_input):
        self.nama = nama_input
        self.nis = nis_input
        self.kelas = kelas_input
    
    def __str__(self):
        return f'nama: {self.nama}, nis: {self.nis}, kelas: {self.kelas}'

    def absen_masuk(self):
        print(f'{self.nama} dengan NIS {self.nis} berhasil absen masuk di kelas {self.kelas}')

siswa1= Siswa('Budi', '001', '12B')
siswa2= Siswa('Siti', '002', '12A') 
siswa3= Siswa('Andi', '003', '12C')

list_siswa = [siswa1, siswa2, siswa3]
for siswa in list_siswa:
    siswa.absen_masuk()
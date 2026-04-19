import unittest

# Ini class buatan lu (gue potong biar ringkas)
class DataNilai:
    def __init__(self):
        self.list_kosong = []
    def tambah_data(self, nilai_baru):
        self.list_kosong.append(nilai_baru)

# ==========================================
# AREA UJIAN 
# ==========================================
class TestDataNilaiLengkap(unittest.TestCase):

    # TUGAS 1: Apa nama fungsi buat "Persiapan" yang jalan duluan?
    def ________(self):
        self.kuiz = DataNilai()
        self.kuiz.tambah_data(100)
        print("Mulai: Data angka 100 dimasukkan.")

    # TUGAS 2: Lu mau mastiin kalau panjang list-nya sekarang adalah 1.
    # Pakai perintah apa buat mastiin itu sama?
    def test_cek_jumlah_data(self):
        jumlah = len(self.kuiz.list_kosong)
        self.________(jumlah, 1)

    # TUGAS 3: Apa nama fungsi buat "Beres-beres" yang jalan paling akhir?
    def ________(self):
        self.kuiz.list_kosong.clear() # Hapus semua isi list
        print("Selesai: Data dibersihkan ke tempat sampah.")

if __name__ == '__main__':
    unittest.main()
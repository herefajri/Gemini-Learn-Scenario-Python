import unittest

# 1. Ini class buatanmu tadi (Saya copy-paste utuh, nggak diubah)
class DataNilai:
    def __init__(self):
        self.list_kosong = []
    def tambah_data(self, nilai_baru):
        self.list_kosong.append(nilai_baru)
    def hitung_rata_rata(self):
        return sum(self.list_kosong) / len(self.list_kosong)
    def cari_nilai_tertinggi(self):
        return max(self.list_kosong)

# ==========================================
# 2. INI AREA UNITTEST (Robot Penguji)
# ==========================================
class TestDataNilai(unittest.TestCase): # Wajib pakai ini

    # A. setUp: Persiapan ujian (Dijalankan OTOMATIS sebelum tiap tes dimulai)
    def setUp(self):
        self.kuiz = DataNilai()
        self.kuiz.tambah_data(75)
        self.kuiz.tambah_data(80)
        self.kuiz.tambah_data(85)
        # Sekarang dompet datanya udah terisi [75, 80, 85]

    # B. Tes Ujian 1: Ngetes Rata-rata
    def test_rata_rata(self):
        hasil = self.kuiz.hitung_rata_rata()
        # assertEqual artinya: "Pastikan 'hasil' itu sama dengan 80.0"
        self.assertEqual(hasil, 80.0) 

    # C. Tes Ujian 2: Ngetes Nilai Tertinggi
    def test_nilai_tertinggi(self):
        hasil = self.kuiz.cari_nilai_tertinggi()
        # assertEqual artinya: "Pastikan 'hasil' itu sama dengan 85"
        self.assertEqual(hasil, 85)

# Perintah buat ngejalanin robot asistennya
if __name__ == '__main__':
    unittest.main()
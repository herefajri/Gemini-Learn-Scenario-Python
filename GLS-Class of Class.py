'''
Buat sebuah sistem untuk menampung dan menghitung nilai kuis kamu.

Buat class bernama DataNilai.

Di dalam __init__(self), buat sebuah variabel bernama kumpulan_angka yang isinya adalah List kosong ([]). (Ini tempat kita nyimpen datanya).

Buat fungsi tambah_data(self, nilai_baru). Tugasnya adalah memasukkan nilai_baru ke dalam list kumpulan_angka tadi. (Ingat materi awal Python tentang cara masukin barang ke dalam List? Pakai fungsi apa hayo?)

Buat fungsi hitung_rata_rata(self). Tugasnya adalah menghitung rata-rata dari semua angka yang ada di dalam kumpulan_angka, lalu me-return hasilnya.

Clue Logika: Rata-rata = Total semua angka dibagi jumlah datanya.

kuis_fajri = DataNilai()
kuis_fajri.tambah_data(75)
kuis_fajri.tambah_data(80)
kuis_fajri.tambah_data(85)
'''

class DataNilai:
    def __init__(self):
        self.list_kosong = []

    def tambah_data(self, nilai_baru):
        self.list_kosong.append(nilai_baru)
        return "Lapor List Terisi!"
    
    def hitung_rata_rata(self):
        total = sum(self.list_kosong)
        rata_rata = total / len(self.list_kosong)
        return rata_rata

    # TUGASMU: Bikin satu fungsi ini aja
    def cari_nilai_tertinggi(self):
        nilai_tertinggi = max(self.list_kosong)
        return nilai_tertinggi
        
kuiz_fajri = DataNilai()
kuiz_fajri.tambah_data(75)
kuiz_fajri.tambah_data(80)
kuiz_fajri.tambah_data(85)
kuiz_fajri.hitung_rata_rata()
print(kuiz_fajri.hitung_rata_rata())
kuiz_fajri.cari_nilai_tertinggi()
print(kuiz_fajri.cari_nilai_tertinggi())
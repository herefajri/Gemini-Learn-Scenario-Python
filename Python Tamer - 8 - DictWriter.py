import csv
import os # Penting untuk cek file ada atau tidak

def catat_absen(nama, id_karyawan):
    nama_file = 'kotak_absen.csv'
    kolom = ['nama_karyawan', 'id_karyawan']
    
    # LOGIKA: Cek apakah file sudah ada?
    file_baru = not os.path.isfile(nama_file)
    
    with open(nama_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=kolom)
        
        # TUGAS KAMU 1: 
        # Jika file_baru bernilai True, panggil fungsi untuk tulis header
        if file_baru == True:
            writer.writeheader()

        # TUGAS KAMU 2: 
        # Panggil writerow dengan format Dictionary sesuai 'kolom'
        writer.writerow({'nama_karyawan': nama, 'id_karyawan': id_karyawan})
        print('Data tersimpan')


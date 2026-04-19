from ast import main
import csv
import os

# --- 1. KOKI (FUNGSI PENULIS) ---
def catat_absen(nama, id_karyawan):
    nama_file = 'bank_absen.csv'
    kolom = ['nama_karyawan', 'id_karyawan']
    
    # TUGAS 1: Gunakan Si Mata-Mata untuk mengecek eksistensi file
    file_sudah_ada = os.path.isfile(nama_file)
    
    with open(nama_file, 'a', newline='') as file:
        # TUGAS 2: Panggil Si Formulir Rapi (DictWriter)
        writer = csv.DictWriter(file, fieldnames=kolom)
        
        # TUGAS 3: Logika Header
        # Jika file BELUM ada (file_sudah_ada bernilai False):
        # panggil writer.writeheader() di sini!
        if file_sudah_ada == False:
            print('File belum ada, menulis header...')
            writer.writeheader()
        
        # TUGAS 4: Tulis Data (Selalu dieksekusi)
        # Gunakan writer.writerow() dengan format Dictionary
        # Contoh: writer.writerow({'nama_karyawan': nama, 'id_karyawan': id_karyawan})
        pass # Hapus pass jika sudah diisi
        writer.writerow({'nama_karyawan' : nama, 'id_karyawan': id_karyawan})
        print('Data tersimpan')
    while True:
        input_nama = input('Masukkan nama karyawan: ').title().strip()
        if not input_nama:
            print('Nama karyawan tidak boleh kosong.')
            continue
        input_id = input('Masukkan ID karyawan: ').strip()
        if not input_id.isdigit():
            print('ID karyawan harus berupa angka.')
            continue
        if not input_id:
            print('ID karyawan tidak boleh kosong.')
            continue
        break
    while True:
        Tombol = input('Apakah Anda ingin mencatat absen lagi? (y/n): ').lower()
        if Tombol == 'y':
            continue
        elif Tombol == 'n':
            print('Terima kasih! Program selesai.')
            break
        else:
            print('Input tidak valid. Silakan masukkan "y" atau "n".')
            continue
    catat_absen(input_nama, input_id)
       
if __name__ == '__main__':
    main()
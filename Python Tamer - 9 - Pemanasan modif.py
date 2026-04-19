from ast import main
import csv
import os

def catat_absen(nama, id_karyawan):
    nama_file = 'bank_absen.csv'
    kolom = ['nama_karyawan', 'id_karyawan']

    file_sudah_ada = os.path.isfile(nama_file)
    
    with open(nama_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=kolom)
        if file_sudah_ada == False:
            print('File belum ada, menulis header...')
            writer.writeheader()

        writer.writerow({'nama_karyawan' : nama, 'id_karyawan': id_karyawan})
        print('Data tersimpan')

def main():
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

        catat_absen(input_nama, input_id)
   
        Tombol = input('Apakah Anda ingin mencatat absen lagi? (y/n): ').lower()
        if Tombol == 'y':
            continue
        elif Tombol == 'n':
            print('Terima kasih! Program selesai.')
            break
        else:
            print('Input tidak valid. Silakan masukkan "y" atau "n".')
            continue
    
       
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Menangkap error kalau user menekan Ctrl + C
        print('\nProgram dihentikan oleh pengguna. Terima kasih!')
    except PermissionError:
        # Menangkap error kalau file CSV sedang terkunci/dibuka
        print('\nTerjadi kesalahan: Tidak memiliki izin untuk menulis ke file. Pastikan file tidak sedang dibuka di aplikasi lain.')
    except Exception as e:
        # Jaring raksasa HARUS selalu di bawah!
        print(f'\nTerjadi kesalahan sistem yang tidak terduga: {e}')
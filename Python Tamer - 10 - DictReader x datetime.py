import csv
import os
from datetime import datetime

# --- 1. FUNGSI KOKI (Tulis Data) ---
def catat_absen(nama_karyawan, id_karyawan, waktu_absen):
    nama_file = 'bank_absen.csv'
    kolom = ['nama_karyawan', 'id_karyawan', 'waktu_absen']

    # 1. Cek apakah file sudah ada dengan os.path.isfile()
    file_sudah_ada = os.path.isfile(nama_file)
    with open(nama_file, 'a', newline='') as file:
        # 2. Buat objek DictWriter dengan fieldnames=kolom
        writer = csv.DictWriter(file, fieldnames=kolom)
        # 3. Jika file belum ada, tulis header dengan writer.writeheader()
        if not file_sudah_ada:
            print('File belum ada, menulis header...')
            writer.writeheader()
        # 4. Tulis data karyawan dengan writer.writerow() dalam format Dictionary
        writer.writerow({'nama_karyawan': nama_karyawan, 'id_karyawan': id_karyawan, 'waktu_absen': waktu_absen})
        print('Data tersimpan!') 

# --- 2. FUNGSI MANDOR (Baca Data) ---
def baca_absen():
    nama_file = 'bank_absen.csv'
    
    # 1. Buat blok try:
        # 2. Buka file pakai: with open(nama_file, mode='r') as file:
        # 3. Buat reader: reader = csv.DictReader(file)
        # 4. Print judul "=== DAFTAR ABSEN ==="
        # 5. Buat loop: for baris in reader:
            # 6. Ambil data: nama = baris['nama_karyawan']
            # 7. Ambil data: id_kary = baris['id_karyawan']
            # 8. Print ID dan Namanya ke layar
    try:
        with open('bank_absen.csv', mode = 'r') as file:
            reader = csv.DictReader(file)
            print("=== DAFTAR ABSEN ===")
            for baris in reader:
                nama = baris['nama_karyawan']
                id_kary = baris['id_karyawan']
                waktu_absen = baris['waktu_absen']
                print(f"Waktu Absen: {waktu_absen}, ID: {id_kary}, Nama: {nama}")

    # 9. Buat blok except FileNotFoundError:
        # 10. Print pesan "[Sistem] File belum ada!"
    except FileNotFoundError:
        print("[Sistem] File belum ada!")

# --- 3. FUNGSI PELAYAN (Menu UI) ---
def main():
    while True:
        # 1. Print tampilan menu: 1. Tambah, 2. Lihat, 3. Keluar
        # 2. Minta input user: pilihan = input("Pilih (1/2/3): ")
        print("Menu:" + "\n1. Tambah Absen" + "\n2. Lihat Absen" + "\n3. Keluar")
        pilihan = input("Pilih (1/2/3): ")

        # 3. Logika if pilihan == '1':
            # Pindahkan logika input Nama, ID, dan pemanggilan catat_absen() yang kemarin ke sini
        if pilihan == '1':
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
            catat_absen(input_nama, input_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif pilihan == '2':
            baca_absen()
        # 4. Logika elif pilihan == '2':
            # Panggil fungsi baca_absen() di sini
            
        # 5. Logika elif pilihan == '3':
            # Print pesan pamit, lalu break
        elif pilihan == '3':
            print('Terima kasih! Program selesai.')
            break
        # 6. Logika else:
            # Print pesan error "Pilihan tidak valid"
        else:
            print('Pilihan tidak valid. Silakan pilih 1, 2, atau 3.')
            continue

# --- 4. TOMBOL START ---
if __name__ == '__main__':
    # (Biarkan blok try/except airbag milikmu yang kemarin di sini)
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram dihentikan oleh pengguna. Terima kasih!')
    except PermissionError:
        print('\nTerjadi kesalahan: Tidak memiliki izin untuk menulis ke file. Pastikan file tidak sedang dibuka di aplikasi lain.')
    except Exception as e:
        print(f'\nTerjadi kesalahan sistem yang tidak terduga: {e}')
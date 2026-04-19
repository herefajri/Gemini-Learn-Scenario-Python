# ==========================================
# UJIAN AKHIR PYTHON DASAR: SISTEM ABSENSI SISWA
# ==========================================
# Modul yang dibutuhkan: csv, os, datetime
import csv
import os
from datetime import datetime
# --- [FUNGSI 1: TAMBAH SISWA] ---
# Task: 
# 1. Tangkap nama, nis, kelas, dan waktu_otomatis
# 2. Simpan ke data_siswa.csv (mode 'a')
# 3. Jangan lupa tulis header jika file baru dibuat
def tambah_siswa(nama_siswa, nis, kelas, waktu_absen):
    nama_file = 'data_siswa.csv'
    berkas_data = ['nama_siswa', 'nis', 'kelas', 'waktu_absen']
   
    eksistensi_file = os.path.isfile(nama_file)
    with open(nama_file, 'a', newline='') as berkas:
        writer = csv.DictWriter(berkas, fieldnames=berkas_data)
        if not eksistensi_file:
            print('File tidak ada/tidak dapat ditemukan...')
            writer.writeheader()
        writer.writerow({'nama_siswa': nama_siswa, 'nis': nis, 'kelas': kelas, 'waktu_absen': waktu_absen})
        print('Data berhasil disimpan!')


# --- [FUNGSI 2: LIHAT SEMUA] ---
# Task:
# 1. Baca file pakai DictReader
# 2. Looping dan print semua baris dengan format rapi
def baca_absen():
    try:
        with open('data_siswa.csv', mode='r') as file:
            reader= csv.DictReader(file)
            print('='*50 + f'\n {'DAFTAR ABSEN':^50}' + '\n' + '='*50)
            for baris in reader:
                nama = baris['nama_siswa']
                id_siswa = baris['nis']
                kelas = baris['kelas']
                waktu_absen= baris['waktu_absen']
                print(f'Waktu Absen: {waktu_absen}, ID: {id_siswa}, Nama: {nama}, Kelas: {kelas}')
    except FileNotFoundError:
        print('[Sistem] File belum ada!')

# --- [FUNGSI 3: CARI SISWA] ---
# Task:
# 1. Input NIS yang dicari
# 2. Pakai flag 'ketemu = False'
# 3. Jika ketemu, print datanya dan ubah flag jadi True
# 4. Jika sampai akhir loop tetap False, print "Siswa tidak ditemukan"
def cari_siswa():
    nama_file = 'data_siswa.csv'
    nis_target = input("Masukkan NIS Siswa yang dicari: ").strip()

    try:
        with open(nama_file, mode='r') as file:
            reader = csv.DictReader(file)
            ditemukan = False
            for baris in reader:
                if baris['nis'] == nis_target:
                    print(f'Waktu Absen: {baris['waktu_absen']}, ID: {baris['nis']}, Nama: {baris['nama_siswa']}, Kelas: {baris['kelas']}')
                    ditemukan = True
            if not ditemukan:
                print(f'[Sistem] Data siswa dengan ID {nis_target} tidak ditemukan!')
    except FileNotFoundError:
        print('[Sistem] File belum ada!')
# --- [FUNGSI 4: HAPUS ABSEN] ---
# Task:
# 1. Input NIS yang ingin dihapus
# 2. Baca file, masukkan semua data ke list KECUALI yang NIS-nya cocok
# 3. Tulis ulang file (mode 'w') dengan isi list baru tersebut
def hapus_absen():
    nama_file = 'data_siswa.csv'
    nis_target = input("Masukkan NIS Siswa yang dicari: ").strip()

    keranjang_data = []
    ditemukan = False
    try:
        with open(nama_file, mode='r') as file:
            reader = csv.DictReader(file)
            header= reader.fieldnames

            for baris in reader:
                if baris['nis'] != nis_target:
                    keranjang_data.append(baris)
                else:
                    ditemukan= True
        if ditemukan:
            with open(nama_file, mode='w', newline='') as files:
                writer= csv.DictWriter(files, fieldnames=header)
                writer.writeheader()
                writer.writerows(keranjang_data)
                print(f'[Sistem] Data dengan ID {nis_target} berhasil dihapus!')
        else: 
            print(f'[Sistem] Data dengan ID {nis_target} tidak ditemukan!')
    except FileNotFoundError:
        print(f'[Sistem] Data dengan ID {nis_target} belum ada!')


    
# --- [FUNGSI 5: MAIN MENU] ---
# Task:
# 1. Buat While True
# 2. Tampilkan Menu 1-5
# 3. Gunakan if-elif-else untuk memanggil fungsi di atas
# 4. Bungkus pemanggilan fungsi dengan try-except agar tidak crash jika ada error
def main():
    print('='*50 + '\n Selamat Datang''\n' + "="*50)
    while True:
        print('Silahkan pilih menu yang Anda tuju:'
            + '\n1. Absen Siswa'
            + '\n2. Lihat Semua Absen Siswa'
            + '\n3. Cari Siswa'
            + '\n4. Hapus Absen'
            + '\n5. Exit')
        pilihan = input('Masukkan pilihan Anda: ').strip()

        if pilihan == '1':
            while True:
                nama = input("Masukkan Nama Siswa: ").strip().title()
                if not nama:
                    print('Nama tidak boleh kosong!')
                    continue
                nis = input("Masukkan NIS Siswa: ").strip()
                if not nis.isdigit():
                    print('NIS harus berupa angka!')
                    continue
                elif not nis:
                    print('NIS tidak boleh kosong!')
                    continue
                kelas = input("Masukkan Kelas Siswa: ").strip().upper()
                if not kelas:
                    print('Kelas tidak boleh kosong!')
                    continue
                waktu_otomatis = datetime.now().strftime("%Y-%m-%d %H:%M")
                break
            tambah_siswa(nama, nis, kelas, waktu_otomatis)
        elif pilihan == '2':
            baca_absen()
        elif pilihan == '3':
            cari_siswa()
        elif pilihan == '4':
            hapus_absen()
        elif pilihan == '5':
            print('Terimakasih telah menggunakan sistem absensi ini!')
            break
        else:
            print('Pilihan tidak valid! Silahkan pilih antara 1-5.')
            continue

# --- [START ENGINE] ---
# Panggil fungsi main() di sini
if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
       print('\nProgram dihentikan oleh pengguna. Terimakasih!')
    except PermissionError:
       print('\n Terjadi kesalahan: Tidak memilki izin untuk menulis ke file. Pastikan file tidak sedang dibuka di aplikasi lain!')
    except Exception as e:
       print(f'\nTerjadi kesalahan sistem yang tak terduga: {e}')
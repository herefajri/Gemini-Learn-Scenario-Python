'''
Docstring for Gemini Learn Scenario - Python.Python Tamer - 6 - Brave or Arogant (Exam SImulation)
Input & Validasi (Hari 4):
- Minta Nama Karyawan. Tidak boleh kosong!
- Minta ID Karyawan. Harus berupa angka (.isdigit()).
Penyimpanan Permanen (Hari 3 & 5):
- Simpan data tersebut ke dalam file absensi.csv.
- Gunakan mode Append ('a').
- Data yang disimpan harus dalam format: ID, Nama, Waktu_Masuk.
- Tips: Untuk Waktu_Masuk, Anda boleh tulis manual saja "08:00" atau pakai string bebas dulu.
Logika Menampilkan Data (Hari 2 & 3):
- Buat menu: 1. Absen, 2. Lihat Daftar Hadir, 3. Keluar.
- Jika pilih menu 2, baca isi absensi.csv dan tampilkan dengan rapi.
Error Handling (Hari 5):
- Jika admin memilih menu 2 tapi file absensi.csv belum ada, jangan sampai program crash. Berikan pesan "Belum ada data".
'''

import csv

print("=== STARTUP ABSENCE SYSTEM ===")
print('Silahkan isi formulir dibawah sesuai dengan identitas Anda')
while True:
    nama = input('Masukkan nama Anda: ')
    if len(nama.strip().title()) > 0:
        break
    elif nama.isdigit():
        print("Nama tidak boleh berupa angka!")
        continue
    else:
        print("Nama tidak boleh kosong!")
        continue

while True:
    id_karyawan = input('ID Karyawan: ')
    if id_karyawan.strip().isdigit():
        break
    else:
        print("ID Karyawan harus berupa angka!")
        continue

# Petunjuk: Gunakan While True untuk menu utama
while True:
    print("\n=== STARTUP ABSENCE SYSTEM ===")
    print("1. Absen Sekarang")
    print("2. Lihat Daftar Hadir")
    print("3. Keluar")

    pilih = input("Pilih Menu (1/2/3): ")

    if pilih == "1":
        with open("absensi.csv", "a", newline="") as file:
            write= csv.writer(file)
            write.writerow([nama, id_karyawan])
            print('Data Tersimpan')
    elif pilih == "2":
        try:
            Cari_nama = input("Ketik nama yang ingin dicari: ").strip().title()
            pilih == 'r'
            with open('absensi.csv', 'r', newline='') as ngeread:
                show=csv.DictReader(ngeread)
            ditemukan = False
            for baris in show:
                if baris ['nama'] == Cari_nama:
                    print('Data Ditemukan: ')
                    print(f'\n Nama Karyawan: {baris["nama"]}\n ID Karyawan: {baris["id_karyawan"]}')
                    ditemukan = True
                    break
            if not ditemukan:
                print(f"Data {Cari_nama} tidak ditemukan.")
        except ValueError as e:
            print(f'Kesalahan: {e}')
            continue
    elif pilih == "3":
        print("Sistem Dimatikan...")
        break
    else:
        print("Menu tidak valid!")
        continue
'''
Docstring for Gemini Learn Scenario - Python.Python Tamer - 5 - Data Sanitization
Mari kita tingkatkan script input CSV Anda yang kemarin. Saya ingin Anda membuat sistem input yang cerewet. Dia tidak akan mau menyimpan data kalau datanya asal-asalan.
Tugas Anda:
Buatlah input untuk Nama Produk dan Jumlah Stok, dengan aturan:
- Nama Produk tidak boleh kosong. Jika kosong, tampilkan pesan error.
- Jumlah Stok harus berupa angka. Gunakan .isdigit() untuk mengeceknya. Jika user memasukkan huruf (misal: "sepuluh"), tolak!
- Format: Sebelum disimpan ke CSV, pastikan Nama Produk diubah menjadi format .title() (Huruf depan besar).

nama = input("Nama Produk: ").strip()
stok = input("Jumlah Stok: ").strip()

if not nama:
    print("❌ Nama tidak boleh kosong!")
elif not stok.isdigit():
    print("❌ Stok harus berupa angka bulat!")
else:
    # Baru di sini jalankan with open(...) dan csv.writer
    print(f"✅ Data {nama.title()} sebanyak {stok} berhasil divalidasi.")
'''
import csv

while True:
    try:
        nama = input("Masukkan Nama Produk: ").strip().title()
        stok = input('Jumlah Stok: ').strip()
        if not nama:
            print("❌ Nama tidak boleh kosong!")
            continue
        elif not stok.isdigit():
            print("❌ Stok harus berupa angka bulat!")
            continue
        else:
            break
    except ValueError as e:
        print(f'Kesalahan: {e}')
        continue

while True:
    try:
        print('Mode Pendataan: '\
              '\n1. Write (w) > Replace Another Data' \
              '\n2. Append (a) > Added a New Data' \
              '\n3. Read (r) > Reading All Data')
        mode = input('Input Mode Pendataan yang Anda Inginkan (w/a/r): ')
        if mode == '1' or mode == 'w'.lower():
            break
        elif mode == '2' or mode == 'a'.lower():
            break
        elif mode == '3' or mode == 'r'.lower():
            break
        else:
            print('Mode tidak valid. Silakan pilih 1, 2, atau 3.')
    except ValueError as e:
        print(f'Kesalahan: {e}')
        continue

if not nama:
    print('Input Kembali Nama Anda')
elif not  stok.isdigit():
    print('Harus Berupa Angka Bulat')
else:
    with open('Produk.csv', f'{mode}' ) as file:
        if mode == 'w' or mode == 'a':
            masukkan = csv.writer(file)
            masukkan.writerow([nama, stok])
        elif mode == 'r':
            baca = csv.reader(file)
            for row in baca:
                print(row)
        else:
            print('Mode tidak valid.')
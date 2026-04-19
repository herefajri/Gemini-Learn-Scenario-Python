print("=== SISTEM PENCATATAN KARYAWAN PERMANEN ===")
nama_karyawan = input("Masukkan nama karyawan: ")
while True:
    try:
        print('Divisi yang tersedia:' \
        '\n 1. Marketing' \
        '\n 2. Teknologi' \
        '\n 3. Keuangan')
        divisi = input("Masukkan divisi: ")
        if divisi == '1':
            divisi = 'Marketing'
            break
        elif divisi == '2':
            divisi = 'Teknologi'
            break
        elif divisi == '3':
            divisi = 'Keuangan'
            break
        else:
            raise ValueError("Divisi tidak valid")
    except ValueError as e:
        print(f"❌ Kesalahan: {e}")

# TUGAS ANDA: 
# Gunakan 'with open(...)' dengan mode 'a' untuk membuka/membuat file 'log_karyawan.txt'
# Lalu gunakan .write() untuk memasukkan format string: "[Nama] bergabung di divisi [Divisi]\n"
print('Fitur Data yang tersedia:' \
'\n 1. Write (w)' \
'\n 2. Append (a)' \
'\n 3. Read (r)')
while True:
    try:
        pilih_fitur = input('Pilih fitur (w/a/r): ')
        if pilih_fitur == '1' or pilih_fitur == 'w':
            pilih_fitur = 'w'
            break
        elif pilih_fitur == '2' or pilih_fitur == 'a':
            pilih_fitur = 'a'
            break
        elif pilih_fitur == '3' or pilih_fitur == 'r':
            pilih_fitur = 'r'
            break
        else:
            raise ValueError("Fitur tidak valid")
    except ValueError as e:
        print(f"❌ Kesalahan: {e}")

with open('log_karyawan.txt', f'{pilih_fitur}') as catatan:
    if pilih_fitur == 'w' or pilih_fitur == 'a':
        catatan.write(f'{nama_karyawan} bergabung di divisi {divisi}\n')
        print("✅ Data berhasil dikunci ke dalam hardisk!")
    else:
        keluarkan_data= catatan.read()
        print(keluarkan_data)
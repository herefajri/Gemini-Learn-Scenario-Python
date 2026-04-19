import csv

print("=== LAPORAN STOK GUDANG ===")

print('ID Barang' \
      '\n1. B001 = Monitor Lengkung' \
      '\n2. B002 = Meja Hidrolik' \
      '\n3. B003 = Kursi Ergonomis')
while True:
    try:
        ID_Barang= input("Masukkan ID Barang (1/2/3): ")
        if ID_Barang == '1':
            ID_Barang ='B001'
            Nama_Produk = 'Monitor Lengkung'
            break
        elif ID_Barang == '2':
            ID_Barang ='B002'
            Nama_Produk = 'Meja Hidrolik' 
            break
        elif ID_Barang == '3':
            ID_Barang ='B003'
            Nama_Produk = 'Kursi Ergonomis'
            break
        else:
            print("ID Barang tidak valid. Silakan coba lagi.")
            continue
    except ValueError as e:
        print(f'Kesalahan {e}')
        continue

Stok_Tersisa = input('Masukkan Sisa Stok: ')

data_baru = [{ID_Barang, Nama_Produk, Stok_Tersisa}]

print('Keterangan Mode Data:' \
      '\n1. Write (w)' \
      '\n2. Append (a)' \
      '\n3. Read (r)')
while True:
    try:
        mode = input('Pilih Mode Pendataan Anda:').lower()
        if mode == '1' or mode == 'w':
            mode = 'w'
            break
        elif mode == '2' or mode == 'a':
            mode = 'a'
            break
        elif mode == '3' or mode == 'r':
            mode = 'r'
            break
        else:
            print('Ada kesalahan pada penulisan/perintah Anda')
            continue
    except ValueError as e:
        print(f'Kesalahan {e}')
        continue

with open('laporan_gudang_copy.csv', f'{mode}', newline='') as file:
    if mode == 'w' or mode == 'a':
        masukkan = csv.writer(file)
        masukkan.writerow([ID_Barang, Nama_Produk, Stok_Tersisa])
        print('Data berhasil ditulis. Silahkan cek untuk mengonfirmasi.')
    elif mode == 'r':
        baca = csv.reader(file)
        for baris in baca:
            print(','.join(baris))
            print("=== LAPORAN STOK GUDANG ===")
    else:
        print("Mode tidak valid.")

'''
ID_Barang,Nama_Produk,Sisa_Stok
B001,Monitor Lengkung,12
B002,Meja Hidrolik,5
B003,Kursi Ergonomis,8


=== LAPORAN STOK GUDANG ===
Produk ID_Barang tersisa Sisa_Stok unit.
Produk Monitor Lengkung tersisa 12 unit.
Produk Meja Hidrolik tersisa 5 unit.
Produk Kursi Ergonomis tersisa 8 unit.
'''
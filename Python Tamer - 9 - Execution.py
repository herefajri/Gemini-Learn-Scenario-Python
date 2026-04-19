import os 

nama_file = 'kotak_absen.csv'
cek = os.path.isfile(nama_file)
print(f'Apakah file "{nama_file}" sudah ada? {cek}')

if cek:
    print('File sudah ada, siap untuk ditulis!')
else:
    print('File belum ada, akan dibuat saat penulisan data pertama kali!')
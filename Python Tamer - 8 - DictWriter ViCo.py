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
        if file_baru:
            writer.writeheader()

        # TUGAS KAMU 2: 
        # Panggil writerow dengan format Dictionary sesuai 'kolom'
        writer.writerow({'nama_karyawan': nama, 'id_karyawan': id_karyawan})
        print('Data Tersimpan!')

# --- 2. SI PEMBACA ---
def load_data():
    nama_file = 'kotak_absen.csv'
    if not os.path.isfile(nama_file):
        return []
    
    with open(nama_file, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)   
# --- 3. SI MANAJER ---
def main():
    while True:
        print("\n=== MESIN ABSENSI MANUAL ===")
        nama = input("Masukkan nama karyawan: ").strip().title()
        id_karyawan = input("Masukkan ID karyawan: ").strip()
        
        if not nama:
            print('Nama tidak boleh kosong, harap diisi!')
            continue
        if not id_karyawan.isdigit():
            print('ID harus berupa angka, harap diisi!')
            continue
        
        catat_absen(nama, id_karyawan)
        
        lagi = input('Apakah Anda ingin menambahkan data lagi? (y/n): ').strip().lower()
        if lagi == 'n':
            break
if __name__ == "__main__":
    main()  
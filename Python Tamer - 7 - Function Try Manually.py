import csv
'''
# --- 1. MEMBANGUN FUNGSI (MESINNYA) ---
def catat_absen(nama_karyawan, id_karyawan):
    # TUGAS 1: Buka file 'absensi.csv' dengan mode 'a' (append) dan newline=''
    # TUGAS 2: Buat objek csv.writer
    # TUGAS 3: Gunakan writerow() untuk memasukkan [nama_karyawan, id_karyawan]
    # TUGAS 4: Print pesan sukses (misal: "Data berhasil disimpan!")
    pass # Hapus kata 'pass' ini kalau Anda sudah menulis logikanya


# --- 2. MEMBANGUN UI & VALIDASI (KEMUDINYA) ---
while True:
    print("\n=== MESIN ABSENSI MANUAL ===")
    # TUGAS 5: Minta input nama. Buat validasi (while loop) agar nama tidak boleh kosong.
    # TUGAS 6: Minta input ID. Buat validasi agar ID harus angka (.isdigit()).
    # TUGAS 7: PANGGIL FUNGSI DI SINI!
    # Masukkan variabel nama dan ID yang sudah lolos validasi ke dalam fungsi catat_absen()
    # TUGAS 8: Tanya user apakah mau tambah data lagi? (y/n). Kalau 'n', break.
    break # Hapus break ini dan ganti dengan logika Anda
'''
# --- 1. MEMBANGUN FUNGSI (MESINNYA) ---
def catat_absen(nama_karyawan, id_karyawan):
    with open ('kotak_absen.csv', 'a', newline='') as file:
        baris_pokok = ['nama_karyawan', 'id_karyawan']
        writer= csv.writer(file)
        writer.writerow([nama_karyawan, id_karyawan])
        print('Data Tersimpan')

# --- 2. MEMBANGUN UI & VALIDASI (KEMUDINYA) ---
def main():
    while True:
        print("\n=== MESIN ABSENSI MANUAL ===")
        while True:
            nama = input("Masukkan nama karyawan: ").strip().title()
            if not nama:
                print('Nama tidak diperbolehkan kosong, harap diisi!')
                continue
            else:
                break

        while True:
            id_input = input('Masukkan ID: ').strip()
            if not id_input.isdigit():
                print('ID tidak diperbolehkan kosong, harap diisi!')
                continue
            else:
                break

        catat_absen(nama, id_input)

        lagi = input('Apakah Anda ingin menambahkan data lagi? (y/n): ').strip().lower()
        if lagi == 'y':
            continue
        elif lagi == 'n':
            break

if __name__ == "__main__":
    main()
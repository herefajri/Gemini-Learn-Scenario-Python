import csv

# --- 1. SI PEMBACA ---
def load_data():
    try:
        with open('absensi.csv', 'r') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

# --- 2. SI PENULIS ---
def save_data(nama, id_karyawan):
    file_kosong = False
    try:
        with open('absensi.csv', 'r') as f: pass
    except FileNotFoundError:
        file_kosong = True

    with open('absensi.csv', 'a', newline='') as f:
        fields = ['nama', 'id_karyawan']
        writer = csv.DictWriter(f, fieldnames=fields)
        if file_kosong:
            writer.writeheader()
        writer.writerow({'nama': nama, 'id_karyawan': id_karyawan})

# --- 3. SI MANAJER ---
def main():
    while True:
        print("\n=== SYSTEM V2.0 ===")
        print("1. Absen\n2. Lihat\n3. Keluar")
        pilih = input("Pilih: ")

        if pilih == '1':
            nama = input("Nama: ").title()
            idx = input("ID: ")
            save_data(nama, idx)
            print("Sip, data masuk!")

        elif pilih == '2':
            data = load_data()
            if not data:
                print("Belum ada data!")
            else:
                for orang in data:
                    print(f"[{orang['id_karyawan']}] {orang['nama']}")

        elif pilih == '3':
            print("Sistem dimatikan...")
            break

        elif pilih == '4':
            target = input("Masukkan ID Karyawan yang akan dipecat (dihapus): ")
            hapus_data(target)

        elif pilih == '5':
            print("Sistem dimatikan...")
            break

# --- 4. SI EKSEKUTOR (Hapus Data) ---
def hapus_data(target_id):
    # 1. Minta Si Pembaca mengambil semua data
    data_lama = load_data()
    
    if not data_lama:
        print("⚠️ Data kosong, tidak ada yang bisa dihapus.")
        return

    # 2. Siapkan mangkok baru
    data_baru = []
    terhapus = False

    # 3. Proses penyaringan
    for orang in data_lama:
        if orang['id_karyawan'] == target_id:
            # Jika ID cocok, abaikan (jangan dimasukkan ke mangkok baru)
            terhapus = True
            nama_terhapus = orang['nama']
        else:
            # Jika ID tidak cocok, selamatkan ke mangkok baru
            data_baru.append(orang)

    # 4. Timpa file lama dengan data dari mangkok baru
    if terhapus:
        # Perhatikan kita pakai mode 'w' (write / overwrite)
        with open('absensi.csv', 'w', newline='') as f:
            fields = ['nama', 'id_karyawan']
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader() # Tulis ulang judul kolom
            writer.writerows(data_baru) # Tulis SEMUA isi mangkok baru sekaligus
        
        print(f"🗑️ Data {nama_terhapus} (ID: {target_id}) telah dimusnahkan!")
    else:
        print(f"❌ Karyawan dengan ID {target_id} tidak ditemukan.")

# Jalankan Manajer-nya
if __name__ == "__main__":
    main()
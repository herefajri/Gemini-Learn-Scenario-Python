# 1. Kita buat lemari arsip kosong (Database simulasi)
database_karyawan = {}

# 2. Kita ubah fungsi registrasi_user
def registrasi_user(email, *akses, **profil):
    # Kemas semua data jadi satu paket utuh
    paket_data = {
        "email_login": email,
        "hak_akses": list(akses), # *args kita jadikan List
        "data_diri": profil       # **kwargs memang sudah berbentuk Dictionary
    }
    
    # Masukkan paket tersebut ke dalam lemari arsip, gunakan 'email' sebagai Kunci/Label foldernya
    database_karyawan[email] = paket_data
    print(f"✅ Akun {email} berhasil diamankan ke database!")

# --- PROSES REGISTRASI ---
Akun = input("Masukkan email akun: ").lower()

while True:
    try:
        print('Server yang ada: ' \
        '\n1. Server1,' \
        '\n2. Server2, ' \
        '\n3. Server3')
        Server = input("Masukkan nama server: ")
        if Server == "1":
            Server = "Server1"
            break
        elif Server == "2":
            Server = "Server2"
            break
        elif Server == "3":
            Server = "Server3"
            break
        else:
            print("❌ Nama server tidak boleh kosong!")
            continue
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

while True:
    try: 
        print('Database yang tersedia:' \
        '\n1. Database Utama,' \
        '\n2. Database Sekunder, ' \
        '\n3. Database Cadangan')
        Database = input("Masukkan nama database: ")
        if Database == '1':
            Database = "Database Utama"
            print(f"Database yang dimasukkan: {Database}")
            break
        elif Database == '2':
            Database = "Database Sekunder"
            print(f"Database yang dimasukkan: {Database}")
            break
        elif Database == '3':
            Database = "Database Cadangan"
            print(f"Database yang dimasukkan: {Database}")
            break
        else:
            print("❌ Nama database tidak boleh kosong!")
            continue
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

Nama = input("Masukkan nama lengkap: ")
if Nama:
    print(f"Nama yang dimasukkan: {Nama}")

while True:
    try:
        print('Divisi yang tersedia:' \
        '\n1. Divisi Frontend,' \
        '\n2. Divisi Backend, ' \
        '\n3. Divisi Mobile,' \
        '\n4. Divisi Data,' \
        '\n5. Divisi Data Science')
        Divisi = input("Masukkan divisi: ")
        if Divisi == "1":
            Divisi = "Divisi Frontend"
            break
        elif Divisi == "2":
            Divisi = "Divisi Backend"
            break
        elif Divisi == "3":
            Divisi = "Divisi Mobile"
            break
        elif Divisi == "4":
            Divisi = "Divisi Data"
            break
        elif Divisi == "5":
            Divisi = "Divisi Data Science"
            break
        else:
            print("❌ Nama divisi tidak boleh kosong!")
            continue
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

while True:
    try:
        print('Level yang tersedia:' \
        '\n1. Anak Magang,' \
        '\n2. Junior,' \
        '\n3. Senior')
        Level = input("Masukkan level: ")
        if Level == "1":
            Level = "Anak Magang"
            break
        elif Level == "2":
            Level = "Junior"
            break
        elif Level == "3":
            Level = "Senior"
            break
        else:
            print("❌ Pilihan level tidak valid!")
            continue
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")
        continue

registrasi_user(Akun, Server, Database, nama=Nama, divisi=Divisi, level=Level)

print("\n" + "="*40 + "\n")

# --- SKENARIO COWORKER MINTA DATA ---
# Coworker: "Bro, bagi data si Andi dong! Nih emailnya: andi@pt.com"

# Cara Anda memanggil datanya: Cukup buka lemari arsip, cari kunci "andi@pt.com"
data_si_andi = database_karyawan[Akun]

print("Ini data si Andi:")
print(data_si_andi)

# Bahkan coworker bisa minta spesifik divisinya saja:
print(f"\nDivisinya Andi adalah: {data_si_andi['data_diri']['divisi']}")
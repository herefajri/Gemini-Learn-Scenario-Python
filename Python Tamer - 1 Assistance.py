data_pelanggan = [
    {"nama": "Budi", "umur": 20, "email": "budi@gmail.com"}, 
    {"nama": "Siti", "umur": 17, "email": "siti_at_yahoo.com"}, 
    {"nama": "Agus", "umur": 25, "email": "agus@domain.id"},
    {"nama": "Joko", "umur": 30, "email": "jokotampan.com"}
]

def filter_pelanggan(daftar_pelanggan):
    pelanggan_valid = []
    pelanggan_invalid = []
    
    # Pythonic Way: Langsung ambil "pelanggan" dari "daftar_pelanggan"
    for pelanggan in daftar_pelanggan:
        
        # Logika diperbaiki: Menggunakan kondisi AND (keduanya harus terpenuhi)
        if pelanggan['umur'] >= 18 and "@" in pelanggan['email']:
            pelanggan_valid.append(pelanggan)
        else:
            # Jika salah satu syarat gagal, otomatis terlempar ke sini (Joko selamat!)
            pelanggan_invalid.append(pelanggan)
            
    return pelanggan_valid, pelanggan_invalid

# Menjalankan fungsi
valid, invalid = filter_pelanggan(data_pelanggan)

print("Berhasil! User Valid:", valid)
print("Ditolak! User Invalid:", invalid)
# TUGAS ANDA: Lengkapi fungsi ini dengan 3 jenis argumen (email, args untuk akses, kwargs untuk profil)
def registrasi_user(email, *akses , **profil):
    print(f"\nMemproses Akun: {email}")
    print("Hak Akses:")
    for jenis in akses:
        print(f'- {jenis}')
        
    print("Profil Lengkap:")
    for key, value in profil.items():
        print(f'{key}: {value}')

# Uji Coba (Jangan diubah):
registrasi_user("andi@pt.com", "Server 1", "Database Utama", nama="Andi Setiawan", divisi="Backend", level="Senior")
registrasi_user("budi_magang@pt.com", "Server Uji Coba", status="Aktif", kontrak="3 Bulan")
'''
Memproses Akun: andi@pt.com
Hak Akses:
- Server 1
- Database Utama
Profil Lengkap:
nama : Andi Setiawan
divisi : Backend
level : Senior

Memproses Akun: budi_magang@pt.com
Hak Akses:
- Server Uji Coba
Profil Lengkap:
status : Aktif
kontrak : 3 Bulan
'''
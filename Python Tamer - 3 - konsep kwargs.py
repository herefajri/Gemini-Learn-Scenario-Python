# TUGAS ANDA: Lengkapi fungsi di bawah ini
def cetak_id_card(**data):
    print("=== ID CARD KARYAWAN ===")
    for id, ket in data.items():
        print(f'{id}: {ket}')


# Uji Coba (Jangan diubah):
cetak_id_card(nama="Andi", divisi="Backend", level="Junior")
print("") # Jeda kosong
cetak_id_card(nama="Denis", divisi="Data Science", senjata="List Comprehension", streak=2)
'''
=== ID CARD KARYAWAN ===
nama : Andi
divisi : Backend
level : Junior

=== ID CARD KARYAWAN ===
nama : Denis
divisi : Data Science
senjata : List Comprehension
streak : 2
'''
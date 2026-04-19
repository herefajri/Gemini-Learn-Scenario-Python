# TUGAS ANDA: Lengkapi fungsi di bawah ini
def buat_tim(nama_divisi, *anggota):
    print(f"--- Tim {nama_divisi} ---")
    for orang in anggota:
        print(f"- {orang}")

# Uji Coba (Jangan diubah):
buat_tim("Backend", "Andi", "Budi", "Citra")
buat_tim("Frontend", "Denis", "Eka")
buat_tim("Keamanan (Solo)", "Fajri")
'''
--- Tim Backend ---
- Andi
- Budi
- Citra
--- Tim Frontend ---
- Denis
- Eka
--- Tim Keamanan (Solo) ---
- Fajri
'''
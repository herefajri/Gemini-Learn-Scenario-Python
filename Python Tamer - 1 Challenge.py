karyawan_mentah = [
    {"id": 101, "nama": "Andi", "divisi": "IT", "gaji": "5000000"}, 
    {"id": 102, "nama": "Budi", "divisi": "HR", "gaji": 4500000},    
    {"id": 103, "nama": "Citra", "divisi": "IT", "gaji": "6200000"}, 
    {"id": 104, "nama": "Denis", "divisi": "IT"}                     
]

total_gaji_it = 0

for karyawan in karyawan_mentah:
    if karyawan.get('divisi') == 'IT':
        gaji_mentah = karyawan.get('gaji', 0)
        total_gaji_it += int(gaji_mentah) if type(gaji_mentah) == str else gaji_mentah
        

print(f"Total gaji Divisi IT bulan ini adalah: Rp {total_gaji_it}")
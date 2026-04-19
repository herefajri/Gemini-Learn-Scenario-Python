'''
Docstring for Gemini Learn Scenario - Python.Python Tamer - 1 Challenge

Sebagai Pawang Sanca level menengah, Anda harus membuat skrip untuk menghitung total gaji divisi "IT". 
Tapi Anda dihadapkan pada dua jebakan mematikan:
- Jebakan Tipe Data (Type Casting): 
Python akan error jika Anda mencoba menjumlahkan angka (4500000) dengan teks ("5000000"). Anda harus mengubah teks menjadi angka.
- Jebakan Data Hilang (KeyError): 
Si Denis dari IT datanya corrupt. Dia tidak punya kunci (key) "gaji". Jika Anda memaksa memanggil karyawan["gaji"] pada Denis, 
program Anda akan meledak dan menampilkan pesan KeyError.
- Tugas Anda:
Tuliskan logika for loop untuk menghitung Total Gaji khusus Divisi IT.
Asumsi untuk Denis: Jika datanya tidak ada gaji, anggap saja gajinya 0 untuk sementara agar program tidak meledak.

Pertanyaan dari Pawang:
Apakah Anda tahu cara aman mengambil data dari Dictionary agar tidak meledak terkena KeyError saat data itu hilang? 
(Petunjuk: Jangan gunakan kurung siku [], gunakan sebuah metode khusus bawaan dictionary di Python).

Sambil Anda menyeduh kopi dan mulai coding, ingat tiga checkpoint mutlak ini agar program Anda tidak meledak saat dijalankan:
- Gatekeeper (Filter): Pastikan Anda hanya memproses karyawan yang memiliki divisi == "IT".
- Akses Aman (Anti-KeyError): Jangan gunakan kurung siku karyawan["gaji"] karena data si Denis akan membuat sistem crash. Silakan googling atau ingat-ingat cara kerja metode .get() pada Dictionary Python. Ini adalah pelampung penyelamat Anda.
- Konversi Tipe Data (Type Casting): Komputer tidak bisa menjumlahkan teks "5000000" dengan angka secara langsung. Anda harus mengubah teks tersebut menjadi integer (bilangan bulat) terlebih dahulu menggunakan fungsi int().

'''

karyawan_mentah = [
    {"id": 101, "nama": "Andi", "divisi": "IT", "gaji": "5000000"},  # Awas: Gaji dalam bentuk String (Teks)!
    {"id": 102, "nama": "Budi", "divisi": "HR", "gaji": 4500000},    # Ini normal (Integer)
    {"id": 103, "nama": "Citra", "divisi": "IT", "gaji": "6200000"}, # Awas: String!
    {"id": 104, "nama": "Denis", "divisi": "IT"}                     # BENCANA: Key "gaji" HILANG!
]

def bersih_data(karyawan):
    data_valid=[]
    data_rusak=[]

    while True:
            for tiap_karyawan in karyawan:
                try:
                    if tiap_karyawan ['id'] is int and tiap_karyawan ['nama'] is str and tiap_karyawan ['divisi'] is str and tiap_karyawan ['gaji'] is int:
                        data_valid.append(tiap_karyawan)
                    else:
                        data_rusak.append(tiap_karyawan)
                except (ValueError, KeyError, NameError):
                    data_rusak.append(tiap_karyawan)
            return data_valid, data_rusak

valid, non_valid= bersih_data(karyawan_mentah)
print(f'Data valid: {valid}')
print(f'Data tidak valid: {non_valid}')
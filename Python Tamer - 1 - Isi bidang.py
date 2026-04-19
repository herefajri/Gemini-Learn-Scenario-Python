data_pelanggan = [
    {"nama": "Budi", "umur": 20, "email": "budi@gmail.com"}, 
    {"nama": "Siti", "umur": 17, "email": "siti_at_yahoo.com"}, 
    {"nama": "Agus", "umur": 25, "email": "agus@domain.id"},
    {"nama": "Joko", "umur": 30, "email": "jokotampan.com"}
]

def cekPelanggan(d):
    A = []
    B = []
    for i in range(len(d)):
        if d[i]['umur'] >= 18:
            if "@" in d[i]['email']:
                A.append(d[i])
        else:
            B.append(d[i])
    print("User valid:", A)
    return A, B

hasil_valid, hasil_invalid = cekPelanggan(data_pelanggan)
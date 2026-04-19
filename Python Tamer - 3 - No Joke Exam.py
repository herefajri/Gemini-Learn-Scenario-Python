# TUGAS ANDA: Racik fungsi proses_checkout di sini
def proses_checkout(pembeli, *keranjang, **pengiriman):
    print(f"\n=== PESANAN MASUK: {pembeli} ===")
    
    # 1. Gunakan List Comprehension untuk mengkapitalisasi *keranjang
    troli = [barang.upper() for barang in keranjang]
    
    print("Daftar Belanjaan:")
    # 2. Tulis for loop untuk mencetak keranjang yang sudah dikapitalisasi
    for barang in troli:
        print(f'- {barang}')
    
    print("Detail Pengiriman:")
    # 3. Tulis for loop untuk membongkar **pengiriman
    for key, value in pengiriman.items():
        print(f'* {key}: {value}')


# ==========================================
# UJI COBA (JANGAN UBAH KODE DI BAWAH INI)
# ==========================================

proses_checkout(
    "Bapak Budi", 
    "laptop asus", "mouse wireless", "keyboard mekanik", 
    kurir="SiCepat", layanan="Next Day", asuransi="Ya"
)

proses_checkout(
    "Ibu Citra", 
    "panci set", "spatula", 
    kurir="JNT", promo="Gratis Ongkir", catatan="Tolong dibungkus bubble wrap tebal!"
)
'''
=== PESANAN MASUK: Bapak Budi ===
Daftar Belanjaan:
- LAPTOP ASUS
- MOUSE WIRELESS
- KEYBOARD MEKANIK
Detail Pengiriman:
* kurir : SiCepat
* layanan : Next Day
* asuransi : Ya

=== PESANAN MASUK: Ibu Citra ===
Daftar Belanjaan:
- PANCI SET
- SPATULA
Detail Pengiriman:
* kurir : JNT
* promo : Gratis Ongkir
* catatan : Tolong dibungkus bubble wrap tebal!

'''
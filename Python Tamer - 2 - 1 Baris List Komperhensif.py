email_mentah = ["Andi@gmail.com", "budi_salah_ketik.com", "CITRA@KANTOR.CO.ID", "denis_tanpa_email"]

# TUGAS ANDA: Buat variabel 'email_bersih' menggunakan 1 BARIS List Comprehension
email_bersih = [var.lower() for var in email_mentah if '@' in var]

print(email_bersih)
# OUTPUT TARGET: ['andi@gmail.com', 'citra@kantor.co.id']

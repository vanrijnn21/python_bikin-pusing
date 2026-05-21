print("Materi if dan loop")
umur = 20
if 18 <= umur <= 25: #python nagsih ijin buat nulis pendek
    print("gen Z")
# IF 
# Cara lama — panjang, lelah
status = "gak aktif"
if status == "aktif":
    print("lagi jalan")
elif status == "nonaktif":
    print("mati")
elif status == "pending":
    print("nunggu")
else:
    print("gak dikenal")
print("-----MATCH AND CASE---------")
 # cara baru - dan lebih efisien
match status:
    case "aktif":
        print("lagi jalan")
    case "nonaktif":
        print("meninggal")
    case "pending":
        print("nunggu")
    case _:
        print("gak dikenal")
# lIST COMPREHENSION
angka = [1,2,3,4,5] #lu punya list angka genap dan dikali dua ( input nya )

#cara lama - kepanjangan 
hasil = []
for n in angka:
    if n % 2 == 0:
        hasil.append(n * 2)
print(hasil)

#cara baru dalam satu baris 
hasil = [n * 2 for n in angka if n % 2 ==0]
print(hasil)
# 4. Dict Comprehension
# sama kayak list tapi pake kurung kurawal ditambah key:value
kuadrat = {n: n**2 for n in range(1, 6)}
print(kuadrat)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Zip - ngegabungin 2 list jadi pasangan 
nama = ["Edi","Edott","edoyy"]
nilai = [70,80,90] #v menggabungkan nama dan nilai n dan v mewakili masing"
hasil = {} # menggunakan dict biasa 
for n ,v in zip(nama,nilai):
    if v >=80:# bersyarat 
        hasil[n] = v
print(hasil)
# gabungan Zip dengan dict Comprehension 
hasil = { n : v for n,v in zip(nama,nilai)if v >= 80}
print(hasil)


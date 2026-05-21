print("hello world")
#latihan 1 - F - String Dan Variabel
print("------f - string dan variabel-------")
harga = 8500000
diskon = 0.15
nominal_diskon = harga * diskon # mencari nominal diskon 
harga_akhir = harga - nominal_diskon # mencari harga akhir setelah di diskon 
print(f"Harga Asli : {harga}")# gubakan f string untuk memudahkan akses variabel
print(f"Diskon 15% :{nominal_diskon}")#
print(f"Harga Akhir : {harga_akhir}")
# latihan 2 -  String
kalimat = " Belajar Python Itu Menyenangkan"
print(kalimat.strip())#menghilangkan spasii
print(kalimat.lower())# mengihlangkan semua huruf kapital
print("python" in kalimat)# mengecek apakah ada kalimat python di dalam "  kalimat "
print("Python" in kalimat)
print(kalimat.split())# untuk memisahkan antar kata 
# latihan ke - 3
print("----LATIHAN KE 3-------")
users = [
    {"nama" : "Adi","umur":25,"premium" : True},#jangan lupa koma nya 
    {"nama" : "Budi","umur":17,"premium" : False},
    {"nama" : "Cika","umur":30,"premium" : True},
    {"nama" : "Doni","umur":15,"premium" : False}
]# materi loop dan kondisi
for i in users:
    print(i["nama"])# menulis semua nama 
for i in users: # untuk memunculkan nama yang umurnya >= 18
    if i ["umur"] >= 18:
        print(i["nama"])
for i in users: # unutk memunculkan nama yang premium
    if i ["premium"] == True:# kondisi boolean 
        print(i["nama"])
# latihan 4 - kondisi kompleks 
# 
print("--------LATIHAN KE 4--------")
nilai = 87
kehadiran = 65
if nilai >= 75 and kehadiran >= 75: # kondisi dua-dua nya benar = bernilai benar 
    print(f"Status : lulus - nilai dan kehadiran mantapp")
elif nilai >= 75 and kehadiran < 75 or nilai < 75 and kehadiran >= 75:#gabungin and dan or 
    print(f"Status :Remedi - nilai oke tapi kehadiran kurang ")# or bernilia benar jika kondisi salah satu benar
else:
    print(f"Status : Gagal - nilai {nilai} dan kehadiran {kehadiran} sama-sama kurang ")
#latihan 4 - Loop Segitiga 
print("------LOOP SEGITIGA--------")
for i in range(1,6):# melakukan perulangan dari 1 - 5 
    print("*" * i)#melakukan pembuatan segitiga 
# latihan ke 6 - Dict , list dan loop
nama = ["adi","budi","cika","doni","eva"]
skor = [88,45,92,67,55]
hasil = {n : v for n  , v in zip (nama,skor) if v >= 70}
print(hasil)#gunakan zip untuk menggabungkan 2 list dan memunculkan nama yang skor nya >= 70
# n = mewakili nama dan v mewakili skor 
hasil2 = {n: v  for n , v in zip(nama,skor)}
print(hasil2) # untuk memunculkan semua user
hasil3 = {n: "lulus" if v >= 70 else "gagal" for n, v in zip(nama, skor)}

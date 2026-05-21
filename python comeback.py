print("balik lagi ke habitat")
nama = "Edi" #string
umur = 17 # integer
tinggi = 170.5 # float 
student = True # boolean 

print(nama,umur) #output : edi , 17 
print("---------------Tipe data---------------------")
#1 - String - teks 
s = "Hello AI Engineer "
print(s.upper())# buat nge capslock semua huruf nya 
print(s[0:5])# pilihan huruf 
print(len(s)) # jumlah kata yag tesedia 
#2 - integer & float - angka
print("------------------------------------")
a = 10 
b = 3 
# + = tambah 
# - = pengurangan 
# * = perkalian 
# / = pembagian 
print(a // b) #pembagian 
print(a % b) #mod
print(a ** b) #pangkat
#3List
print("---------------------------------------------")
buah = ["mangga","apel","strawberry"]
print(buah[1])#pakai kurung siku 
#4 - Dictionary - key:value
print("-----------------------------------------")
profil = {
    "nama": "Budi", # note = jangan lupa memakai koma
    "skill": "Python",
    "level": 1
}
print(profil["nama"])
profil["level"] = 3 #upgrade data 
print(profil["level"])
print("----------kondisi-----------------")
umur = 40
if umur >= 35: # waib menjorok kedalam 
    print("Senior kepala tiga")
elif umur >= 25:
    print("Gen - Millenial")
elif umur >= 16:
    print("Lu Gen-Z")
else: # selain nya
    print("masih Bocah ingusan")

 # Operator kondisi yang sering kepake
# ==  sama dengan
# !=  tidak sama
# and, or, not 
 # and jika kondisi dua" nya benar maka bernilai benar
 # or jika kondisi salah satu benar maka bernilai benar
 # not berkebailkan 
x = 15
if x > 10 and x < 20:
    print("antara 10 dan 20")

# Ternary (satu baris)
status = "tua" if umur >= 30 else "Muda"
print(status)
# materi pengulangan 
print("----------Loop--------------")
# for - iterasi atas sesuatu yang bisa dihitung 
buah = ["mangga","apel","strawberry"]
for b in buah:
    print(b) # mendeklarasi kan semuanya 
#range - untuk buat angka yang berurutan 
for i in range(5):# mendeklarasikan angka 0 sampai yang ditentukan 
    print(i)
for i in range(1,6):
    print(i)
# enumerate — dapat index( keterangan urutan) sekaligus
for idx, b in enumerate(buah):
    print(idx, b) 
# while - melakukan pengulangan selama kondisi true 
j = 0
while j < 5:
    print(j)
    j += 1 # wajib pakai ini , kalau enggak bakal infinite loop
# break and Continue - berhenti dan lanjutkan 
for i in range (10):# break dan continue memakai if 
    if i == 3 : continue # angka 3 nya di - skip 
    if i == 7 : break # sebek=lum angka 7 berhenti
    print(i)




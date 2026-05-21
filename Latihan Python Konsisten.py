print("----Latihan Python------")
nama = "Risky"
jumlah_anggota = 3
aktif = True#pakai f string untuk mendeklarisikan variabel lebih mudah
print(f"Nama tim: {nama}, Anggota: {jumlah_anggota}, Aktif: {aktif}")
# latihan - 2
kalimat = "saya mau jadi ai engineer"
print(kalimat[0])#memunculkan huruf pertama
print(kalimat[-1])#memunculkan huruf terakhir , python ngaish index negatif - 1 , bisa itung dari depan juga 
print(kalimat.upper())# mengubahnya menjadi capslock semua
print(len(kalimat))# menghitung jumlah kalimat yang tersedia 
hasil = kalimat.replace("saya","Edoyy")#mengganti kalimat lama dengan kalimat yang baru
print(hasil)
#latihan - 3 dict = key:value
inventory = {#dict memakai kurung kurawal bukan kurung siku
    "harta_karun":2,#jangan lupa memakai koma 
    "pedang":3,
    "sarung":1
}#get untuk mengetahui value tersedia di dalemnya
print(inventory.get("harta_karun",0))#jangan lupa tambahin default value = 0
print(inventory.get("harta_karun",0))#jangan lupa tambahin default value = 0
# latihan - 4 Dict lagiiii
mahasiswa = {
    "nama":"Edoyyy",
    "jurusan":"Ilmu komputer",
    "ipk":3.5,
    "status":"aktif"
}
mahasiswa["ipk"] = 3.8
print(mahasiswa["ipk"])
for n, i in mahasiswa.items():# menguunakan item loop kry & value dari dict 
    print(f"{n}:{i}")#items itu ngasih key:value sekaligus tiap iterasi
# latihan ke 5 - Kondisi 
jam = 19
if 5 <= jam <= 11:# cara bacanya : jika waktu diantara jam 5 dan 11 maka....
    print("pagi")
elif 12 <= jam <= 14:
    print("Siang")
elif 15 <= jam <= 17:
    print("Sore")
elif 18 <= jam <= 23:
    print("Malam")
else:# selainnya 
    print("dini hari")
# latihan ke 6 - Kondisi
ujian = [45,78,90,55,88,62,91]# pake list - loop - familykondisi
for i in ujian:
    print(i)#pake loop i sampai seterusnya 
    if i >= 75:# jika nilai diatas 75
        print("lulus")
    elif 60 <= i <= 74:# nilai diantara 60 - 74       
        print("Remedi")
    elif i < 60:#nilai 60 kebawah 
        print("Gagal")
    else:# nilai anomalii 
        print("selainnya")
# latihan ke 7 - Loop
for i in range(1, 51):# ememunculkan angka 1 - 50
    if i % 7 == 0:#angka yang habis idbagi 7 
        continue# maka akan di skip 
    print(i)# memunculkan semua angka
# latihan ke 8 - enumarated 
kata = ["python","adalah","bahasa","yang","keren"]
for idx , k in enumerate(kata , 1):#digunakan untuk memeunculkan sekaligus index 
    print(f"{idx}:{k}")#pakai f string untuk mendeklarasikan v 
# latihan ke 9 - Comprehension dan Zip(gabungan list)
produk = ["laptop","hp","kulkas","monitor"]# mewakili n = produk
harga = [100000,75000,50000,25000]# mewakili v = angka
hasil = {n : v for n , v in zip(produk,harga) if v >= 50000}#gunakan zip untuk menggabungkan 2 list 
print(hasil)
# latihan ke 10 - List and Loop
angka = [3,7,12,5,18,21,4,9,15]
hasil = [ n ** 2 for n in angka if n % 3 == 0]# pakai list agar urutan terjaga
print(hasil) # yang keluar hanya nagka yang habis dibagi oleh 3

        
    


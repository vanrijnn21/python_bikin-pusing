
print("hello world")
print("---String Manipulation-----")
kalimat = " halo,nama saya adalah AI Engineer "
print(kalimat.title())#tiap kata huruf pertama kapital
print(kalimat.count("a"))#menghitung jumlah huruf a 
kata = kalimat.split()#pecah menjadi list kata per kata 
kata.reverse()#balik urutannya 
hasil = " ".join(kata)# gabungin lagi menjadi string
print(hasil)
# latihan 2 

print("-----Latihan 2-------")
transaksi = [
    {"item":"kopi","harga":25000,"qty":3},
    {"item":"roti","harga":15000,"qty":2},
    {"item":"susu","harga":18000,"qty":4},
]
for i in transaksi:# lakukan loop 
    total_item = i["harga"] * i["qty"] # di jadikan variabel terlebih dahulu
    print(f"{i['item']}: Rp {total_item:,}")# kalo dict list pakai kutip 1
total = 0 
for t in transaksi:
    total += t["harga"] * t["qty"]# lakukan loop 
print(f"Grand Total : Rp {total:,}") # diluar loop keitung semua 
mahal = max(transaksi, key=lambda t: t["harga"] * t["qty"])# karena transaksinya di dict jadi harus pake key=
print(f"Item paling mahal: {mahal['item']}")#lambda function mini satu baris - 
# contoh lambda = key=lambda t: t["harga"] * t["qty"]
# ringkasan max(transaksi,           → cari yang terbesar dari list transaksi
#    key=lambda t:        → berdasarkan... untuk tiap dict t #   t["harga"]*t["qty"]) → hasil kali harga dan qty nya
# latihan 3 - nested loop 
for i in range(1,6): #buat baris 
    for j in range(1,6):# buat kolom
        print(i * j , end=" ") # lakukan operator perkalian - pakai end untuk tidak newline
    print() # - baris baru 
# latihan 4 - dict 
data = [
    {"nama": "Edi", "nilai": [80, 90, 70]},
    {"nama": "Ujong", "nilai": [60, 55, 75]},
    {"nama": "Kia", "nilai": [90, 95, 100]},
    {"nama": "Amba", "nilai": [40, 50, 45]},
]
# rata-rata nilai satu orang
# rata = sum(d["nilai"]) / len(d["nilai"])
# bikin dict comprehension-nya = 
hasil = {d["nama"]: sum(d["nilai"]) / len(d["nilai"]) for d in data}
print(hasil)
'''penjelasan nya : 
pakai dict = hasil -> loop ( nama ) : lalu program akan melalukan sum ( penjumalahan all)
lalu - program akan melakukan len yaitu menghitung jumlah elemen  , lalau program akan melakukan loop - 
for d ( d -> merujuk pada d yang ebrada di nama , sum nilai , dan len nilai)- in ( dalam ) - data ( kita punya dict)'''
lulus = [nama for nama, rata in hasil.items() if rata >= 70]# items : buat akses key  + value sekaligus 
print(lulus)
terbaik = max(hasil, key=lambda nama: hasil[nama])# pake lambda function mini
print(terbaik)# max (dict, key=lambda )
''' Data lo bentuknya dict?       → pake .items()
Data lo bentuknya dua list?   → pake zip()'''
# Latihan - 5 Dict 
chat = [
    {"role": "user", "content": "halo"},
    {"role": "assistant", "content": "halo juga!"},
    {"role": "user", "content": "cuaca hari ini gimana?"},
    {"role": "assistant", "content": "maaf saya tidak tahu cuaca"},
    {"role": "user", "content": "oke makasih"},
]
for i in chat:
    if i["role"] == "user":
        print(i["content"])

# penjelasan = 
''' kita akan memuculkan user nya saja , maka kita lakukan loop ( i ) in chat ( dict yang kita buat )
lalu setelah itu kita masukin ke if -> i ( loop ) - > role - disini kita hanya 
mengkhususkan - si user , lalu kita deklarasikan lewat print tapi yang di deklarasikan adalah 
content nya aja '''
jumlah = 0
for j in chat:
    if j["role"] == "user":
        jumlah += 1 
print(jumlah)
# penjelasan =
''' jumlah pertama 0 - lalu kita sama seperti tadi akan tetapi ketika setiap
bertemu dengan user(akan menambah 1) - lalu kita print'''
assistant_msgs = [i["content"] for i in chat if i["role"] == "assistant"]
print(assistant_msgs)
''' kita pake list satu baris disini logika nya sama kayak yang awal - cuma beda tipis'''
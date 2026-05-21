# while ( perulangan )

i = 1 
while i <= 10: # kurang dari sama dengan 10 
    print(i)
    i += 1 # dalam while wajib ada ini ( tambah )
print("---------------------------------------------")
#  while ( perunlangan ) - hitung mundur 
i = 10 
while i >= 1: # lebih dari sama dengan 1 
    print(i)
    i -= 1 # dikurang satu persatu 
print("------------------------------------------------")
i = 1 
total = 0 # nilai awal 
while i <= 5: 
    total  = total + i # cara kerjanya = 1 + 2 + 3 + 4 + 5 
    i += 1 
print(total) # hasil penjumlahan 
print("------------------------------------------------------")
i = 1 
while i <= 10: 
    if i % 2 == 0: # pake konsep mod ( jadi bilangan yang abis dibagi 2 doang yang terimput)
        print (i) # misalnya 4 di %(modulus) 2 = 0 jika 5 berarti sisa 1 
    i += 1
print("-----------------------------------------------------------------")
print("ini materi list") 
buah = ["apel","mangga","durian"]#kalo list itu pakai kurung siku 
print(buah[0])# deklarasi nya kayak gini 
print(buah[1])
print(buah[2])
buah.append("anggur") # append = penambahan data 
print(buah)
print(buah[3])
buah.remove("apel")
print(buah)
print("--------------------------------------------")
#ini materi dictionary 
data = {
    "nama":"edi", # set nya kayak gini 
    "umur": 17,
    "tinggi":170
}

print(data["nama"]) # deklarasi kayak ginii pake kurung kurawal 
print(data["umur"])
print(data["tinggi"])

user = {
    "username": "Edi",
    "password": "xixixi"
}

input_user = input("Username: ") #pake function 
input_pass = input("Password: ")

if input_user == user["username"] and input_pass == user["password"]:
    print("Login berhasil")
else:
    print("Login gagal")+
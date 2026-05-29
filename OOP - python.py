
import os # import os
print("hello world")
'''Class  = cetakan / blueprint
   Object = hasil cetakannya
Kayak:
Class  = cetakan kue
Object = kue-kuenya (bisa bikin banyak dari satu cetakan)
 - class NamaClass:                    # 1. deklarasi class, huruf kapital
    def __init__(self, parameter):      # 2. constructor — jalan pertama kali
        self.param = parameter          # 3. attribute — data yang disimpen

    def nama_method(self):          # 4. method — fungsi di dalam class
        return self.param
__init__  → function yang otomatis jalan waktu object dibuat
self      → merujuk ke object itu sendiri
attribute → variabel yang nyimpen data object (self.nama, self.hp)
method    → function yang bisa dilakuin object'''
class Karakter: # deklarasi class - huruf kapital
    def __init__(self , nama , hp , attack): #construktor - jalan pertama kali
        self.nama = nama # attritube = data yang disimpan 
        self.hp = hp
        self.attack = attack 

k1 = Karakter("edi",100,80) # isi dari karakter 
k2 = Karakter("edoy",200,80)
print(k1.hp)# deklarasi
print(k2.attack)
# Contoh oop = 

class Kucing:
    def __init__(self , nama , warna):
        self.nama = nama # attribute
        self.warna = warna # attribute 
    def suara(self): # method - function
        return (f"{self.nama} bilang ; Meoww!")
    def info(self): # method - function 
        return (f"{self.nama} warnanya {self.warna}")
    # objectnya :
kucing1 = Kucing("Mimi","Oranye")
kucing2 = Kucing("Tom","Hitam")

print(kucing1.suara())# kalo function pake buka - tutup kurung 
print(kucing2.nama)# akses attribute langsung 
# latihan oop
class Mahasiswa:
    def clear():
     os.system("cls" if os.name == "nt" else "clear")    # clear terminal 
    def __init__(self , nama , jurusan , ipk):
        self.nama = nama # attribute 
        self.jurusan = jurusan # attribute 
        self.ipk = ipk # attribute 
    def info(self): # pakai f string untuk deklarasi ulang 
        return(f"Nama : {self.nama} | Jurusan : {self.jurusan} | IPK : {self.ipk}")
    def lulus(self): # deklarasin pakai kondisii
        return self.ipk >= 3.0
    clear() # jalankan 
# object : 
m1 = Mahasiswa("edi","informatika",3.7)
m2 = Mahasiswa("mochii","keperawatan",3.4)
# deklarasi :

print(m1.info())
print(m2.lulus()) # langsung ke function - deklarasinya
print(m1.jurusan) # langsung ke attribute
# latihan OOP -
class RekeningBank:
    def __init__(self, nama , saldo):
        self.nama = nama # attribute
        self.saldo = saldo # attribute 
    def setor(self,jumlah):      #self.saldo = saldo yang tersimpan di object      
          self.saldo += jumlah   # jumlah = angka yang dikirim waktu manggil method dan += tambah ke saldo yang udah ada 
    def tarik(self , jumlah ):
        if self.saldo >= jumlah: # tarik saldo jika saldo mencukupi nominal
            self.saldo -= jumlah # jika saldo cukup maka akan dikurangi 
        else:
            print("saldo tidak cukup")# jika tidak maka akan langsung keluar ;
    def cek_saldo(self):
        print(f"Saldo : {self.saldo:,}")# :, = format angka ribuan 
# object : 
r1 = RekeningBank("edi",500000)
# deklarasi : 
r1.setor(200000)
r1.tarik(30000)
r1.cek_saldo() # deklarasi nya langsung tanpa print sebab tidak ada return 
print(r1.nama)
'''Kenapa pake self.saldo bukan saldo biasa?
python# saldo biasa — cuma ada di dalam function, hilang setelah selesai
def setor(self, jumlah):
    saldo = 500000   # ini lokal, gak nyambung ke object

# self.saldo — tersimpen di object, bisa diakses semua method
def setor(self, jumlah):
    self.saldo += jumlah   # ini yang beneran ngubah saldo object
self itu kayak penghubung antara method dan data yang tersimpen di object. Tanpa self, tiap method gak kenal satu sama lain.'''
# Inheritance ( Pewarisan ) =
# Class induk : 
class Karakter:
    def __init__(self,nama,hp):
        self.nama = nama
        self.hp = hp 
    def info(self):
        return (f"Nama : {self.nama} | HP : {self.hp}")
    # Anak anak - Class : 
class Warrior(Karakter):
    def __init__(self,nama,hp,weapon): # tambah parameter weapon
        super().__init__(nama,hp) # = > panggil __init__ = induk
        self.weapon = weapon # attribute weapon = tambahan 
    def skill(self):
        return (f"skill : {self.weapon}")

class Mage(Karakter):
    def __init__(self , nama , hp , spell):
        super().__init__(nama,hp)# => panggil __init__ = induk nya 
        self.spell = spell # attribute tambahan 
    def skill(self):
        return (f"skill : {self.spell}")
# object : 
w = Warrior("Edi",80,"Pedang")
m = Mage("Kia",100,"Fireball")
# deklarasi : 
print(w.info()) # Deklarasi tanpa buka / tutup kurung
print(m.info())# masuk ke function -> pake buka tutup kurung 
print(w.weapon)
print(m.spell)
# Error handling : 
try:
    angka = int("halo") # coba ini dulu
except ValueError:
    print("bukan angka!!") # kalau gagal , lakukan ini

print("program tetap jalan") # ini tetep kejalan
'''try:
    # "coba jalanin ini"
except NamaError:
    # "kalau error ini muncul, lakukan ini"
Sesimpel itu. try = coba. except = kalau gagal.
# 1. ValueError — tipe data salah
int("halo")        # string gak bisa jadi int

# 2. ZeroDivisionError — dibagi nol
10 / 0             # matematika gak boleh ini

# 3. KeyError — key dict gak ada
data = {"nama": "Edi"}
data["umur"]       # key "umur" gak exist'''
try:
    angka = int("halo")
except ValueError:
    print("bukan angka!")
# latihan error handling 
def konversi_float(nilai):
    try:
        return float(nilai) # angka yang desimal 
    except ValueError:
          return 0.0

print(konversi_float("3.14"))   # 3.14
print(konversi_float("halo"))   # 0.0 - program tetep berjalan walaupun value erroe - erroe handling
print(konversi_float("99"))     # 99.
# latihan 
def bagi(a, b):
    try:
        hasil = a / b
        return hasil                        # ← return kalau sukses
    except TypeError:
        return "Input harus angka!"         # ← pesan error 1
    except ZeroDivisionError:
        return "Gak bisa dibagi nol!"       # ← pesan error 2

print(bagi(10, 2))     # 5.0
print(bagi("a", 2))    # Input harus angka!
print(bagi(10, 0))     # Gak bisa dibagi nol!
# latihan 
def set_nilai(nilai):
    if nilai < 0:
        raise ValueError("Nilai Gak Boelh Negatif")
    if nilai > 100:
        raise ValueError("Nilai Gak Boleh Lebih dari 100")
    return nilai
try:
    print(set_nilai(86))
    print(set_nilai(-3))
    print(set_nilai(180))
except ValueError as e:
    print(f"Error : {e}")
'''except → satpam yang NANGKEP orang masuk
raise  → lo sendiri yang LEMPAR orang keluar'''
# latihan 
def ambil_data(data, key):
    try:
        return data[key]
    except KeyError:
        return "gak ada woii"
profil = {"Nama" : "Edi " , "Umur" : 22, "Kota":"Jakarta"}
print(ambil_data(profil, "Nama"))    # Edi
print(ambil_data(profil, "pencapaian"))   # data tidak ditemukan
print(ambil_data(profil, "Umur"))

    

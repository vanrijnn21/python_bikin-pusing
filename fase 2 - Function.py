print("hello world")
def rata_rata(nilai):
    return sum(nilai) / len(nilai)
print(rata_rata([80,90,84]))
print(rata_rata([90,88,78]))
# anatomi function 
'''def nama_function(parameter1, parameter2):
    # isi function
    return hasil --
    - penjelasan singkat nya - 
 def        → keyword wajib
nama       → bebas, snake_case
parameter  → input yang diterima, bisa kosong
return     → output yang dikembalikan'''
# latihan dasar - function 
def sapa(nama):
    return f"Halo , {nama}! selamat datang di python !!"# jangan lupa f string 
print(sapa("kia"))
print(sapa("edi"))
# function 3 - Multilple paarmeter + default value 
# Function bisa nerima lebih dari satu parameter
# Default value = nilai otomatis kalau parameter gak diisi

def perkenalan(nama, umur, kota="Jakarta"):  # kota punya default value
    return f"Nama: {nama}, Umur: {umur}, Kota: {kota}"

print(perkenalan("Edi", 22))              # kota otomatis "Jakarta"
print(perkenalan("Kia", 17, "Bandung"))   # kota diisi "Bandung"
# hitung belanjaan 
def hitung_belanja(harga,qty,diskon=0): # tiga parameter sekaligus
    total = harga * qty # pakai operator perkalian 
    diskon_nominal = total * diskon # pakai operator perkalian 
    hasil =  total - diskon_nominal # lalu dimasukin ke return dengan operator pengurangan 
    return f"Harga : {harga} , Qty : {qty}, Diskon : {diskon} , Total : Rp {int(hasil):,}" # lalu return seperti biasa 
# jangan lupa paai f string 

print(hitung_belanja(25000,3)) 
print(hitung_belanja(24000,3,0.2))# pakai desimal untuk diskon cnth = 0,2 = 20%
chat = [
    {"role": "user", "content": "halo"},
    {"role": "assistant", "content": "halo juga!"},
    {"role": "user", "content": "cuaca gimana?"},
    {"role": "assistant", "content": "gak tau cuaca"},
    {"role": "user", "content": "oke makasih"},
]

def analisis_chat(chat):# pake comprehension - 
    jumlah_user =len([c for c in chat if c["role"] =="user"])# buat deklarasi kan variabel ulang 
    jumlah_asst =len([c for c in chat if c["role"] =="assistant"]) # len ( mengitung jumlah )
    pesan_user = [c["content"] for c in chat if c["role"] == "user"]
    terakhir = pesan_user[-1]  # ambil yang terakhir - 1 , 
    return jumlah_user , jumlah_asst , terakhir 
user , asst , terakhir = analisis_chat(chat)#tiga variabel nerima 3 nilai sekaligus 
print(f"Pesan user      : {user}")# deklarasikan - return 
print(f"Pesan assistant : {asst}")
print(f"Pesan terakhir  : {terakhir}")
# argh - argumentasi tak terbatas 
def jumlah(*argh):
    return sum(argh) # sum = hitung jumlah semuanya 
print(jumlah(1,2,3)) #- > tuple
print(jumlah(1,2,3,4,5))
print(jumlah(5,6)) # lakukan deklarasi 
def coba2(**kwargh):
    print(kwargh) # -> dict fleksibel 
coba2(nama = "edi",umur=22)
# latihan argh - 
def total_belanja(*argh):  
    return sum(argh)# pakai sum untuk menghitung semuanya 
print(total_belanja(10000,25000,15000)) # deklarasikan
print(total_belanja(5000,8000))
print(total_belanja(10000,7000,9000,2000))
# latihan kwargh -
def buat_profil(**kwargs):
    for k, v in kwargs.items():# karena dict -> pake loop . items
        print(f"{k}: {v}")

buat_profil(nama="Edi", umur=22, hobby="ngoding")# deklarasikan 
#latihan - kwargh 
def biodata(**kwargs):
    for k , v in kwargs.items():
        if k =="umur":
            print(f":{k} : {v} tahun")
        else:
            print(f"{k} : {v}")
biodata(nama="edi",umur=22,kota="bogor",hobby="ngoding")
# latihan kwargh + parameter 
def log(level, **kwargs):
    info = " | ".join(f"{k}: {v}" for k, v in kwargs.items())
    print(f"[{level}] {info}")

log("INFO", nama="Edi", umur=22)
log("WARNING", error="file not found", line=42)
log("ERROR", message="server down")
'''kwargs.items() → dapet semua pasangan key:value
f"{k}: {v}"    → format tiap pasangan jadi string
" | ".join()   → gabungin semua string pake pemisah " | "
f"[{level}]"   → tambahin level di depan'''
#---latihan kwargs 
def buat_karakter(nama , **kwargs):
    print(f"---Karakter-----")# deklarikan ini terleboh dahulu
    print(f"Nama : {nama}")
    for k , v in kwargs.items():# masuk ke loop -> untuk deklarasi
        print(f"{k} : {v}")
buat_karakter("Edi",hp=100,attack=85,defense=70)
# args dan kwargs - 
def order(nama_resto , *args , **kwargs):
    print(f"---OUTPUT---")
    print(f"Resto : {nama_resto}")# deklarasikan pakai f string 
    print(f"Order : {",".join(args)}") # dipisah dengan join (,)
    print(f"Info : {" | ".join(f"{k} : {v}" for k , v in kwargs.items())}") # 
    '''f"{k}: {v}" for k, v in kwargs.items()  → bikin list string per pasangan
         " | ".join(...) → gabungin semua pake " | "'''
order("Warteg Bahagia", "nasi", "ayam", "es teh", alamat="Jl. Merdeka", catatan="pedas")
# deklarasi function







# Error Handling Python — Panduan Lengkap dari 0 sampai 100

---

## 1. Kenapa Error Handling Penting?

Tanpa error handling, program lo kayak mobil tanpa rem:

```python
# Tanpa error handling
data = {"nama": "Edi"}
print(data["umur"])      # KeyError 💀 program mati
print("ini gak kejalan") # baris ini gak pernah dieksekusi
```

Dengan error handling:
```python
try:
    print(data["umur"])
except KeyError:
    print("key gak ada!")
    
print("program tetap jalan")  # ini tetep kejalan ✅
```

---

## 2. Struktur Dasar

```python
try:
    # kode yang mungkin error
except NamaError:
    # kalau error itu muncul, lakukan ini
```

Cara bacanya:
```
try    → "coba jalanin ini"
except → "kalau error ini muncul, tangkep dan lakukan ini"
```

---

## 3. Alur Eksekusi

```python
try:
    print("step 1")    # ✅ jalan
    int("halo")        # ❌ error di sini
    print("step 2")    # ⛔ gak kejalan, langsung loncat ke except
except ValueError:
    print("step 3")    # ✅ jalan karena error ditangkep
    
print("step 4")        # ✅ jalan — program lanjut normal
```

Output:
```
step 1
step 3
step 4
```

---

## 4. Jenis-Jenis Error yang Sering Muncul

```python
# ValueError — tipe data gak sesuai
int("halo")            # string gak bisa jadi int
float("abc")           # sama

# ZeroDivisionError — dibagi nol
10 / 0
10 // 0

# KeyError — key dict gak ada
data = {"nama": "Edi"}
data["umur"]           # "umur" gak ada di dict

# IndexError — index list di luar jangkauan
buah = ["apel", "mangga"]
buah[5]                # index 5 gak ada

# TypeError — operasi di tipe data yang salah
"halo" + 123           # gak bisa gabungin string + int
len(123)               # len() gak bisa di angka

# AttributeError — attribute/method gak ada
"halo".terbang()       # string gak punya method terbang()

# FileNotFoundError — file gak ketemu
open("file_gak_ada.txt")
```

---

## 5. Tangkep Satu Error

```python
def bagi(a, b):
    try:
        hasil = a / b
        print(f"Hasil: {hasil}")
    except ZeroDivisionError:
        print("Gak bisa dibagi nol!")

bagi(10, 2)   # Hasil: 5.0
bagi(10, 0)   # Gak bisa dibagi nol!
```

---

## 6. Tangkep Banyak Error Sekaligus

```python
def konversi(nilai):
    try:
        hasil = int(nilai)
        print(f"Hasil: {hasil}")
    except ValueError:
        print("Bukan angka!")
    except TypeError:
        print("Tipe data salah!")

konversi("123")    # Hasil: 123
konversi("halo")   # Bukan angka!
konversi(None)     # Tipe data salah!
```

---

## 7. Tangkep Error Apapun (Generic)

```python
try:
    # kode yang mungkin error
    hasil = 10 / 0
except Exception as e:
    print(f"Ada error: {e}")
    # output: Ada error: division by zero
```

`Exception` = tangkep error apapun.
`as e` = simpen pesan errornya ke variabel `e`.

---

## 8. `else` — Jalan Kalau Gak Ada Error

```python
try:
    angka = int("123")
except ValueError:
    print("Bukan angka!")
else:
    print(f"Berhasil convert: {angka}")  # jalan kalau try sukses
```

```
try     → coba
except  → kalau gagal
else    → kalau berhasil
```

---

## 9. `finally` — Selalu Jalan Apapun

```python
def buka_file(nama_file):
    try:
        f = open(nama_file)
        data = f.read()
    except FileNotFoundError:
        print("File gak ketemu!")
    finally:
        print("Selesai — selalu jalan")  # error atau gak, ini tetep jalan

buka_file("ada.txt")       # Selesai — selalu jalan
buka_file("gak_ada.txt")   # File gak ketemu! + Selesai — selalu jalan
```

Analogi: `finally` = cleaning service. Apapun yang terjadi di dapur, cleaning service tetep dateng beresin.

---

## 10. Struktur Lengkap

```python
try:
    # kode yang mungkin error
except ValueError:
    # tangkep ValueError
except ZeroDivisionError:
    # tangkep ZeroDivisionError
except Exception as e:
    # tangkep error apapun selain di atas
else:
    # jalan kalau try sukses tanpa error
finally:
    # selalu jalan apapun yang terjadi
```

---

## 11. `raise` — Lempar Error Sendiri

Kadang lo mau bikin error sendiri kalau kondisi gak sesuai:

```python
def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur gak boleh negatif!")
    if umur > 150:
        raise ValueError("Umur gak masuk akal!")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"Error: {e}")
# Error: Umur gak boleh negatif!
```

---

## 12. Custom Exception — Bikin Error Sendiri

```python
# Bikin class error sendiri
class SaldoKurang(Exception):
    pass

class RekeningBank:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def tarik(self, jumlah):
        if jumlah > self.saldo:
            raise SaldoKurang(f"Saldo kurang! Saldo lo cuma {self.saldo:,}")
        self.saldo -= jumlah

# Pakenya:
r = RekeningBank(500000)
try:
    r.tarik(1000000)
except SaldoKurang as e:
    print(f"Gagal: {e}")
# Gagal: Saldo kurang! Saldo lo cuma 500,000
```

---

## 13. Real World — AI Engineering

Lo bakal sering pake ini waktu manggil API:

```python
import requests

def panggil_ai(prompt):
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={"x-api-key": "your-key"},
            json={"prompt": prompt}
        )
        response.raise_for_status()  # raise error kalau status bukan 200
        return response.json()
        
    except requests.exceptions.ConnectionError:
        print("Gak ada koneksi internet!")
    except requests.exceptions.Timeout:
        print("Request timeout!")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error gak terduga: {e}")
    finally:
        print("Request selesai")
```

---

## 14. Ringkasan

```
try     → coba jalanin kode ini
except  → kalau error ini muncul, lakukan ini (bisa banyak)
else    → kalau try sukses tanpa error
finally → selalu jalan apapun yang terjadi
raise   → lempar error sendiri
```

---

## 15. Latihan

```python
# Soal 1 — basic
# Bikin function "konversi_int" yang nerima string
# Coba convert ke int, kalau gagal return 0

# Soal 2 — multiple except
# Bikin function "bagi" yang nerima dua angka
# Tangkep: ValueError (bukan angka) dan ZeroDivisionError (dibagi 0)

# Soal 3 — raise
# Bikin function "set_nilai" yang nerima nilai 0-100
# Kalau di luar range, raise ValueError dengan pesan yang jelas

# Soal 4 — real world
# Bikin function "ambil_data" yang nerima dict dan key
# Kalau key ada → return valuenya
# Kalau key gak ada → return "data tidak ditemukan"
# Pake try/except KeyError
```

---

*Simpan file ini, baca ulang kalau lupa, langsung praktek soalnya.*

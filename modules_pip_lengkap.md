# Modules & pip Python — Panduan Lengkap dari 0 sampai 100

---

## 1. Apa itu Module?

Module = file Python yang isinya kode yang bisa dipake di file lain.

Bayangin lo punya toko — daripada bikin semua barang sendiri, lo tinggal order dari supplier. Module itu suppliernya.

```python
# Tanpa module — harus nulis sendiri
def hitung_akar(x):
    # nulis algoritma akar dari nol... ribet 💀
    ...

# Dengan module — tinggal pake
import math
print(math.sqrt(16))   # 4.0 — langsung jalan
```

---

## 2. Tiga Jenis Module

```
1. Built-in   → udah ada di Python, tinggal import
2. Third-party → buatan orang lain, harus install dulu pake pip
3. Custom     → buatan lo sendiri
```

---

## 3. Built-in Modules — Udah Ada, Tinggal Import

### `math` — operasi matematika
```python
import math

print(math.sqrt(16))      # 4.0 — akar kuadrat
print(math.pi)            # 3.141592653589793
print(math.ceil(4.2))     # 5 — bulatkan ke atas
print(math.floor(4.8))    # 4 — bulatkan ke bawah
print(math.pow(2, 10))    # 1024.0 — 2 pangkat 10
print(math.log(100, 10))  # 2.0 — logaritma
```

### `random` — angka acak
```python
import random

print(random.randint(1, 10))        # angka random 1-10
print(random.choice(["a","b","c"])) # pilih random dari list
print(random.shuffle([1,2,3,4,5]))  # acak urutan list
print(random.random())              # float random 0.0 - 1.0
```

### `datetime` — tanggal dan waktu
```python
from datetime import datetime

sekarang = datetime.now()
print(sekarang)                           # 2026-05-17 20:20:00
print(sekarang.strftime("%d/%m/%Y"))      # 17/05/2026
print(sekarang.strftime("%H:%M:%S"))      # 20:20:00
print(sekarang.year)                      # 2026
print(sekarang.month)                     # 5
```

### `os` — interaksi dengan sistem operasi
```python
import os

print(os.getcwd())                        # direktori sekarang
print(os.listdir("."))                    # list file di direktori
os.makedirs("folder_baru", exist_ok=True) # bikin folder
os.system("cls" if os.name == "nt" else "clear")  # clear terminal
```

### `json` — baca/tulis JSON
```python
import json

# Dict → JSON string
data = {"nama": "Edi", "umur": 22}
json_str = json.dumps(data)
print(json_str)           # '{"nama": "Edi", "umur": 22}'

# JSON string → Dict
data_balik = json.loads(json_str)
print(data_balik["nama"]) # Edi

# Simpan ke file
with open("data.json", "w") as f:
    json.dump(data, f)

# Baca dari file
with open("data.json", "r") as f:
    data_dari_file = json.load(f)
```

### `sys` — interaksi dengan Python interpreter
```python
import sys

print(sys.version)          # versi Python
print(sys.platform)         # os yang dipake
sys.exit()                  # stop program
```

---

## 4. Cara Import

```python
# Import seluruh module
import math
math.sqrt(16)               # harus pake nama module

# Import spesifik — gak perlu nama module
from math import sqrt, pi
sqrt(16)                    # langsung pake
print(pi)

# Import semua — hindari ini, bikin kode susah dibaca
from math import *
sqrt(16)

# Import dengan alias — buat nama yang lebih pendek
import numpy as np          # konvensi standar
import pandas as pd         # konvensi standar
import matplotlib.pyplot as plt
```

---

## 5. pip — Package Manager Python

pip = tukang install library. Semua library third-party diinstall pake pip.

### Cara install
```bash
# Install library
pip install nama-library

# Install versi spesifik
pip install numpy==1.24.0

# Install beberapa sekaligus
pip install numpy pandas matplotlib

# Uninstall
pip uninstall nama-library

# Liat semua yang terinstall
pip list

# Cek versi
pip show numpy
```

### Library wajib AI Engineer
```bash
# Data science
pip install numpy
pip install pandas
pip install matplotlib

# AI / LLM
pip install openai
pip install anthropic
pip install langchain
pip install llama-index

# Web / API
pip install requests
pip install fastapi
pip install uvicorn

# Utility
pip install python-dotenv   # buat .env file
pip install tqdm            # progress bar
```

---

## 6. Virtual Environment — WAJIB dipake

Virtual env = ruangan terpisah buat tiap project. Biar library satu project gak bentrok sama project lain.

```bash
# Bikin virtual env
python -m venv nama_env

# Aktifin (Windows)
nama_env\Scripts\activate

# Aktifin (Mac/Linux)
source nama_env/bin/activate

# Matiin
deactivate
```

Tanda udah aktif — ada nama env di depan terminal:
```
(nama_env) C:\Users\...>
```

---

## 7. requirements.txt — Daftar Library Project

Biar orang lain bisa install semua library yang lo pake sekaligus:

```bash
# Generate dari library yang udah terinstall
pip freeze > requirements.txt

# Install semua dari requirements.txt
pip install -r requirements.txt
```

Isi `requirements.txt`:
```
numpy==1.24.0
pandas==2.0.0
openai==1.0.0
langchain==0.1.0
```

---

## 8. Bikin Module Sendiri

```python
# File: helper.py
def sapa(nama):
    return f"Halo, {nama}!"

def hitung_rata(nilai):
    return sum(nilai) / len(nilai)

VERSI = "1.0.0"
```

```python
# File: main.py — pake module helper
import helper

print(helper.sapa("Edi"))              # Halo, Edi!
print(helper.hitung_rata([80, 90]))    # 85.0
print(helper.VERSI)                    # 1.0.0

# Atau import spesifik
from helper import sapa, hitung_rata
print(sapa("Kia"))
```

---

## 9. `__name__` — Jalan Kalau Dipanggil Langsung

```python
# File: helper.py
def sapa(nama):
    return f"Halo, {nama}!"

# Kode di bawah ini HANYA jalan kalau helper.py dijalankan langsung
# Gak jalan kalau helper.py di-import dari file lain
if __name__ == "__main__":
    print(sapa("Edi"))
    print("ini cuma buat testing")
```

---

## 10. Real World — AI Engineering

```python
# .env file — simpen API key, JANGAN hardcode di kode
# OPENAI_API_KEY=sk-xxx
# ANTHROPIC_API_KEY=sk-ant-xxx

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load .env file
load_dotenv()

# Ambil API key dari environment
api_key = os.getenv("ANTHROPIC_API_KEY")

# Inisialisasi client
client = Anthropic(api_key=api_key)

# Panggil API
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Halo!"}
    ]
)

print(response.content[0].text)
```

---

## 11. Ringkasan

```
import math              → import seluruh module
from math import sqrt    → import spesifik
import numpy as np       → import dengan alias

pip install numpy        → install library
pip freeze > req.txt     → simpan daftar library
pip install -r req.txt   → install dari daftar

python -m venv env       → bikin virtual env
env\Scripts\activate     → aktifin virtual env
```

---

## 12. Latihan

```python
# Soal 1 — built-in module
# Import random, bikin function "tebak_angka" yang:
# - Generate angka random 1-10
# - Minta user input tebakan
# - Print "Benar!" atau "Salah! Jawabannya {angka}"

# Soal 2 — datetime
# Import datetime, bikin function "info_waktu" yang:
# - Print tanggal sekarang format: "17 Mei 2026"
# - Print jam sekarang format: "20:20:00"
# - Print hari apa sekarang (Senin, Selasa, dll)

# Soal 3 — json
# Bikin dict data_diri lo
# Simpen ke file "data.json"
# Baca lagi dari file, print semua isinya

# Soal 4 — custom module
# Bikin file "utils.py" berisi 3 function:
# - hitung_rata(nilai) → rata-rata list
# - cari_max(nilai) → nilai terbesar
# - cari_min(nilai) → nilai terkecil
# Import dan pake di file main.py
```

---

*Simpan file ini, baca ulang kalau lupa, langsung praktek soalnya.*

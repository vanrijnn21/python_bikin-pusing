
## Author
Risky Edi Setiawan

# 🐍 Python → AI Engineer Roadmap

> Dokumentasi perjalanan belajar Python dari nol sampai siap jadi AI Engineer.
> Konsisten > Pinter. Dikit-dikit, lama-lama bukit.

---

## 📊 Progress

| Fase | Materi | Status |
|------|--------|--------|
| Fase 1 | Python Dasar |  Selesai |
| Fase 2 | Python Menengah | Selesai |
| Fase 3 | Library AI Wajib | ⏳ Belum mulai |
| Fase 4 | Dunia AI Beneran | ⏳ Belum mulai |
| Target | Junior AI Engineer | 🎯 Goal |

---

## 🗺️ Roadmap Lengkap

### ✅ Fase 1 — Python Dasar (Selesai)

**Materi yang dikuasai:**

- **Variabel & Tipe Data**
  - String, integer, float, boolean
  - F-string dan string formatting `{:,}`
  - String methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`, `.count()`, `.title()`
  - String indexing: `[0]`, `[-1]`, `[start:end]`

- **List & Dict**
  - Bikin, akses, update, hapus
  - `.get()` dengan default value
  - `.items()`, `.keys()`, `.values()`
  - List of dict (format API response)

- **Kondisi**
  - `if`, `elif`, `else`
  - Chained comparison: `18 <= umur <= 25`
  - Operator: `and`, `or`, `not`
  - Ternary: `"lulus" if nilai >= 75 else "gagal"`
  - `match-case` (Python 3.10+)

- **Loop**
  - `for` loop, `while` loop
  - `range()`, `enumerate()`, `zip()`
  - `break`, `continue`
  - Nested loop

- **Comprehension**
  - List comprehension: `[x for x in list if kondisi]`
  - Dict comprehension: `{k: v for k, v in zip(a, b)}`
  - Kombinasi `zip()` + comprehension + filter

- **Lambda**
  - Function mini satu baris
  - Penggunaan dengan `max()`, `min()`, `sorted()`

---

### (Selesai ) Fase 2 — Python Menengah (Sedang Berjalan)

-  **Function**
  - `def`, parameter, `return`
  - Default parameter
  - `*args` dan `**kwargs`
  - Scope: local vs global

-  **OOP (Object Oriented Programming)**
  - Class dan object
  - `__init__`, method, attribute
  - Inheritance
  - `super()`

-  **Error Handling**
  - `try`, `except`, `finally`
  - Custom exception
  - Common errors: `TypeError`, `KeyError`, `ValueError`

-  **Modules & Packages**
  - `import`, `from ... import`
  - Bikin module sendiri
  - Virtual environment
  - `pip install`

---

### ⏳ Fase 3 — Library AI Wajib

- [ ] **NumPy**
  - Array dan matrix
  - Operasi matematika
  - Broadcasting

- [ ] **Pandas**
  - DataFrame dan Series
  - Filtering, sorting, grouping
  - Baca/tulis CSV

- [ ] **Requests**
  - Hit REST API
  - Handle response JSON
  - Headers dan authentication

- [ ] **Matplotlib**
  - Line chart, bar chart
  - Visualisasi data dasar

---

### ⏳ Fase 4 — Dunia AI Beneran

- [ ] **OpenAI / Anthropic SDK**
  - Setup API key
  - Basic completion
  - Chat history management
  - Streaming response

- [ ] **Prompt Engineering**
  - System prompt
  - Few-shot prompting
  - Chain of thought

- [ ] **LangChain Dasar**
  - LLM chains
  - Prompt templates
  - Memory

- [ ] **LlamaIndex Dasar**
  - Document loading
  - Index building
  - Query engine

- [ ] **Project: RAG Chatbot**
  - Upload PDF
  - Vector database
  - Query dan retrieval
  - Simple UI

---

## 📁 Struktur Repo

```
python-ai-journey/
├── fase-1-dasar/
│   ├── latihan-1-variabel.py
│   ├── latihan-2-string.py
│   ├── latihan-3-dict.py
│   ├── latihan-4-kondisi.py
│   ├── latihan-5-loop.py
│   └── latihan-6-comprehension.py
├── fase-2-menengah/
│   ├── latihan-function.py
│   ├── latihan-oop.py
│   └── latihan-error-handling.py
├── fase-3-library/
│   ├── numpy-dasar.py
│   ├── pandas-dasar.py
│   └── requests-api.py
├── fase-4-ai/
│   ├── openai-sdk.py
│   ├── langchain-dasar.py
│   └── rag-chatbot/
└── README.md
```

---

## 💡 Konsep Penting yang Udah Dikuasai

```python
# Dict comprehension + zip + filter — satu baris
hasil = {n: v for n, v in zip(nama, skor) if v >= 70}

# Lambda + max() — cari item terbesar berdasarkan kondisi
mahal = max(transaksi, key=lambda t: t["harga"] * t["qty"])

# List of dict — format standar API response
chat = [
    {"role": "user", "content": "halo"},
    {"role": "assistant", "content": "halo juga!"},
]

# Loop chat history — yang bakal dipake tiap hari
pesan_user = [c["content"] for c in chat if c["role"] == "user"]
```

---

## 🛠️ Tools & Setup

| Tool | Fungsi | Status |
|------|--------|--------|
| Python 3.10+ | Runtime | ✅ |
| VS Code | Code editor | ✅ |
| GitHub | Version control | ✅ |
| Google Colab | Cloud notebook | ✅ |
| Git CLI | Version control pro | 🔄 Coming soon |
| Virtual Env | Isolasi project | ⏳ Fase 2 |

---

## 📅 Timeline

```
Minggu 1–2  → Fase 1 selesai 
Minggu 2–3  → Fase 2 selesai
Minggu 3–4  → Fase 3
Minggu 4–6  → Fase 4 + project pertama
Bulan 2–3   → Portfolio ready
Bulan 3–4   → Junior AI Engineer 🎯
```

---

## 📌 Catatan Penting

> **Konsistensi ngalahin bakat.** Lebih baik 1 jam sehari selama 3 bulan daripada marathon seminggu terus berhenti.

> **Tangan harus gerak.** Baca doang gak cukup — ketik ulang semua kode, ubah-ubah nilainya, coba bikin error sendiri.

> **Comment kode lo.** Nulis kenapa, bukan cuma apa. Kebiasaan ini yang bikin lo keliatan pro.

---

*Last updated: Mei 2026*
*Goal: Junior AI Engineer 🚀*


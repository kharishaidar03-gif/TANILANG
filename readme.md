# 🌾 TANI Language (Bahasa Pemrograman Petani)

**TANI** adalah bahasa pemrograman edukasi berbasis Python yang menggunakan istilah-istilah dunia pertanian Indonesia. Proyek ini dirancang untuk dijalankan di lingkungan mobile menggunakan **Termux** dan dikelola melalui **ZArchiver**.

---

## 🛠️ Fitur & Sintaks
Bahasa ini menggunakan kata kunci unik yang dekat dengan kearifan lokal:

| Perintah | Fungsi | Contoh |
| :--- | :--- | :--- |
| `TANAM` | Mencetak teks atau nilai variabel ke layar (Print). | `TANAM "Halo Sawah!"` |
| `PUPUK` | Menetapkan nilai ke sebuah variabel (Assignment). | `bibit PUPUK "Padi"` |
| `PANEN` | Menghentikan program dengan sukses (Exit). | `PANEN` |
| `#` | Menulis catatan atau komentar (diabaikan mesin). | `# Ini komentar` |

---

## 📂 Struktur Proyek
Proyek ini memiliki arsitektur modular:
* `lexer.py`: Memecah kode menjadi komponen kecil (Token).
* `parser_tani.py`: Mengatur struktur dan logika perintah.
* `tani.py`: File utama (Interpreter) untuk menjalankan kode.
* `script.tani`: File tempat kamu menulis kode bahasa TANI.

---

## 🚀 Cara Install & Menjalankan

### 1. Persiapan (Termux)
Pastikan kamu sudah menginstal Python di Termux:
```bash
pkg update && pkg upgrade
pkg install python

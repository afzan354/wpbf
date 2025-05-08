Berikut README lengkap untuk script **`wpbf.py`** yang bisa kamu pakai di GitHub:

---

# 🛠️ WordPress Login Brute Forcer (`wpbf.py`)

Script ini melakukan brute-force login ke halaman WordPress login (`wp-login.php`) menggunakan kombinasi daftar username dan password dari file. Cocok untuk **pengujian keamanan (ethical hacking)** pada WordPress milik sendiri.

⚠️ **PERINGATAN**: Penggunaan terhadap situs tanpa izin adalah tindakan ilegal. Script ini **hanya untuk tujuan edukasi dan pengujian sistem milik sendiri**.

---

## 🔍 Fitur

* Membaca kombinasi username dan password dari file (`user.txt` dan `pass.txt`)
* Menangani hidden field dari form login WordPress (seperti nonce, redirect)
* Menggunakan sesi (`requests.Session`) untuk efisiensi
* Mendeteksi login sukses berdasarkan redirect ke `/wp-admin`

---

## 📂 Struktur File

Pastikan Anda memiliki file berikut:

```
wpbf.py
user.txt      # berisi daftar username (satu per baris)
pass.txt      # berisi daftar password (satu per baris)
```

Contoh `user.txt`:

```
admin
test
administrator
```

Contoh `pass.txt`:

```
admin123
123456
password
```

---

## ⚙️ Cara Instalasi

1. **Clone repo ini**:

   ```bash
   git clone https://github.com/afzan354/wpbf.git
   cd wpbf
   ```

2. **Install dependencies**:
   Script ini memerlukan `requests` dan `beautifulsoup4`.

   ```bash
   pip install requests beautifulsoup4
   ```

---

## ▶️ Cara Menjalankan

```bash
python wpbf.py
```

Script akan mencoba setiap kombinasi username dan password dari file, lalu menampilkan hasil:

```
Failed: admin - admin123
Failed: admin - 123456
Success! Username: admin, Password: password
```

Jika login berhasil (terdeteksi redirect ke `/wp-admin`), proses akan berhenti.

---

## 🧪 Target

Secara default, script diarahkan ke:

```
https://localhost.com/wp-login.php
```

Kamu bisa mengubah URL target dengan mengedit variabel `url` di awal script.

---

## ❗ Penting

* Jangan gunakan script ini terhadap situs yang **bukan milik kamu** atau **tanpa izin tertulis**.
* WordPress biasanya menggunakan mekanisme perlindungan (rate limit, captcha, login delay) yang bisa membuat brute-force menjadi tidak efektif.

---

## 📄 Lisensi

Distribusi bebas untuk edukasi dan riset keamanan. Gunakan dengan tanggung jawab dan sesuai hukum yang berlaku.

---

Kalau kamu ingin, aku bisa bantu buatkan `requirements.txt` dan `.gitignore` juga agar repositorimu lebih rapi. Mau sekalian dibantu?

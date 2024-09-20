# Aplikasi Cipher

Aplikasi ini adalah sebuah aplikasi berbasis GUI menggunakan Python yang memungkinkan pengguna untuk mengenkripsi dan mendekripsi teks menggunakan tiga jenis cipher: Vigenère, Playfair, dan Hill cipher. Aplikasi ini menyediakan opsi untuk input melalui keyboard dan juga unggahan file untuk teks.

## Fitur

- **Cipher Vigenère**: Mengenkripsi dan mendekripsi teks menggunakan kata kunci di mana setiap huruf dalam teks digeser oleh huruf yang sesuai dalam kunci.
- **Cipher Playfair**: Cipher substitusi yang mengenkripsi pasangan huruf.
- **Cipher Hill**: Cipher substitusi poligrafik yang menggunakan aljabar linear untuk mengenkripsi pasangan huruf dengan matriks kunci 2x2.
- **Opsi Input**: Pengguna dapat memasukkan teks melalui keyboard atau mengunggah file `.txt`.
- **Antarmuka Pengguna**: GUI yang sederhana dan mudah digunakan dibangun dengan Tkinter.

## Persyaratan

- Python 3.x
- Tkinter (biasanya sudah terinstal dengan Python)
- Numpy

Untuk menginstal pustaka yang diperlukan, Anda bisa menjalankan perintah berikut:

```bash
pip install numpy
# Aplikasi Cipher

Aplikasi ini adalah sebuah aplikasi berbasis GUI menggunakan Python yang memungkinkan pengguna untuk mengenkripsi dan mendekripsi teks menggunakan tiga jenis cipher: Vigenère, Playfair, dan Hill cipher. Aplikasi ini menyediakan opsi untuk input melalui keyboard dan juga unggahan file untuk teks.

## Fitur

- **Cipher Vigenère**: Mengenkripsi dan mendekripsi teks menggunakan kata kunci di mana setiap huruf dalam teks digeser oleh huruf yang sesuai dalam kunci.
- **Cipher Playfair**: Cipher substitusi yang mengenkripsi pasangan huruf.
- **Cipher Hill**: Cipher substitusi poligrafik yang menggunakan aljabar linear untuk mengenkripsi pasangan huruf dengan matriks kunci 2x2.
- **Opsi Input**: Pengguna dapat memasukkan teks melalui keyboard atau mengunggah file `.txt`.
- **Antarmuka Pengguna**: GUI yang sederhana dan mudah digunakan dibangun dengan Tkinter.

## Persyaratan

- Python 3.x
- Tkinter (biasanya sudah terinstal dengan Python)
- Numpy

Untuk menginstal pustaka yang diperlukan, Anda bisa menjalankan perintah berikut:

```bash
pip install numpy

Cara Penggunaan
Jalankan Aplikasi: Untuk menjalankan aplikasi, eksekusi file main.py:

bash
python main.py
Pilih Cipher: Pilih salah satu dari tiga cipher (Vigenère, Playfair, atau Hill) dari tombol radio yang disediakan.

Masukkan Kunci Enkripsi: Berikan kunci enkripsi (minimal 12 karakter untuk keamanan).

Pilih Metode Input: Pilih apakah teks akan dimasukkan melalui keyboard atau dengan mengunggah file .txt.

Enkripsi/Dekripsi:

Klik tombol "Encrypt" untuk mengenkripsi teks.
Klik tombol "Decrypt" untuk mendekripsi teks.
Lihat Hasil: Hasil enkripsi atau dekripsi akan ditampilkan di kotak teks di bagian bawah aplikasi.

Deskripsi File
main.py: Berisi implementasi GUI menggunakan Tkinter dan menangani aksi enkripsi dan dekripsi.
ciphers.py: Berisi logika untuk cipher Vigenère, Playfair, dan Hill, termasuk fungsi-fungsi pembantu untuk pemrosesan awal dan pembuatan kunci.
cipher_input.txt: File teks contoh untuk pengujian enkripsi dan dekripsi berbasis file.
Algoritma Enkripsi
Cipher Vigenère
Cipher Vigenère menggeser setiap huruf dari teks asli berdasarkan jumlah posisi yang ditentukan oleh huruf yang sesuai dalam kunci.

Enkripsi: vigenere_encrypt(text, key)
Dekripsi: vigenere_decrypt(text, key)
Cipher Playfair
Cipher Playfair bekerja dengan mengenkripsi pasangan huruf (digraf) berdasarkan matriks 5x5 huruf yang dihasilkan dari kunci.

Enkripsi: playfair_encrypt(text, key)
Dekripsi: playfair_decrypt(text, key)
Cipher Hill
Cipher Hill adalah cipher poligrafik yang mengenkripsi pasangan huruf menggunakan perkalian matriks. Sebuah matriks 2x2 dihasilkan dari kunci.

Enkripsi: hill_encrypt(text, key)
Dekripsi: hill_decrypt(text, key)
Contoh Penggunaan
Anda dapat menggunakan file input contoh cipher_input.txt yang telah disediakan untuk menguji fungsi enkripsi dan dekripsi berbasis file.


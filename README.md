# Sistem Pencarian Data Buku Perpustakaan Digital

## Deskripsi Proyek

Proyek ini merupakan implementasi algoritma pencarian data buku pada dataset perpustakaan digital menggunakan bahasa pemrograman Python. Proyek dibuat untuk mempelajari dan membandingkan kinerja algoritma **Linear Search** dan **Binary Search** berdasarkan jumlah perbandingan serta waktu eksekusi.

Dataset yang digunakan berisi data buku dengan berbagai atribut, seperti ID buku, judul, penulis, penerbit, tanggal terbit, kategori, jumlah halaman, rating, dan bahasa.

## Tujuan

- Mengimplementasikan algoritma Linear Search dan Binary Search.
- Memahami perbedaan cara kerja kedua algoritma.
- Menghitung jumlah operasi perbandingan selama pencarian.
- Mengukur waktu eksekusi algoritma.
- Membandingkan hasil pengujian pada ukuran dataset yang berbeda.

## Teknologi yang Digunakan

- Python
- Dataset CSV
- Visual Studio Code
- Git dan GitHub

## Algoritma

### 1. Linear Search

Linear Search mencari data dengan memeriksa elemen satu per satu dari awal dataset hingga data ditemukan atau seluruh elemen selesai diperiksa.

Kompleksitas waktu:
- Best case: Ω(1)
- Average case: Θ(n)
- Worst case: O(n)

### 2. Binary Search

Binary Search mencari data dengan membagi ruang pencarian menjadi dua bagian secara berulang. Algoritma ini membutuhkan data yang sudah terurut berdasarkan ID buku.

Kompleksitas waktu:
- Best case: Ω(1)
- Average case: Θ(log n)
- Worst case: O(log n)

## Dataset

Dataset yang digunakan adalah `google_books_dataset.csv`.

Program memuat data buku yang valid untuk proses pencarian. Pada pengujian awal, program berhasil memuat **15.139 data buku valid**.

## Struktur Folder

```text
tugas_daa/
├── main.py
├── google_books_dataset.csv
└── README.md
```

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer dan terminal berada di folder proyek.

### 1. Menjalankan program

```bash
python main.py
```

### 2. Menguji algoritma

```bash
python main.py --benchmark
```

Perintah tersebut menjalankan pengujian algoritma sesuai skenario dan ukuran dataset yang telah ditentukan dalam program.

### 3. Mencari buku menggunakan kedua algoritma

```bash
python main.py --key "ID_BUKU" --algorithm both
```

Ganti `ID_BUKU` dengan ID buku yang tersedia dalam dataset.

### 4. Menggunakan Linear Search

```bash
python main.py --key "ID_BUKU" --algorithm linear
```

### 5. Menggunakan Binary Search

```bash
python main.py --key "ID_BUKU" --algorithm binary
```

## Pengujian

Pengujian dilakukan pada beberapa ukuran input, yaitu 100, 1.000, dan 10.000 data. Skenario pencarian meliputi:

- Data ditemukan di posisi awal.
- Data ditemukan di posisi tengah.
- Data ditemukan di posisi akhir.
- Data tidak ditemukan.

Parameter yang diamati adalah jumlah perbandingan dan waktu eksekusi. Waktu eksekusi dapat berbeda bergantung pada perangkat dan kondisi saat program dijalankan.

## Kesimpulan

Linear Search memiliki cara kerja yang sederhana, tetapi jumlah pemeriksaannya dapat meningkat seiring bertambahnya ukuran dataset. Binary Search dapat mengurangi ruang pencarian secara bertahap sehingga lebih efisien untuk pencarian pada data yang sudah terurut.

Proyek ini menunjukkan perbedaan karakteristik kedua algoritma melalui implementasi dan pengujian menggunakan Python.

## Catatan

Proyek ini dibuat untuk keperluan pembelajaran Algoritma dan Analisis Kompleksitas. Pastikan file dataset tersedia di lokasi yang sesuai agar program dapat dijalankan.

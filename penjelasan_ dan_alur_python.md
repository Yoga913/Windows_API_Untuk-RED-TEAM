# manual book

**EXTRACK_IAT.PY:**

Python yang menggunakan pustaka `pefile` untuk melakukan analisis terhadap file PE (Portable Executable).
 File PE adalah format file eksekusi yang digunakan oleh Windows.

## Berikut adalah penjelasan untuk setiap kode dan alur pada program

 1. `import pefile` dan `import sys`: Ini adalah pernyataan impor yang digunakan untuk mengimpor modul `pefile` dan `sys`. Modul `pefile` digunakan untuk membaca dan menganalisis file PE, sedangkan `sys` digunakan untuk berinteraksi dengan sistem operasi dan argumen baris perintah.

 2. `def extract_iat(pe_file):`: Ini adalah definisi fungsi `extract_iat` yang mengambil satu argumen, yaitu `pe_file`, yang merupakan path menuju file PE yang akan dianalisis.

 3. `try:`: Ini memulai blok try-except, yang digunakan untuk menangani pengecualian yang mungkin terjadi saat menjalankan kode di dalamnya.

 4. `pe = pefile.PE(pe_file)`: Ini membuat objek `pe` menggunakan pustaka `pefile` untuk membaca file PE yang disediakan.

 5. `if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):`: Ini memeriksa apakah file PE memiliki tabel impor. Jika ya, maka kode di dalamnya akan dieksekusi. Jika tidak, maka program akan mencetak "No imports found.".

 6. `for entry in pe.DIRECTORY_ENTRY_IMPORT:`: Ini iterasi melalui setiap entri dalam tabel impor.

 7. `print(f"Imports from {entry.dll.decode()}:")`: Ini mencetak nama DLL dari setiap entri impor.

 8. `for imp in entry.imports:`: Ini iterasi melalui setiap impor dalam entri impor.

 9. `address = hex(imp.address)`: Ini mengonversi alamat impor menjadi format heksadesimal.

 10. `name = imp.name.decode() if imp.name else 'Ordinal Import'`: Ini mendekode nama impor jika ada, jika tidak, itu menetapkan 'Ordinal Import'.

 11. `print(f"    {address} {name}")`: Ini mencetak alamat heksadesimal dan nama impor.

 12. `except Exception as e:`: Jika terjadi pengecualian saat menjalankan kode di dalam blok `try`, maka pengecualian tersebut akan ditangkap di sini dan dicetak.

 13. `if __name__ == '__main__':`: Ini memeriksa apakah skrip ini dijalankan sebagai program utama.

 14. `if len(sys.argv) > 1:`: Ini memeriksa apakah argumen baris perintah telah diberikan.

 15. `extract_iat(sys.argv[1])`: Jika argumen telah diberikan, fungsi `extract_iat` dipanggil dengan argumen pertama yang merupakan path ke file PE.

 16. `else:`: Jika tidak ada argumen yang diberikan, program mencetak pesan meminta path ke file PE.

 Alur program ini adalah membaca file PE yang diberikan sebagai argumen baris perintah, menganalisis impor yang ada dalam file tersebut, dan mencetak informasi tentang setiap impor, termasuk alamat dan nama impor jika tersedia. Jika tidak ada impor yang ditemukan, program akan mencetak pesan yang sesuai.

## =================================================

**ordinal_pe.py:**

 Python yang digunakan untuk mencari ordinal dari sebuah fungsi dalam sebuah file DLL (Dynamic Link Library).

 1. Pertama-tama, program mengimpor dua modul, yaitu `pefile` dan `sys`. Modul `pefile` digunakan untuk membaca Portable Executable (PE) files seperti file DLL, sedangkan modul `sys` digunakan untuk berinteraksi dengan sistem operasi dan membaca argumen baris perintah.

 2. Kemudian, terdapat fungsi `find_ordinal(dll_path, function_name)` yang berfungsi untuk mencari ordinal dari fungsi yang diberikan. Fungsi ini menerima dua parameter: `dll_path` (alamat file DLL) dan `function_name` (nama fungsi yang ingin dicari ordinalnya). Fungsi ini membuka file DLL menggunakan `pefile.PE` dan kemudian mencari setiap simbol dalam direktori ekspor (export directory). Jika nama fungsi cocok dengan `function_name` yang diberikan, maka fungsi akan mengembalikan ordinal dari fungsi tersebut. Jika tidak ditemukan, akan mengembalikan `None`.

 3. Fungsi `main()` adalah titik masuk utama program. Pertama, program memeriksa jumlah argumen baris perintah. Jika jumlahnya tidak sama dengan 3, maka program akan mencetak pesan penggunaan dan keluar dengan status keluar 1.

 4. Jika jumlah argumen baris perintah sesuai, program akan mengambil path file DLL dan nama fungsi dari argumen baris perintah.

 5. Kemudian, program memanggil fungsi `find_ordinal()` dengan path file DLL dan nama fungsi yang diberikan. Hasil yang dikembalikan oleh fungsi ini akan disimpan dalam variabel `ordinal`.

 6. Selanjutnya, program memeriksa apakah `ordinal` tidak `None`. Jika tidak, maka program mencetak pesan bahwa fungsi dengan nama yang diberikan memiliki ordinal tertentu. Jika `ordinal` adalah `None`, program akan mencetak pesan bahwa fungsi tidak ditemukan.

 7. Terakhir, program memanggil fungsi `main()` jika script dijalankan secara langsung (bukan diimpor sebagai modul).

 Dengan demikian, tujuan utama dari kode tersebut adalah untuk memberikan cara untuk mencari ordinal dari sebuah fungsi dalam sebuah file DLL berdasarkan nama fungsi yang diberikan sebagai argumen baris perintah.

## ================================================

## Windows-API-untuk-Tim Merah

Repositori ini adalah kompilasi API Windows utama untuk digunakan dalam PenTest, operasi Tim Merah, dan Analisis Malware

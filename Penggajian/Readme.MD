# Penjelasan 
Kode ini adalah contoh program Python untuk menghitung gaji karyawan berdasarkan nama, gaji pokok, golongan, jumlah anak, dan status pernikahan. Program ini menggunakan class Employee yang memiliki atribut dan method sebagai berikut:

- Atribut:
  - name: nama karyawan (string)
  - salary: gaji pokok karyawan (integer)
  - grade: golongan karyawan (integer antara 1 sampai 4)
  - num_children: jumlah anak karyawan (integer non-negatif)
  - married: status pernikahan karyawan (boolean)
- Method:
  - get_salary(): mengembalikan gaji bersih karyawan setelah ditambahkan tunjangan dan dikurangi pajak (integer)

✅ Tunjangan yang diberikan kepada karyawan adalah:

- Tunjangan golongan: persentase dari gaji pokok sesuai dengan golongan karyawan
  - Golongan 1: 5%
  - Golongan 2: 10%
  - Golongan 3: 15%
  - Golongan 4: 20%
- Tunjangan anak: 2% dari gaji pokok untuk setiap anak
- Tunjangan istri: 10% dari gaji pokok jika karyawan sudah menikah

✅ Pajak yang dipotong dari gaji karyawan adalah:

- Pajak penghasilan: persentase dari total gaji sebelum pajak sesuai dengan rentang gaji
  - Gaji <= 5 juta: 5%
  - Gaji > 5 juta dan <= 10 juta: 10%
  - Gaji > 10 juta: 15%

✅ Bonus yang diberikan kepada karyawan adalah:

- Bonus keluarga: jumlah uang tambahan sesuai dengan golongan dan jumlah anak karyawan
  - Golongan 1 dan memiliki >= 2 anak: Rp250.000
  - Golongan 2 dan memiliki >= 3 anak: Rp500.000
  - Golongan 3 dan memiliki >= 4 anak: Rp1.000.000
  - Golongan 4 dan memiliki >= 5 anak: Rp1.500.000

✅ Untuk menggunakan program ini, buat objek Employee dengan memberikan nilai untuk atributnya, lalu panggil method get_salary() untuk mendapatkan gaji bersihnya. Contoh:

emp1 = Employee("Budi", 8000000, 2, 2, True)
print(emp1.get_salary())

Output:
9040000
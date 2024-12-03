print('##  Program Python Menghitung Gaji Karyawan  ##')
print('===============================================')
print()

#Jika jam kerja karyawan lebih dari 48 jam per minggu maka akan mendapat uang lembur dengan perhitungan uang lembur = (jam kerja-48)*4000.
#Jika jam kerja kurang dari 48 jam maka pegawai tidak akan mendapat uang lembur.
#Perhitungan gaji pegawai adalah upah + uang lembur.
#Input berupa nama karyawan, golongan dan jam kerja.
#Outputnya adalah nama karyawan dan gaji yang diterima.
#Golongan = A maka upah per jam 5000
#Golongan = B maka upah per jam 7000
#Golongan = C maka upah per jam 8000
#Golongan = D maka upah per jam 10000


# proses input
 
nama = input('Nama Karyawan: ')
golongan = input('Golongan: ')
jam_kerja = int(input('Jumlah jam kerja: '))
 
print()
 
# tentukan jumlah upah per jam berdasarkan golongan
 
if golongan == "A":
  upah_per_jam = 5000
elif golongan == "B":
  upah_per_jam = 7000
elif golongan == "C":
  upah_per_jam = 8000
elif golongan == "D":
  upah_per_jam = 10000
 
total_upah = jam_kerja * upah_per_jam
  
# cek apakah jam kerja lebih dari 48 jam
if (jam_kerja - 48) > 0:
  total_upah = total_upah + ((jam_kerja - 48)*4000)
   
# proses output
print(nama,'menerima upah Rp.',total_upah,'per minggu')
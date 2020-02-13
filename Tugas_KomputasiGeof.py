#Created on Sun May 5 14:08:00 2019

#@author: Nama: Muhammad Dhery Mahendra , NPM: 1706046180

"""Jawaban Soal Nomer 1"""

#Membuat Grafik antara Freq dengan Obs

import matplotlib.pyplot as plt

#Data Freq sebagai X dan data Obs sebagai Y

x = [10400,8800.0,7200.0,6000.0,5200.0,4400.0,3600.0,3000.0,2600.0,2200.0,1800.0,1500.0,1300.0,1100.0,900.00,780.00,640.00,530.00,460.00,390.00,320.00,265.00,229.00,194.00,159.00,132.00,115.00,97.000,79.000,66.000,57.000,49.000,40.000,33.000,27.500,22.500,18.800,16.200,13.700,11.200,9.4000,8.1000,6.9000,5.6000,4.7000,4.1000,3.4000,2.8100,2.3400,2.0300,1.7200,1.4100,1.1700,1.0200,0.8600,0.7000,0.5900,0.5100,0.4300,0.3500]

y = [118.10,120.20,126.94,132.21,135.90,140.75,148.32,154.47,162.18,166.02,171.59,182.24,180.82,173.80,172.86,174.86,173.47,173.66,169.12,164.51,160.78,154.91,149.28,145.26,134.36,129.19,119.48,114.50,106.44,98.047,87.549,82.577,74.658,67.245,60.845,52.375,48.247,42.095,39.842,34.371,29.379,26.838,23.794,21.791,19.845,18.257,17.760,17.024,15.859,15.909,15.607,16.403,16.539,19.550,23.114,24.810,28.806,32.496,16.893,33.039]

#Mempersiapkan frame nya
plt.figure(figsize=(9,6))

#Plot data dalam grafik dengan menggunakan skala logaritmik
plt.loglog(x,y)


"""Membuat Grafik antara Freq dengan Cal"""

#Data Freq sebagai X dan data Cal sebagai Y

X = [10400,8800.0,7200.0,6000.0,5200.0,4400.0,3600.0,3000.0,2600.0,2200.0,1800.0,1500.0,1300.0,1100.0,900.00,780.00,640.00,530.00,460.00,390.00,320.00,265.00,229.00,194.00,159.00,132.00,115.00,97.000,79.000,66.000,57.000,49.000,40.000,33.000,27.500,22.500,18.800,16.200,13.700,11.200,9.4000,8.1000,6.9000,5.6000,4.7000,4.1000,3.4000,2.8100,2.3400,2.0300,1.7200,1.4100,1.1700,1.0200,0.8600,0.7000,0.5900,0.5100,0.4300,0.3500]

Y = [117.48,121.44,126.39,131.26,135.49,141.00,148.44,155.65,161.25,167.22,172.87,176.10,177.33,177.52,176.48,175.23,173.08,170.59,168.34,165.15,160.38,154.84,149.97,143.91,136.03,128.12,121.96,114.07,104.34,95.886,89.218,82.651,74.400,67.124,60.616,53.799,47.995,43.442,38.657,33.480,29.551,26.653,23.984,21.186,19.393,18.318,17.266,16.648,16.434,16.496,16.787,17.401,18.191,18.874,19.811,21.022,22.056,22.932,23.931,25.069]
         
#Plot kedua data (Freq Vs Obs & Freq Vs Cal) menjadi 1 grafik 
plt.plot(X,Y,'r--d') #plot grafik dan memberi warna merah serta bentuk diamond
plt.title(' Freq Vs Obs (Biru), Freq Vs Cal (Merah), & Kurva Regresi Linear Data Freq Vs Obs (Hijau) ') #judul
plt.xlabel(' Freq ') #keterangan pada sumbu X
plt.ylabel(' Obs & Cal ') #keterangan pada sumbu Y


"""Jawaban Soal Nomer 2"""

#Data cal dan obs yang akan dimasukkan ke dalam rumus RMSE

cal = [117.48,121.44,126.39,131.26,135.49,141.00,148.44,155.65,161.25,167.22,172.87,176.10,177.33,177.52,176.48,175.23,173.08,170.59,168.34,165.15,160.38,154.84,149.97,143.91,136.03,128.12,121.96,114.07,104.34,95.886,89.218,82.651,74.400,67.124,60.616,53.799,47.995,43.442,38.657,33.480,29.551,26.653,23.984,21.186,19.393,18.318,17.266,16.648,16.434,16.496,16.787,17.401,18.191,18.874,19.811,21.022,22.056,22.932,23.931,25.069]

obs = [118.10,120.20,126.94,132.21,135.90,140.75,148.32,154.47,162.18,166.02,171.59,182.24,180.82,173.80,172.86,174.86,173.47,173.66,169.12,164.51,160.78,154.91,149.28,145.26,134.36,129.19,119.48,114.50,106.44,98.047,87.549,82.577,74.658,67.245,60.845,52.375,48.247,42.095,39.842,34.371,29.379,26.838,23.794,21.791,19.845,18.257,17.760,17.024,15.859,15.909,15.607,16.403,16.539,19.550,23.114,24.810,28.806,32.496,16.893,33.039]

"""Menghitung Root Mean Square Error (RMSE)"""

#Nilai awal sumasi
sumtotal = 0

for i in range(len(cal)): #banyaknya data antara cal dan obs adalah sama, jadi bisa pake len cal atau len obs, hasilnya bakal sama aja
    total = sumtotal + (cal[i]-obs[i])**2 #Menghitung jumlah dari seluruh nilai data (cal-obs)^2
    
hasilbagi = float(total)/(len(cal)) #jumlah nilai data (cal-obs)^2 dibagi oleh banyaknya data
RMSE = (hasilbagi)**0.5 #hasil dari pembagiannya diakarkan sehingga didaptkan nilai RMSE 

print 'Nilai RMSE = ', RMSE 



"""Jawaban Soal Nomer 3"""

"""Hitung Nilai Rata - Rata pada data Freq Vs Obs"""
#Nilai awal sumasi
sumx = 0
sumy = 0

for i in range (len(x)):
    sumx = sumx + X[i] #Menghitung total nilai x
    sumy = sumy + Y[i] # Menghitung total nilai y
    
xr = float(sumx)/len(x) #Nilai rata - rata x
yr = float(sumy)/len(y) #Nilai rata - rata y


"""Hitung Nilai gradien (m) untuk data Freq Vs Obs"""
#Nilai awal sumasi
pembilang = 0
penyebut = 0

for i in range (len(x)):
    pembilang = pembilang + (x[i]-xr)*(y[i]-yr)
    penyebut = penyebut + (x[i]-xr)**2
     
m = pembilang/penyebut #Rumus Gradien
c = yr - m*xr #Rumus Intercept

print 'Persamaan Kurva Regresi Linear data Freq Vs Obs : y = ',m,'x +',c


"""Plot kurva regresi linear pada data Freq Vs Obs"""

import numpy as np

#Membuat domain A sebanyak 100 dalam range 0 s/d 10000, A di sumbu x dan B di sumbu y
A = np.linspace(0,10000,100)
B = m*A + c # Hitung nilai B untuk masing - masing A

plt.plot(A,B,'g-') #Membuat garis warna green
plt.savefig('GRAFIK_TUGAS_KOMPUT.png',dpi=300) #membuat gambar grafik format png resolusi 300
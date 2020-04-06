# -*- coding: utf-8 -*-
"""
Created on  April 04 12:06:59 2020

Cara Running:
    1. File scv Satu Folder 
    2. Script Py 
    3. Semuanya Harus Satu Folder
    4. Output berupa File PNG

@author: M. Dhery Mahendra
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Well_2.csv")
d = data["Depth(m)"]
GR = data["GR"]
rho = data["rho"]
v1 = data["Vp"]
v2 = data["Vs"]

#Nomor 1 A Membuat Grafik GR, Vp, Vs dan Rho dalam satu panel
fig= plt.figure(figsize = (15,6)) #Ukuran Bingkai
plt1a=fig.add_subplot(141) #Lokasi Plot ada di Matriks 4x4 di Baris 1 Colum 1
plt1a.set_title("Depth-GR") #Judul Plot
plt1a.plot(GR,d, 'r') #Plot GR sama Depth dengan kode warna Merah
plt1a.grid() #Grid di plot

plt2a=fig.add_subplot(142) #Lokasi Plot ada di Matriks 4x4 di Baris 1 Colum 2
plt2a.set_title("Depth-Vp") #judul Plot
plt2a.plot(v1,d, 'r') #plot Vp sama Depth dengan kode warna Merah
plt2a.grid()

plt3a=fig.add_subplot(143) #Lokasi Plot ada di Matriks 4x4 di Baris 1 Colum 3
plt3a.set_title("Depth-Vs") #judul Plot
plt3a.plot(v2,d,'b') #Plot Vs sama depth dengan kode warna biru
plt3a.grid() #Grid di plot

plt4a=fig.add_subplot(144) #Lokasi Plot ada di Matriks 4x4 di Baris 1 Colum 4
plt4a.set_title("Depth-rho") #judul plot
plt4a.plot(rho,d,'b') #Plot Rho sama depth dengan kode warna biru
plt4a.grid() #grid di plot

#Nomor 1 B Scatter Plot
z = v1*rho #Cara mencari nilai Impedansi akustik
v = v1/v2 # Nilai Vp/Vs

plt.figure(figsize = (15, 7)) #Ukuran Bingkai
plt.title("AI vs Vp/Vs") #Judul Plot
plt.scatter(z,v, vmin=20, vmax=120, c=GR)# Plot AI vs Vp/Vs dengan kode Scatter dan warna gr
plt.xlabel("Impedansi Akustik") #Xlabel
plt.ylabel("Vp/Vs") #Ylabel
plt.grid()
plt.colorbar()

#Nomor 1 C
Lamdarho = ((v1*rho)-(v2**2*rho))*rho #Cara Mencari Lamda-rho
MyuRho = v2**2*rho**2 #Cara Mencari nilai myu-rho

plt.figure(figsize = (15, 7)) #Ukuran Bingkai
plt.title("Lamdarho vs MyuRho") #Judul Plot
plt.scatter (Lamdarho, MyuRho , vmin=20, vmax=120, c=GR) # Plot AI vs Vp/Vs dengan kode Scatter dan warna gr
plt.xlabel("LamdaRho") #Xlabel
plt.ylabel("MyuRho") #Ylabel
plt.grid()
plt.colorbar()

# -*- coding: utf-8 -*-
"""
Created on  April 04 12:06:59 2020

Cara Running:
    1. File scv Satu Folder 
    2. Script Py 
    3. Semuanya Harus Satu Folder

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

plt.savefig('1a', dpi=300)

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

plt.savefig('1b', dpi=300)

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

plt.savefig('1c', dpi=300)

#
#BATAS NOMOR
#

import segyio
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D #Untuk Axis 3D

#Input data Seismik
#Raw data Trace
#Tampilkan dalam bentuk 3 dimensi penampang inline, 
#xline dan time seperti yang pernah diajarkan di kelas untuk data 3d_nearstack!
#2a
Seismik1 = '3d_nearstack.sgy'
c = segyio.open(Seismik1, "r+", iline=101, xline=151, ignore_geometry=True)
b = (c.trace.raw[:]).T

#Buat Kubus
d = np.reshape(b,[251,101,250])
d1 = d[:,:,19] #menunjukan  penampang yang atas di timesice 19
d2 = d[:,19,:] #menunjukan  penampang yang atas di timesice 19
d3 = d[19,:,:] #menunjukan  penampang yang atas di timesice 19

#Inline
xb=np.linspace(1,101,101) #Seperti tugas kemarin
YB=40*np.ones((151,101)) 
zb=np.linspace(1,151,151)
XB,ZB = np.meshgrid(xb,zb)

#Xline
xc=np.linspace(1,101,101) #Maaf pak saya masih ragu disini
YC=40*np.ones((141,101))
zc=np.linspace(1,141,141)
XC,ZC = np.meshgrid(xc,zc)

#Buat Grafiik Mat.plot
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax2 = ax1.plot_surface(XB,YB,ZB, rstride=1, cstride=1, facecolors=plt.cm.seismic(d1), shade=True)
ax3 = ax1.plot_surface(YC,XC,ZC, rstride=1, cstride=1, facecolors=plt.cm.seismic(d1), shade=False)
fig.suptitle('3D Seismik Inline 101 Xline 151', fontsize=16)

plt.savefig('2a', dpi=300)
c.close()

#2b
#Mendefinisikan dan membuka file menggunakan SEGYIO
nearstack = '3d_nearstack.sgy'
farstack = '3d_farstack.sgy'
n = segyio.open(nearstack, ignore_geometry=True)
f = segyio.open(farstack, ignore_geometry=True)

#Membuat Array agar bisa dikurang Nilai Tracenya
arrayn = (n.trace.raw[:2020]).T     #Ide dari iksan
arrayf = (f.trace.raw[:2020]).T     #Saya mangambil dari 0-2020
attFN = arrayf-arrayn              #Ini Sesuai Soal Katanya F-N

# Set up a figure and plot a few shot gathers
clip = 100e+2 #untuk nentuin warna
vmin, vmax = -clip, clip #Seperti Tugas kemarin tentang load data 2d seismik

figsize=(20,60) #ukuran bingkai
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(n.trace.raw[:1500].T, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax) #Warna seismik
plt.title("Seismic Nearstack") #raw = mengatur section saya ambil 0-1500 
plt.savefig('2b1', dpi=300)

figsize=(20,60) #Ukuran bingkai
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(f.trace.raw[:1500].T, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax) #Warna seismik
plt.title("Seismic Farstack") #raw = mengatur section saya ambil 0-1500 
plt.savefig('2b2', dpi=300)

figsize=(20,60)
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(attFN, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax) #ada referensi dari github tugas sebelumnya
plt.title("Attribute Far-Near Stack")
plt.savefig('2b3', dpi=300)

#2c
#Membuat Array agar bisa dikurang Nilai Tracenya
arrayn = (n.trace.raw[:]).T     #Ide dari iksan
arrayf = (f.trace.raw[:]).T     #Saya mangambil dari 0-2020
DeltFN = arrayf-arrayn              #Ini Sesuai Soal Katanya F-N

#Buat Kubus
d = np.reshape(DeltFN,[251,101,250])
d1 = d[10,:,:] #menunjukan  penampang yang atas di timesice 10
d2 = d[150,:,:] #menunjukan  penampang yang atas di timesice 150
d3 = d[250,:,:] #menunjukan  penampang yang atas di timesice 250

figsize=(10,10)
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(d1, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax) #ide dari iksan(biar bisa nampilinn attFN)
plt.title("Attribute Far-Near stack TimeSlice 10")
plt.savefig('2c1', dpi=300)

figsize=(10,10)
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(d2, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax)
plt.title("Attribute Far-Near stack TimeSlice 150")
plt.savefig('2c2', dpi=300)

figsize=(10,10)
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(d3, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax)
plt.title("Attribute Far-Near stcak TimeSlice 250")
plt.savefig('2c2', dpi=300)

#
#BATAS NOMOR
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("koefisen_refleksi.csv") #Input Data CSV
kr = data["cr"] #Mengambil Data Koef Refleksi
tetha = np.arange(0, 46, 1) #Membuat Fungsi sudut datang 0-45 derajat
#3a
plt.figure()
plt.plot(tetha, kr, "r")
plt.title("Koef Refleksi Vs Sudut Datang")
plt.xlabel("Sudut Datang(Tetha)")
plt.ylabel("Koefisien Refleksi")
plt.grid()

plt.savefig('3a',dpi=300)

#Inisiasi Variabel
xn = tetha
fxn = kr  
z1,z2 = 5712,5288 #Impedansi AKustik
vp1,vp2 = 2020,2000 #Kecepatan gelombang p
rho1,rho2 = 2.09,2.38 #rho
dvp = vp2-vp1 #delta Kecepatan gelombang p
vp = (vp2+vp1)/2 
drho = rho2-rho1
rho = (rho2+rho1)/2
vs1 = 1500.0
vs2 = 1000.0


#Kolaborasi dan ide dari M. Kholis Fadhillah dan William Janesta
def derivFunc(z1,z2): 
    return -2*z2/(z2+z1)**2  

def derivFunc2(rho1,vp): 
    return vp*rho1**0

def derivFunc3(rho2,vp2): 
    return vp2*rho2**0

def derivFunc4(vs1,miu1): 
    return (miu1**0)/(vs1**2)
  
def derivFunc5(vs2,miu2): 
    return miu2**0/vs2**2

#Kolaborasi dan ide dari M. Kholis Fadhillah dan William Janesta
def newtonRaphson(z1,z2): 
    h = kr[0] / derivFunc(z1,z2) 
    if abs(h) >= 0.0001:
        h = kr/derivFunc(z1,z2) 
        z1,z2 = z1,z2 - h 

newtonRaphson(5712,5288) 

def newtonRaphson1(vp1,rho1): 
    h = 5712 / derivFunc2(rho1,vp1) 
    if abs(h) >= 0.0001:
        h = 5712/derivFunc2(rho1,vp1)*0.05
          
        vp1,rho1 = vp1,rho1 - h
      
newtonRaphson1(2596,2.2)
  
def newtonRaphson2(vp2,rho2): 
    h = 5288 / derivFunc3(rho2,vp2) 
    if abs(h) >= 0.0001:
        h = 5288/derivFunc3(rho2,vp2)*0.05
          
        vp2,rho2 = vp2,rho2 - h
         
newtonRaphson2(2116,2.5)

def newtonRaphson3(vs1,miu1): 
    h = 2.09 / derivFunc4(vs1,miu1) 
    if abs(h) >= 0.0001:
        h = 2.09/derivFunc4(vs1,miu1)
          
        vs1,miu1 = vs1,miu1 - h
        
newtonRaphson3(1700,5700000)
  
def newtonRaphson4(vs2,miu2): 
    h = 2.38 / derivFunc5(vs2,miu2) 
    if abs(h) >= 0.0001:
        h = 2.38/derivFunc5(vs2,miu2)
          
        vs2,miu2 = vs2,miu2 - h
        
newtonRaphson4(1100,2400000)

#Mencari Nilai poison ratio lapisan 1 dan poison ratio lapisan 2 pada data relektifitas tersebut
pois1 = (((vp1/vs1)**2)-2)/(2*(((vp1/vs1)**2)-1))
pois2 = (((vp2/vs2)**2)-2)/(2*(((vp2/vs2)**2)-1))
r0 = 0.5*((dvp/vp)+(drho/rho)) 
#3b
print(pois1,pois2,r0)

#
#BATAS NOMOR
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d #Untuk Interpolasi

data1 = pd.read_csv('tnmo.csv')
data2 = pd.read_csv('vnmo.csv')
data3 = pd.read_csv('horizon a.csv')

vnmo = np.array(data2)
tnmo = np.array(data1)
hra = np.array(data3["Horizon A"])

tcdp1 = tnmo [:,:] #time Normal move out
vcdp1 = vnmo [:,:] #velovity normal move out

#Insiasi Variabel
tmin = np.min(hra)
tmax = np.max(hra)
dt = 0.002
t = np.arange(tmin,tmax,dt)
m = len(t)
vinterp = np.zeros((m,34))
vrms1 = vinterp[:,1]

for i in range(0,34):
    finterp = interp1d(tnmo[:,i],vnmo[:,i],kind='cubic',fill_value="extrapolate")
    vinterp[:,i] = finterp(t)

vrms1 = vinterp[:,1] #Sudah dibhas dikelas online velocity 
m = len(vrms1)
vint = np.zeros((m-1,1))
tint = t[0:m-1] 

#Kolaborasi dan ide dari M. Kholis Fadhillah
for i in range (m-1):
    vint [i] = ((t[i+1]*(vrms1[i+1]*2)-t[i]*(vrms1[i]*2))/(t[i+1]-t[i]))*0.5
    
def dpth0(vint,t):
    return vint*t/2

def dpthn(vint,t,t2):
    return (vint*(t-t2))/2

dpth = np.zeros((m-1,1))
tdpth = t[0:m-1]

#Kolaborasi dan ide dari M. Kholis Fadhillah
for n in range (m-1):
    dpth[n] = dpth0(vint[0],t[0])
for n in range (m-1):
    if n == 0:
        continue
    elif n == 1:
        dpth[n] = dpth[n] + dpthn(vrms1[n],t[n],t[n-1])
    else:
        dpth[n] = dpth[n] + dpth[n-1] + dpthn(vrms1[n],t[n],t[n-1])

plt.figure()
plt.title("Grafik Time Vs Velocity Horizon A")
plt.pcolor(vinterp,cmap='hsv')
plt.colorbar()
plt.xlabel("Velocity")
plt.ylabel("Time")
plt.savefig('4a',dpi=300)

plt.figure()
plt.title("Grafik Time Vs Velocity Horizon A")
plt.plot (vrms1,t, label = 'Velocity1')
plt.plot(vint,tint,label = "Velocity2")
plt.xlabel("Velocity")
plt.ylabel("Time")
plt.grid()
plt.legend()
plt.savefig('4a1',dpi=300)

plt.figure()
plt.title("Grafik Depth Vs Velocity Horizon A")
plt.plot (vrms1,t, label = 'Velocity1')
plt.plot(dpth,tdpth,label = 'Velocity2')
plt.xlabel("Velocity")
plt.ylabel("Depth")
plt.grid()
plt.legend()
plt.savefig('4b',dpi=300)

plt.figure()
plt.title("Grafik Depth Vs Velocity Horizon A")
plt.pcolor(dpth,cmap='hsv')
plt.colorbar()
plt.xlabel("Velocity")
plt.ylabel("Depth")
plt.savefig('4b1',dpi=300)

#THANK YOU PAK AGUS

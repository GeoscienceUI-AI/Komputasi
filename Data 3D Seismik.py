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

plt.savefig('3D seismik.png', dpi=300)
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

figsize=(20,60) #Ukuran bingkai
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(f.trace.raw[:1500].T, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax) #Warna seismik
plt.title("Seismic Farstack") #raw = mengatur section saya ambil 0-1500 

figsize=(20,60)
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(attFN, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax) #ada referensi dari github tugas sebelumnya
plt.title("Attribute Far-Near Stack")

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

figsize=(10,10)
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(d2, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax)
plt.title("Attribute Far-Near stack TimeSlice 150")

figsize=(10,10)
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k', squeeze=False, sharex=True)
axs = axs.ravel()
im = axs[0].imshow(d3, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax)
plt.title("Attribute Far-Near stcak TimeSlice 250")

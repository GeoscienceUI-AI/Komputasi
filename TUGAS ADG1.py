# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:06:59 2020

Cara Running:
    1. File well1.csv 
    2. Script Py 
    3. Semuanya Harus Satu Folder
    4. Output berupa File PNG

@author: M. Dhery Mahendra
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def KoefRef(y,z):
    return (y - z)/(y + z)

def Ricker(f,t):
    pift = np.pi*f*t
    wav = (1 - 2*pift**2)*np.exp(-pift**2)
    return wav

def Conv(x,y):
    return 0
    

data = pd.read_csv("well1.csv")
d = data["Depth"]
GR = data["GR"]
rho = data["RHOB"]
v = data["Vel"]
z = v*rho

lstZ = []
for i in range(len(z)):
    lstZ.append(z[i])

#print(lstZ)    
y = []

for i in range(len(z)):
    count = z[i]+ 1
    y.append(count)    

lstValue = []
for i in range(len(y)):
    value = KoefRef(y[i],z[i])
    lstValue.append(value)

#print(lstValue)

LstFq = []
LstT = []
strt = -0.5
LstT.append(strt)
LstFq.append(Ricker(40,strt))
for i in range(500):
    strt += 0.002
    LstFq.append(Ricker(40,strt))
    LstT.append(strt)    

conv = np.convolve(lstValue,LstFq)

plt.figure(figsize = (3,30))
plt.subplot(5,1,1)
plt.title("Depth-Velocity")
plt.plot(v,d , 'g')
plt.grid()

plt.subplot(5,1,2)
plt.title("Depth-GR")
plt.plot(GR,d, 'r')
plt.grid()

plt.subplot(5,1,3)
plt.title("Depth-Rhob")
plt.plot(rho,d,'b')
plt.grid()

plt.subplot(5,1,4)
plt.title("Hasil Convolusi")
plt.plot(conv,'k')
plt.grid()

plt.subplot(5,1,5)
plt.title("Ricker Wavelet")
plt.plot(LstFq,LstT)
plt.grid()

plt.savefig('GRAFIK_ADG1_DHERY.png',dpi=300)
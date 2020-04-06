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

plt.figure()
plt.title("Grafik Time Vs Velocity Horizon A")
plt.plot (vrms1,t, label = 'Velocity1')
plt.plot(vint,tint,label = "Velocity2")
plt.xlabel("Velocity")
plt.ylabel("Time")
plt.grid()
plt.legend()

plt.figure()
plt.title("Grafik Depth Vs Velocity Horizon A")
plt.plot (vrms1,t, label = 'Velocity1')
plt.plot(dpth,tdpth,label = 'Velocity2')
plt.xlabel("Velocity")
plt.ylabel("Depth")
plt.grid()
plt.legend()

plt.figure()
plt.title("Grafik Depth Vs Velocity Horizon A")
plt.pcolor(dpth,cmap='hsv')
plt.colorbar()
plt.xlabel("Velocity")
plt.ylabel("Depth")


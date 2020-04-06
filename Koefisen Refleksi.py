#
#BATAS NOMOR
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("koefisen_refleksi.csv") #Input Data CSV
kr = data["cr"] #Mengambil Data Koef Refleksi
tetha = np.arange(0, 46, 1) #Membuat Fungsi sudut datang 0-45 derajat

plt.plot(tetha, kr, "r")
plt.title("Koef Refleksi Vs Sudut Datang")
plt.xlabel("Sudut Datang(Tetha)")
plt.ylabel("Koefisien Refleksi")
plt.grid()

plt.savefig('GRAFIK_ADG1_DHERY.png',dpi=300)

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

print(pois1,pois2,r0)


import segyio
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

xx, yy = np.meshgrid(np.linspace(0,81,80), np.linspace(0,81,80))
X =  xx
Y =  yy
Z =  10*np.ones(X.shape)
xx1, yy1 = np.meshgrid(np.linspace(0,119,80), np.linspace(0,119,80))
X1 = xx1
Y1 = yy1
Z1 = 1*(10*np.ones(X1.shape))
xx2, yy2 = np.meshgrid(np.linspace(0,151,80), np.linspace(0,151,80))
X2 = xx2
Y2 = yy2
Z2 = 10*np.ones(X2.shape)
file = 'contoh.sgy'

c = segyio.open(file, "r+",ignore_geometry=True)

b = (c.trace.raw[:]).T

d = np.reshape(b,[151,119,81])
d1 = d[:,:,1]
d2 = d[:,1,:]
d3 = d[1,:,:]
#4= np.squeeze(d1, axis = 0)
fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax = fig.gca(projection='3d')
#ax.contour3D(d1,d2,d3, 50, cmap='binary')
'''ax.plot_surface(d1, d2, d3, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
'''
xb=np.linspace(1,81,81)
YB=75*np.ones((151,81))
zb=np.linspace(1,151,151)
XB,ZB = np.meshgrid(xb,zb)

xc=np.linspace(1,81,81)
YC=75*np.ones((119,81))
zc=np.linspace(1,119,119)
XC,ZC = np.meshgrid(xc,zc)

ax1 = fig.add_subplot(121)
ax1.imshow(d2, cmap=plt.cm.BrBG, interpolation='nearest', origin='lower', extent=[0,1,0,1])
ax2 = fig.add_subplot(122, projection='3d')
ax3 = ax2.plot_surface(X2,Y2,Z2+75, rstride=1, cstride=1, facecolors=plt.cm.BrBG(d3), shade=False)
#ax2 = fig.add_subplot(133, projection='3d')
ax4 = ax2.plot_surface(XB,YB,ZB, rstride=1, cstride=1, facecolors=plt.cm.BrBG(d2), shade=False)
ax5 = ax2.plot_surface(YC,XC,ZC, rstride=1, cstride=1, facecolors=plt.cm.BrBG(d1), shade=False)
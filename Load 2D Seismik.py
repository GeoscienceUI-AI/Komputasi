# -*- coding: utf-8 -*-
"""
Program Untuk Menampilan 2D Seismik

Created on Fri Feb 14 10:39:47 2020

@author: Muhammad Dhery Mahendra
"""

import matplotlib.pyplot as plt
import segyio 

segyfile = "ST9715-206.sgy"

f = segyio.open(segyfile, ignore_geometry=True)

# Set up a figure and plot a few shot gathers

clip = 100e+2 #Warna Seismik
vmin, vmax = -clip, clip

# Figure

figsize=(20, 60) #ukuranAI
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize, facecolor='w', edgecolor='k',
                       squeeze=False,
                       sharex=True)
#subplot bikin beberapa gambar
axs = axs.ravel()
im = axs[0].imshow(f.trace.raw[:] .T, cmap=plt.cm.seismic, vmin=vmin, vmax=vmax)

plt.savefig('GRAFIK_Seimik_MDM.png',dpi=800)
#raw = mengatur section
###############################################################################
# Close the file

f.close()



from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
dir_graphics="Graphics/"
im=Image.open("Images/Imagen.tif")
f=np.fft.fft2(im)
f=np.fft.fftshift(f)
f=np.log(np.abs(f))
fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(10,5))
ax1.imshow(im)
ax2.imshow(f)
ax3.imshow(1000*f,cmap="binary")
ax1.set_title("Imagen original")
ax2.set_title("FFT")
ax3.set_title("FFT B/N")
ax3.plot([6.5,63.3],[247.4,247.4],color="black",lw=4)
ax3.text(2,238,"5  1nm$^{-1}$",fontsize=26)
ax2.plot([6.5,63.3],[247.4,247.4],color="black",lw=4)
ax2.text(2,238,"5 1nm$^{-1}$",fontsize=26)
for ax in (ax1,ax2,ax3):
    ax.set_xticks([]);ax.set_yticks([])
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.188)
plt.savefig(dir_graphics+"FFT.png")
plt.show()
plt.clf()
hexa_x,hexa_y=np.loadtxt("Data/hexa.csv",delimiter=",",unpack=True)
n=np.size(hexa_x)
plt.imshow(1000*f)
plt.axis("off")
for i in range(n):
    j=i+1
    if j==n: j=0
    pos=[i,j]
    plt.plot(hexa_x[pos],hexa_y[pos],lw=3,color="black")
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
plt.savefig(dir_graphics+"hexa.png",dpi=200)
plt.show()
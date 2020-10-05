from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

def plot_image(image,path,name,cmap=None,bar=True):
    plt.axis("off")
    plt.imshow(image,cmap=cmap)
    if bar:
        plt.plot([6.5,63.3],[247.4,247.4],color="black",lw=4)
        plt.text(2,238,"5  1nm$^{-1}$",fontsize=26)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.188)
    plt.savefig(path+name,dpi=200)
    if name=='hexa.png':
        plt.show()
    plt.clf()

dir_graphics="Graphics/"
im=Image.open("Images/Imagen.tif")
f=np.fft.fft2(im)
f=np.fft.fftshift(f)
f=np.log(np.abs(f))
plot_image(im,dir_graphics,"Original.png",bar=False)
plot_image(1000*f,dir_graphics,"FFTBN.png",cmap="binary",bar=True)
plot_image(f,dir_graphics,"FFT.png",bar=True)
hexa_x,hexa_y=np.loadtxt("Data/hexa.csv",delimiter=",",unpack=True)
n=np.size(hexa_x)
for i in range(n):
    j=i+1
    if j==n: j=0
    pos=[i,j]
    plt.plot(hexa_x[pos],hexa_y[pos],lw=3,color="black")
plot_image(1000*f,dir_graphics,"hexa.png")
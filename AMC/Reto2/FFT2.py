from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

def plot_image(image,cmap=None,bar=True):
    plt.axis("off")
    plt.imshow(image,cmap=cmap)
    if bar:
        plt.plot([6.5,63.3],[247.4,247.4],color="black",lw=4)
        plt.text(2,238,"5  1nm$^{-1}$",fontsize=26)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.188)
    plt.show()
    plt.clf()

im=Image.open("Imagen.tif")
f=np.fft.fft2(im)
f=np.fft.fftshift(f)
f=np.log(np.abs(f))
plot_image(im,bar=False)
plot_image(1000*f,bar=True)
plot_image(f,bar=True)
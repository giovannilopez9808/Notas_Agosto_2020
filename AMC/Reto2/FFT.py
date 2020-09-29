from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
tamaño=(5,5)
coeficientes = [0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2,  16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0]
factor = 1
im=Image.open("Images/Imagen.tif")
ima=im.filter(ImageFilter.Kernel(tamaño, coeficientes, factor))
plt.imshow(ima)
plt.show()
f=np.fft.fft2(im)
f=np.fft.fftshift(f)
f=20*np.log(np.abs(f))
imagen_procesada = imagen_original.filter(ImageFilter.Kernel(tamaño, coeficientes, factor))
print(np.max(f),np.min(f))
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(8,5))
ax1.imshow(im)
ax2.imshow(f,cmap="binary")
ax1.set_title("Imagen original")
ax2.set_title("FFT")
ax2.plot([6.5,63.3],[247.4,247.4],color="black",lw=6)
ax2.text(2,238,"2 nm",fontsize=32)
for ax in (ax1,ax2):
    ax.set_xticks([]);ax.set_yticks([])
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.188)
plt.savefig("Graphics/FFT.png")
plt.show()
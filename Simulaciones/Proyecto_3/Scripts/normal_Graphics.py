import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
dir_graphics="../Graphics/"
os.system("gfortran Normal_dis.f -o a.out && ./a.out")
data=np.loadtxt("data.txt")
os.system("rm data.txt && rm a.out")
plt.hist(data,bins=125,color="#d00000",alpha=0.65,label="Datos")
xmin,xmax=plt.xlim()
mu, std = norm.fit(data)
x = np.linspace(xmin,xmax, 100)
p = norm.pdf(x, mu, std)*10**(4)
plt.plot(x,p,lw=3,color="#f48c06",label="Fit")
plt.ylim(0,3500)
plt.ylabel("Conteo")
plt.xlabel("Valores de la distribución")
plt.legend(frameon=False,ncol=2,mode="expand")
plt.subplots_adjust(left=0.114,bottom=0.112,right=0.96,top=0.929)
plt.savefig(dir_graphics+"norm.png",dpi=200)
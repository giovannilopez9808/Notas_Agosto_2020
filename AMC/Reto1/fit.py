import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import constants as C
#<------------------------Funcion de la radiacion de cuerpo negro------------------>
def black_body_freq(v,T):
    a=2*h*v**3/c**2
    b=h*v/(k*T)
    i=a/(np.exp(b)-1)
    return i
#<-----------------------Constante de Boltzmann------------------------------------>
c=C.c;k=C.Boltzmann;h=C.h;pi=np.pi
#<----------------------Lectura de los datos----------------------------------->
lon,spec=np.loadtxt("data.txt",unpack=True,skiprows=18,usecols=[0,1])
#<-------------Convertir unidades de medicion------------------------->
freq=(lon*100)*c
spec2=spec*1e-20
#<-----------------------Fit------------------------------------------->
pars, cov = curve_fit(f=black_body_freq,xdata=freq,ydata=spec2,p0=[5])
fit=black_body_freq(freq,pars[0])
print(cov)
#<---------------------------------Inicio de la grafica----------------------------->
plt.xlabel("Frequency (GHz)")
plt.ylabel("Intensity (MJy/sr)")
plt.ylim(0,450)
plt.xlim(0,700)
plt.scatter(freq*1e-9,spec2*1e20,marker="o",label="COBE data")
plt.plot(freq*1e-9,fit*1e20,label="Fit",color="green")
plt.legend(ncol=2,mode="expand",frameon=False)
plt.savefig("Graphics/fit.png")
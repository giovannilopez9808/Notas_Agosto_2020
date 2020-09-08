import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as C
#<------------------------Funcion de la radiacion de cuerpo negro------------------>
def black_body_freq(v,T):
    a=2*h*v**3/c**2
    b=h*v/(k*T)
    i=a/(np.exp(b)-1)
    return i
#<---Funcion de la radiación de cuerpo negro propuesta por Rayleigh y Jeans---------->
def black_body_no(v,T):
    i=2*T*k*v**2/c**2
    return i 
#<-----------------------Constantes--------------------------------------------->
c=C.c;k=C.Boltzmann;h=C.h;pi=np.pi
#<------------------------------Calculo para diferentes temperaturas----------------------------->
lon=np.arange(0.2,12,0.01)*1e-6
#<--------------------------Longitudes a frecuencias----------------------------------------->
freq=c/lon
lon=lon*1e9
T=5000
spec_black=black_body_freq(freq,T)*1e10
spec_rayleigh=black_body_no(freq,T)*1e10
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.179,top=0.902)
plt.plot(lon,spec_black,lw="2",color="#dd2d4a",label="Black Body Equation Plank")
plt.plot(lon,spec_rayleigh,lw="2",color="#023e7d",label="Black Body Equation Rayleigh-Jeans")
plt.ylim(0,300)
plt.xlim(200,12000)
plt.yticks(np.arange(0,325,25))
plt.xticks(np.arange(200,12000+1000,1000),rotation=60)
plt.legend(frameon=False)
plt.ylabel("Intensity (MJy/sr)")
plt.xlabel("Wavelength (nm)")
plt.savefig("Graphics/exp_vs_teo.png",dpi=100)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import constants as C
from sklearn.metrics import r2_score
#<------------------------Funcion de la radiacion de cuerpo negro------------------>
def black_body_freq(v,T):
    a=2*h*v**3/c**2
    b=h*v/(k*T)
    i=a/(np.exp(b)-1)
    return i
#<-----------------------Constantes--------------------------------------------->
c=C.c;k=C.Boltzmann;h=C.h;pi=np.pi
#<----------------------Lectura de los datos----------------------------------->
lon,spec=np.loadtxt("data.txt",unpack=True,skiprows=18,usecols=[0,1])
#<-------------Convertir unidades de medicion------------------------>
#<----------------------cm^-1 -> Hz------------------------------------>
freq=(lon*100)*c
#<---------------------Mjy/sr -> W/m2srHz----------------------------------------->
spec=spec*1e-20
#<-----------------------Fit------------------------------------------->
pars,cov=curve_fit(f=black_body_freq,xdata=freq,ydata=spec,p0=[5])
fit=black_body_freq(freq,pars[0])
#<------------------------------W/m2srHZ -> Mjy/sr----------------------------------------->
spec=spec*10**(26-6)
fit=fit*10**(26-6)
#<---------------------------Hz -> Gz--------------------------------------->
freq=freq*1e-9
#<---------------------------------Inicio de la grafica----------------------------->
plt.xlabel("Frequency (GHz)")
plt.ylabel("Intensity (MJy/sr)")
plt.ylim(0,425)
plt.xlim(0,650)
plt.scatter(freq,spec,marker="o",label="COBE data",c="#f48c06")
plt.plot(freq,fit,label="Fit",color="#370617",lw="2")
plt.legend(ncol=2,mode="expand",frameon=False)
plt.grid(ls="--",color="grey")
plt.savefig("Graphics/fit.png",dpi=100)
plt.clf()
#<---------------------------Calculo de la diferencia relativa--------------------->
var=(np.abs(spec-fit))/spec
#<-----------------------------Calculo de la R2---------------------------------->
r2=r2_score(spec,fit)
print("Temperatura de fit",pars[0])
print("La diferencia relativa es",round(np.mean(var)*100,4))
print("El coeficiente de determinacion es",r2)
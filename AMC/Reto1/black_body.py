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
#<------------------------------Calculo para diferentes temperaturas----------------------------->
lon=np.arange(0.2,3.2,0.01)*1e-6
#<--------------------------Longitudes a frecuencias----------------------------------------->
freq=c/lon
#<---------------------------Lista de temperaturas----------------------------->
T_list=[3000,3500,4000,4500,5000,5500,6000]
T_color=["F48C06","e85d04","DC2F02","9D0208","6A040F","370617","03071E"]
max_lon=[];max_spec=[]
for T,color in zip(T_list,T_color):
    spec=black_body_freq(freq,T)
    #<------------------------------W/m2srHZ -> PBjy/sr----------------------------------------->
    spec=spec*10**(26-15)
    #<--------------------------Localizacion del especto maximo--------------------------------->
    max_point=np.max(spec)
    max_spec=np.append(max_spec,max_point)
    #<--------------------------------Localizacion de la localizacion---------------------------------->
    loc=np.where(max_point==spec)[0]
    max_lon=np.append(max_lon,lon[loc]*1e9)
    #<------------------------------------Grafica de cada temperatura------------------------------->
    plt.plot(lon*1e9,spec,label=str(T)+" K",lw="4",color="#"+color)
plt.plot(max_lon,max_spec,label="Ley de Wien",color="#2b2d42",ls="--")
plt.ylabel("Intensity (PBJy/sr)")
plt.xlabel("Wavelength (nm)")
plt.xlim(200,3200)
plt.ylim(0,5000)
plt.xticks(np.arange(200,3700,500))
plt.yticks(np.arange(0,5500,500))
plt.legend(frameon=False,mode="expand",ncol=4)
plt.savefig("Graphics/black_body.png",dpi=100)
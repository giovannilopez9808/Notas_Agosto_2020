import numpy as np
import matplotlib.pyplot as plt
#<---------------------------Funcion para graficar----------------->
def plot(ax,energy,color,ylabel,yticks,max):
    ax.set_xlim(0,max)
    ax.set_ylabel(ylabel)
    ax.plot(walks,energy,color=color,lw=3)
    if ax!=ax3:
        ax.set_xticks([])
    ax.set_yticks(yticks)
#<----------------------------Direcciones de los archivos-------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
#<-_----------------------Grafica de la energía--------------------------------->
walks,e_kin,e_pot=np.loadtxt(dir_results+"8_T_U_P.dat",unpack=True,usecols=[0,1,2])
max_walks=np.max(walks)
e_pot=e_pot*1e3
e_tol=e_pot+e_kin
fig,(ax1,ax2,ax3)=plt.subplots(3,figsize=(9,7))
#<---------------------------Dimensiones de la grafica-------------------------->
plt.subplots_adjust(left=0.114,right=0.952,bottom=.124,top= 0.938)
#<--------------------------Ploteo de cada energia con sus parametros----------------------->
plot(ax1,e_kin,"#8d0801","Kinetic energy",np.arange(0.9,1.02,0.02),max_walks)
plot(ax2,e_pot,"#001427","Potencial energy",np.arange(-1,-0.87,0.02),max_walks)
plot(ax3,e_tol,"#1b4332","Total energy",np.arange(-0.05,0.07,0.02),max_walks)
plt.xlabel("Walks")
plt.savefig(dir_graphics+"Energy.png")
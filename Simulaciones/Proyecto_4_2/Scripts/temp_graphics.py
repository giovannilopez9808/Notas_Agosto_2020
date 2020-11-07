import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import matplotlib.pyplot as plt
#<---------------------Direccion de los archivos-------------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
colors=["b76935","a56336","935e38","6f523b","5c4d3c","4a473e","38413f","263c41","143642"]
n=9;n_particle=np.arange(100,1000,100)
fig,axs=plt.subplots(3,3,figsize=(12,8))
axs=np.reshape(axs,9)
for i,ax,color in zip(range(n),axs,colors):
    print("Calculando temperatura de "+str(i))
    n_part=n_particle[i]
    #<----------------------------------Pasos-------------------------------->
    walks,ekin_list=np.loadtxt(dir_results+"8_T_U_P_"+str(i)+".dat",usecols=[0,1],unpack=True)
    file=open(dir_results+"temp_"+str(i)+".dat","w")
    for walk,ekin in zip(walks,ekin_list):
        temp=ekin/(3*n_part)
        file.write(str(walk)+" "+str(temp)+"\n")
    file.close()
    temp=np.loadtxt(dir_results+"temp_"+str(i)+".dat",usecols=1)
    ax.set_xlim(0,2e5)
    ax.set_title("Número de partículas: "+str(n_particle[i]))
    if ax in [axs[6],axs[7],axs[8]]:
        ax.set_xticks(np.arange(0,2e5+0.4e5,0.4e5))
        ax.set_xticklabels(np.round(np.arange(0,2+0.4,0.4),2))
    else:
        ax.set_xticks([])
    ax.plot(walks,temp,color="#"+color)
#<------------------------Label eje x---------------------------------------->
fig.text(0.5, 0.04, 'Walks (10$^{5}$)', ha='center',fontsize=13)
#<--------------------------Label en el eje y-------------------------------------------->
fig.text(0.03, 0.5, 'Temperatura (10$^{-3}$)', va='center', rotation='vertical',fontsize=13)
plt.subplots_adjust(left=0.107,bottom=0.11,right=0.945,top=0.952,wspace=0.275,hspace=0.214)
plt.savefig(dir_graphics+"temp.png",dpi=200)
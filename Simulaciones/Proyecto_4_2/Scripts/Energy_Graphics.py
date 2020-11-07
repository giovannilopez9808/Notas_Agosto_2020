import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
colors=["b76935","a56336","935e38","6f523b","5c4d3c","4a473e","38413f","263c41","143642"]
n=9;n_particle=np.arange(100,1000,100)
#<-------------Divisiones de las graficas---------------------------->
fig,axs=plt.subplots(3,3,figsize=(12,8))
axs=np.reshape(axs,9)
for i,ax,color in zip(range(n),axs,colors):
    #<------------------Lectura de los datos------------------------->
    walks,e_pot=np.loadtxt(dir_results+"8_T_U_P_"+str(i)+".dat",unpack=True,usecols=[0,2])
    e_pot=e_pot*1e2
    ax.plot(walks,e_pot,color="#"+color)
    ax.set_xlim(0,2e5)
    ax.set_title("Número de partículas "+str(n_particle[i]))
    # #<-----------------------Añadir label del eje x a las ultimas tres------------------>
    if ax in [axs[6],axs[7],axs[8]]:
        ax.set_xticks(np.arange(0,2e5+0.4e5,0.4e5))
        ax.set_xticklabels(np.round(np.arange(0,2+0.4,0.4),2))
    else:
        ax.set_xticks([])
#<------------------------Label eje x---------------------------------------->
fig.text(0.5, 0.04, 'Walks (10$^{5}$)', ha='center',fontsize=13)
#<--------------------------Label en el eje y-------------------------------------------->
fig.text(0.04, 0.5, 'U(10$^{2}$)', va='center', rotation='vertical',fontsize=13)
plt.subplots_adjust(left=0.107,bottom=0.11,right=0.945,top=0.952,wspace=0.28,hspace=0.214)
plt.savefig(dir_graphics+"energy.png",dpi=200)
import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir="../Results_2/";dir_graphics="../Graphics/"
rho_values=np.round(np.array([0.3,0.6,0.8]),2)
temp_values=np.round(np.arange(0.3,1.3,0.2),2)
#<-----------------------------Colores de las graficas--------------------->
fig,axs_total=plt.subplots(5,3,figsize=(12,7))
axs_total=np.transpose(axs_total)
colors=["#03071e","#6a040f","#9d0208","#e85d04","#faa307"]
for rho,axs in zip(rho_values,axs_total):
    for t,ax,color in zip(temp_values,axs,colors):
        #<------------------Lectura de los datos------------------------->
        version="8_T_U_P_"+str(rho)+"_"+str(t)+".dat"
        walks,e_kin,e_pot=np.loadtxt(dir+version,unpack=True,usecols=[0,1,2])
        e_tol=e_pot*1e3+e_kin
        walks=walks*1e-4
        ax.plot(walks,e_tol,color=color)
        min=np.min(e_tol)
        max=np.max(e_tol)
        yticks=np.round(np.linspace(min,max,5),2)
        ax.set_yticks(yticks)
        #<-----------------Añadir el titulo centrado---------------------->
        if ax==axs[0]:
             ax.set_title("$\\rho=$"+str(rho))
        #<-----------------------Añadir label del eje x a las ultimas tres------------------>
        if ax==axs[-1]:
            ax.set_xticks(np.arange(0,2+0.5,0.5))
        else:
            ax.set_xticks([])
        if axs in axs_total[0]:
            ax.set_ylabel("$T=$"+str(t))
        #<-----------------------------------Guardado de la gráfica------------------------->
fig.text(0.5, 0.04, 'Walks (10$^{3}$)', ha='center',fontsize=14)
fig.text(0.04, 0.5, 'Energía total', va='center', rotation='vertical',fontsize=14)
plt.savefig(dir_graphics+"Energy.png",dpi=200)
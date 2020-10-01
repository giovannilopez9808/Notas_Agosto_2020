import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir="../Results/";dir_graphics="../Graphics/"
rho_values=np.round(np.array([0.3,0.6,0.8]),2)
temp_values=np.round(np.arange(0.3,1.3,0.2),2)
#<-----------------------------Colores de las graficas--------------------->
fig,axs_total=plt.subplots(5,3,figsize=(12,7))
axs_total=np.transpose(axs_total)
colors=["#03071e","#6a040f","#9d0208","#e85d04","#faa307"]
lim_list=[[0.25,0.4,0.05],[0.4,0.6,0.05],[0.4,0.8,0.1],[0.6,1,0.1],[0.8,1.4,0.2]]
for rho,axs in zip(rho_values,axs_total):
    for t,ax,color,lim in zip(temp_values,axs,colors,lim_list):
        #<------------------Lectura de los datos------------------------->
        version="temp_"+str(rho)+"_"+str(t)+".dat"
        walks,temp=np.loadtxt(dir+version,unpack=True)
        walks=walks*1e-4
        ax.plot(walks,temp,color=color,lw=3)
        ax.set_ylim(lim[0],lim[1])
        ax.set_yticks(np.round(np.arange(lim[0],lim[1]+lim[2],lim[2]),2))
        ax.set_xlim(walks[0],walks[-1])
        ax.plot([walks[0],walks[-1]],[t,t],ls="--",color="green")
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
fig.text(0.04, 0.5, 'Temperatura', va='center', rotation='vertical',fontsize=14)
plt.savefig(dir_graphics+"Temp.png",dpi=200)
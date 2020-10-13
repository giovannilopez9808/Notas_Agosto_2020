import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir="../Results/";dir_graphics="../Graphics/"
rho_values=np.round(np.arange(0.4,0.8,0.1),2)
#<-----------------------------Colores de las graficas--------------------->
fig,axs=plt.subplots(2,2,figsize=(8,6))
axs=np.reshape(axs,4)
colors=["#03071e","#6a040f","#dc2f02","#f48c06"]
x_lim=[0,26,2]
xtick=np.arange(x_lim[0],x_lim[1]+x_lim[2],x_lim[2])
for rho,ax,color in zip(rho_values,axs,colors):
    #<------------------Lectura de los datos------------------------->
    version="8_T_U_P_"+str(rho)+".dat"
    walks,e_kin,e_pot=np.loadtxt(dir+version,unpack=True,usecols=[0,1,2],max_rows=130)
    e_tol=e_pot*1e3+e_kin
    walks=walks*1e-2
    ax.plot(walks,e_tol,color=color)
    min=np.min(e_tol)
    max=np.max(e_tol)
    yticks=np.round(np.linspace(min,max,5),2)
    ax.set_yticks(yticks)
    ax.set_ylim(yticks[0],yticks[-1])
    ax.set_xlim(0,26)
    #<-----------------Añadir el titulo centrado---------------------->
    ax.set_title("$\\rho=$"+str(rho))
    #<-----------------------Añadir label del eje x a las ultimas dos------------------>
    if ax in [axs[2],axs[-1]]:
        ax.set_xticks(xtick)
    else:
        ax.set_xticks([])
    for x in xtick:
        #<------------------------Linea vertical-------------------------------------------->
        ax.plot([x,x],[yticks[0],yticks[-1]],ls="--",color="black",alpha=0.5)
    for y in yticks:
        #<---------------------Linea horizontal----------------------------------------->
        ax.plot([xtick[0],xtick[-1]],[y,y],ls="--",color="black",alpha=0.5)  
        #<-----------------------------------Guardado de la gráfica------------------------->
fig.text(0.5, 0.04, 'Walks (10$^{2}$)', ha='center',fontsize=14)
fig.text(0.04, 0.5, 'Energía total', va='center', rotation='vertical',fontsize=14)
plt.subplots_adjust(left=0.145,bottom=0.114,right=0.96,top=0.938,wspace=0.2,hspace=0.2)
plt.savefig(dir_graphics+"Energy.png",dpi=200)
plt.show()
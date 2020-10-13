import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
#<-----------------------------------------Densidades----------------------------->
rho_values=np.round(np.arange(0.4,0.8,0.1),2)
colors=["#03071e","#6a040f","#dc2f02","#f48c06"]
fig,axs=plt.subplots(2,2,figsize=(8,6))
axs=np.reshape(axs,4)
#<--------------------------------------Limites de las graficas y ticks------------------------------>
x_lim=[0.9,4.9];y_lim=[0,8];delta=[0.6,1]
#<-----------------------------------Definicion de valores de ticks---------------------------->
xtick=np.arange(x_lim[0],x_lim[1]+delta[0],delta[1]);ytick=np.arange(y_lim[0],y_lim[1]+delta[1],delta[1])
for rho,ax,color in zip(rho_values,axs,colors):
    #<------------------------------------Grafica de la distribucion radial------------------------->
    r,hist=np.loadtxt(dir_results+"4_hr_"+str(rho)+".dat",unpack=True)
    #<-----------------------------------Grafica de R2------------------------------------>
    ax.plot(r,hist,color=color,lw=3)
    ax.set_title("$\\rho=$"+str(rho))
    #<----------------------------------------------Limits de las graficas------------------------>
    ax.set_xlim(x_lim[0],x_lim[1]);ax.set_ylim(y_lim[0],y_lim[1])
    if ax in [axs[0],axs[2]]:
        ax.set_yticks(ytick)
    else:
        ax.set_yticks([])
    if ax in [axs[2],axs[3]]:
        ax.set_xticks(xtick)
    else:
        ax.set_xticks([])
    #<------------------------------Creacion del grid------------------------------------>
    for x in xtick:
        #<------------------------Linea vertical-------------------------------------------->
        ax.plot([x,x],[ytick[0],ytick[-1]],ls="--",color="black",alpha=0.5)
    for y in ytick:
        #<---------------------Linea horizontal----------------------------------------->
        ax.plot([xtick[0],xtick[-1]],[y,y],ls="--",color="black",alpha=0.5)
#<----------------------------Titulo del eje x en medio-------------------------->
lines,labels=fig.axes[-1].get_legend_handles_labels()
#<----------------------------------Shared xlabel---------------------------->
fig.text(0.5, 0.04, 'Distancia radial (r)', ha='center',fontsize=14)
fig.text(0.015, 0.5, "$ \\rho (r)$", va='center', rotation='vertical',fontsize=14)
fig.legend(lines, labels, loc = 'upper center',ncol=5,frameon=False)
plt.subplots_adjust(left=0.074, bottom=0.121, right=0.964, top=0.91, wspace=0.083, hspace=0.15)
plt.savefig(dir_graphics+"Dis_rad.png",dpi=300)
plt.show()
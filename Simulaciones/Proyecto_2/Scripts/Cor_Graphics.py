import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results2="../Results_2/";dir_graphics="../Graphics/"
#<-----------------------------------------Densidades----------------------------->
rho_values=np.round(np.array([0.3,0.6,0.8]),2)
temp_values=np.round(np.arange(0.3,1.3,0.2),2)
colors=["#03071e","#6a040f","#d00000","#e85d04","#faa307"]
fig,axs=plt.subplots(1,3,figsize=(14,5))
axs=np.reshape(axs,3)
#<--------------------------------------Limites de las graficas y ticks------------------------------>
x_lim=[0.9,4.9];y_lim=[0,6];delta=[0.6,1]
#<-----------------------------------Definicion de valores de ticks---------------------------->
xtick=np.arange(x_lim[0],x_lim[1]+delta[0],delta[1]);ytick=np.arange(y_lim[0],y_lim[1]+delta[1],delta[1])
for rho,ax in zip(rho_values,axs):
    for t,color in zip(temp_values,colors):
        #<------------------------------------Grafica de la distribucion radial------------------------->
        r2,hist2=np.loadtxt(dir_results2+"4_hr_"+str(rho)+"_"+str(t)+".dat",unpack=True)
        #<-----------------------------------Grafica de R2------------------------------------>
        ax.plot(r2,hist2,color=color,label="T="+str(t),lw=2,alpha=0.7)
        ax.set_title("$\\rho=$"+str(rho))
        #<----------------------------------------------Limits de las graficas------------------------>
        ax.set_xlim(x_lim[0],x_lim[1]);ax.set_ylim(y_lim[0],y_lim[1])
        if ax==axs[0]:
            ax.set_yticks(ytick)
            ax.set_ylabel("$ \\rho (r)$",fontsize=14)
        else:
            ax.set_yticks([])
        ax.set_xticks(xtick)
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
fig.legend(lines, labels, loc = 'upper center',ncol=5,frameon=False)
plt.subplots_adjust(left=0.08, bottom=0.174, right=0.92, top=0.88, wspace=0.11, hspace=0.188)
plt.savefig(dir_graphics+"Dis_rad.png",dpi=300)
plt.show()
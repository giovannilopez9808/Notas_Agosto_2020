import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir="../Results/";dir_graphics="../Graphics/"
#<------------------------Valores de rho----------------------------------->
rho_values=np.round(np.arange(0.4,0.8,0.1),2)
#<-----------------------------Colores de las graficas--------------------->
fig,axs=plt.subplots(2,2,figsize=(8,6))
axs=np.reshape(axs,4)
#<-.-----------------------Colores de las graficas-------------------------------->
colors=["#03071e","#6a040f","#dc2f02","#f48c06"]
#<-------------------Lista de los limites de las graficas------------------------->
x_lim,y_lim=[0,26,2],[1,3,0.5]
xtick=np.arange(x_lim[0],x_lim[1]+x_lim[2],x_lim[2])
ytick=np.arange(y_lim[0],y_lim[1]+y_lim[2],y_lim[2])
for rho,ax,color in zip(rho_values,axs,colors):
    #<------------------Lectura de los datos------------------------->
    version="temp_"+str(rho)+".dat"
    walks,temp=np.loadtxt(dir+version,unpack=True,max_rows=2600)
    walks=walks*1e-2
    #<---------------------Ploteo de la grafica------------------------->
    ax.plot(walks,temp,color=color,lw=3)
    ax.set_ylim(y_lim[0],y_lim[1])
    #<---------------------Ticks en y--------------------------------------->
    ax.set_yticks(ytick)
    #<-----------------Añadir el titulo centrado---------------------->
    ax.set_title("$\\rho=$"+str(rho))
    #<-----------------------Añadir label del eje x a las ultimas tres------------------>
    ax.set_xlim(x_lim[0],x_lim[1])
    if ax in [axs[2],axs[-1]]:
        ax.set_xticks(xtick)
    else:
        ax.set_xticks([])
    if ax in [axs[0],axs[2]]:
        ax.set_yticks(ytick)
    else:
        ax.set_yticks([])
  #<------------------------------Creacion del grid------------------------------------>
    for x in xtick:
        #<------------------------Linea vertical-------------------------------------------->
        ax.plot([x,x],[ytick[0],ytick[-1]],ls="--",color="black",alpha=0.5)
    for y in ytick:
        #<---------------------Linea horizontal----------------------------------------->
        ax.plot([xtick[0],xtick[-1]],[y,y],ls="--",color="black",alpha=0.5)   
#<------------------------Label eje x---------------------------------------->
fig.text(0.55, 0.04, 'Walks (10$^{2}$)', ha='center',fontsize=14)
#<--------------------------Label en el eje y-------------------------------------------->
fig.text(0.04, 0.5, 'Temperatura', va='center', rotation='vertical',fontsize=14)
plt.subplots_adjust(left=0.114,bottom=0.114,right=0.955,top=0.938,wspace=0.067,hspace=0.2)
plt.savefig(dir_graphics+"Temp.png",dpi=200)
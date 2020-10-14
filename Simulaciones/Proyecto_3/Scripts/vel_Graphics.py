import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
#<----------------------------Direcciones de los archivos-------------------->
dir="../Results/";dir_graphics="../Graphics/"
rho_values=np.round(np.arange(0.4,0.8,0.1),2)
colors=["#03071e","#6a040f","#dc2f02","#f48c06"]
n_pasos=20
n_part=784
fig,axs=plt.subplots(2,2,figsize=(8,6))
axs=np.reshape(axs,4)
x_lim,y_lim=[-4,4,1],[0,3500,500]
xtick=np.arange(x_lim[0],x_lim[1]+x_lim[2],x_lim[2])
ytick=np.arange(y_lim[0],y_lim[1]+y_lim[2],y_lim[2])
for rho,ax,color in zip(rho_values,axs,colors):
    vel=[]
    for i in range(n_pasos):
        data_x,data_y=np.loadtxt(dir+"2_velo_"+str(rho)+".dat",unpack=True,skiprows=i*(n_part+1)+1,max_rows=n_part)
        vel=np.append(vel,data_x)
        vel=np.append(vel,data_y)
    ax.hist(vel,bins=25,color=color,label="Data")
    ax.set_ylim(y_lim[0],y_lim[1])
    mu, std = norm.fit(vel)
    x = np.linspace(x_lim[0],x_lim[1], 100)
    p = norm.pdf(x, mu, std)*10**(4)
    ax.plot(x,p,lw=3,color="#f48c06",label="Fit")
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
    for y in ytick:
    #<---------------------Linea horizontal----------------------------------------->
        ax.plot([xtick[0],xtick[-1]],[y+250,y+250],ls="--",color="black",alpha=0.5)  
        ax.plot([xtick[0],xtick[-1]],[y,y],ls="--",color="black",alpha=0.5)
#<------------------------Label eje x---------------------------------------->
fig.text(0.55, 0.04, 'Velocidades', ha='center',fontsize=14)
#<--------------------------Label en el eje y-------------------------------------------->
fig.text(0.02, 0.5, 'Conteo', va='center', rotation='vertical',fontsize=14)
plt.subplots_adjust(left=0.114,bottom=0.114,right=0.955,top=0.938,wspace=0.067,hspace=0.2)
plt.savefig(dir_graphics+"vel.png",dpi=200)
plt.show()
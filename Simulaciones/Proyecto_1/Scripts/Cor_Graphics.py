import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results2="../Results_2/";dir_graphics="../Graphics/";dir_results3="../Results_3/"
#<-----------------------------------------Densidades----------------------------->
rho_values=np.round(np.arange(0.1,1 ,0.1),2)
for rho in rho_values:
    rho=0.1
    #<------------------Grafica la posicion inicial---------------------------------->
    pos_x,pos_y=np.loadtxt(dir_results2+"5_Cor_in_"+str(rho)+".dat",unpack=True,usecols=[0,1])
    plt.scatter(pos_x,pos_y,c="#2d6a4f",marker=".")
    #<----------------------------Limite de las posiciones------------------------->
    lim=np.arange(-30,35,5)
    #<--------------------------------Reposicion de las particulas---------------------->
    lim_real=np.arange(0,65,5)
    #<----------------------------Renombramiento de los bordes--------------------------_>
    #plt.yticks(lim,lim_real);plt.xticks(lim,lim_real)
    plt.yticks([]);plt.xticks([])
    plt.savefig(dir_graphics+"Cor_in_"+str(rho)+".png")
    plt.clf()
fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9))=plt.subplots(3,3,figsize=(9,7))
axs=[ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]

x_lim=[0.9,4.9];y_lim=[0,5];delta=[0.6,1]
xtick=np.arange(x_lim[0],x_lim[1]+delta[0],delta[1]);ytick=np.arange(y_lim[0],y_lim[1]+delta[1],delta[1])
for rho,ax in zip(rho_values,axs):
    #<------------------------------------Grafica de la distribucion radial------------------------->
    r2,hist2=np.loadtxt(dir_results2+"4_hr_"+str(rho)+".dat",unpack=True)
    r3,hist3=np.loadtxt(dir_results3+"4_hr_"+str(rho)+".dat",unpack=True)
    ax.plot(r2,hist2,label="R$^{2}$",color="#6a040f")
    ax.set_title("$\\rho=$"+str(rho))
    ax.plot(r3,hist3,label="R$^{3}$",color="#0096c7")
    ax.set_xlim(x_lim[0],x_lim[1])
    ax.set_ylim(y_lim[0],y_lim[1])
    if ax in [ax1,ax4,ax7]:
        ax.set_yticks(ytick)
        ax.set_ylabel("$ \\rho (r)$")
    else:
        ax.set_yticks([])
    if ax in [ax7,ax8,ax9]:
        ax.set_xticks(xtick)
        #ax.set_xlabel("Distancia radial (r)")
    else:
        ax.set_xticks([])
    ax.legend(frameon=False,ncol=2,bbox_to_anchor=(0,1,1,0),mode="expand")
    for x,y in zip(xtick,ytick):
        ax.plot([x,x],[ytick[0],ytick[-1]],ls="--",color="black",alpha=0.5)
        ax.plot([xtick[0],xtick[-1]],[y,y],ls="--",color="black",alpha=0.5)
ax8.set_xlabel('Distancia radial(r)')
plt.savefig(dir_graphics+"Dis_rad.png",dpi=300)
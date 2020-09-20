import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results2="../Results_2/";dir_graphics="../Graphics/";dir_results3="../Results_3/"
#<----------Lista de las direcciones, titulos y terminaciones de las graricas------------->
dirs=[dir_results2,dir_results3];titles=["R$^{2}$","R$^{3}$"];names=["2","3"]
#<-_----------------------Grafica de la energía--------------------------------->
rho_values=np.round(np.arange(0.1,0.6,0.1),2)
#<-----------------------------Colores de las graficas--------------------->
colors=["#0466c8","#52b788"]
for dir,color,title,name in zip(dirs,colors,titles,names):
    #<-------------Divisiones de las graficas---------------------------->
    fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9))=plt.subplots(3,3,figsize=(9,7))
    axs=[ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]
    for rho,ax in zip(rho_values,axs):
        #<------------------Lectura de los datos------------------------->
        walks,e_kin,e_pot=np.loadtxt(dir+"8_T_U_P_"+str(rho)+".dat",unpack=True,usecols=[0,1,2])
        e_tol=e_pot*1e3+e_kin
        walks=walks*1e-4
        ax.plot(walks,e_tol,color=color)
        #<-----------------Añadir el titulo centrado---------------------->
        if ax==ax2:
            ax.set_title(title+"\n $\\rho=$"+str(rho))
        else:
            ax.set_title("$\\rho=$"+str(rho))
        #<-----------------------Añadir label del eje x a las ultimas tres------------------>
        if ax in [ax7,ax8,ax9]:
            ax.set_xticks(np.arange(0,20+5,5))
            ax.set_xlabel("Walks (10$^{4}$)")
        else:
            ax.set_xticks([])
        ax.set_yticks([])
    #<-----------------------------------Guardado de la gráfica------------------------->
    plt.savefig(dir_graphics+"Energy_"+name+".png",dpi=200)
    plt.clf()
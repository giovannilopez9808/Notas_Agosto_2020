import numpy as np
import matplotlib.pyplot as plt
#<---------------------Direccion de los archivos-------------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
#<---------------------------------Numero de particulas------------------------->
n_part=np.size(np.loadtxt(dir_results+"5_Cor_in.dat",usecols=0))
#<----------------------------------Pasos-------------------------------->
walks=np.loadtxt(dir_results+"8_T_U_P.dat",usecols=0)
#<---------------------------Numero de pasos---------------------------->
n_walks=np.arange(4)
#<----------------------------Limite de las posiciones------------------------->
lim=np.arange(-30,35,5)
#<--------------------------------Reposicion de las particulas---------------------->
lim_real=np.arange(0,65,5)
fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2, 2)
#<----------------------------Lista de axs------------------------->
axs=[ax1,ax2,ax3,ax4]
plt.subplots_adjust(left=0.057,right=0.964,bottom=0.064,top= 0.912)
print("Creando graficas")
for walk,walk_real,ax in zip(n_walks,walks,axs):
    #<--------------------------------Lectura de las posiciones------------------------------------->
    pos_x,pos_y=np.loadtxt(dir_results+"3_coor.dat",unpack=True,usecols=[0,1],skiprows=walk*(n_part+1)+1,max_rows=n_part)
    #<----------------------------Renombramiento de los bordes--------------------------_>
    ax.set_yticks([]);ax.set_xticks([])
    ax.set_title("Walk N="+str(int(walk_real)))
    ax.scatter(pos_x,pos_y,c="#2d6a4f",alpha=0.7,marker=".")
plt.savefig(dir_graphics+"Dim_Graphics.png")
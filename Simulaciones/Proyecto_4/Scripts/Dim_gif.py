import numpy as np
import matplotlib.pyplot as plt
import datetime
from os import listdir
import matplotlib.pyplot as plt
import math
import imageio
import os,sys
import time
#<------------------------Funcion para generar el gif---------------------------->
def create_gif(filenames, duration):
	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))
	output_file='../Graphics/dim.gif'
	imageio.mimsave(output_file, images, duration=duration)
#<---------------------Direccion de los archivos-------------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
#<---------------------------------Numero de particulas------------------------->
n_part=np.size(np.loadtxt(dir_results+"5_Cor_in_0.dat",usecols=0))
#<----------------------------------Pasos-------------------------------->
walks=np.loadtxt(dir_results+"8_T_U_P_0.dat",usecols=0)
#<---------------------------Numero de pasos---------------------------->
n_walks=np.size(walks)
# #<----------------------------Limite de las posiciones------------------------->
# lim=np.arange(-30,35,5)
# #<--------------------------------Reposicion de las particulas---------------------->
# lim_real=np.arange(0,65,5)
print("Creando graficas")
for walk,walk_real in zip(range(n_walks),walks):
    #<--------------------------------Lectura de las posiciones------------------------------------->
    pos_x,pos_y=np.loadtxt(dir_results+"3_coor_0.dat",unpack=True,usecols=[0,1],skiprows=walk*(n_part+1)+1,max_rows=n_part)
    #<------------------------------Limites de la caja--------------------------------->
    #plt.ylim(-30,30);plt.xlim(-30,30)
    #<----------------------------Renombramiento de los bordes--------------------------_>
    #plt.yticks(lim,lim_real);plt.xticks(lim,lim_real)
    plt.yticks([]);plt.xticks([])
    plt.title("Walk N="+str(int(walk_real)))
    plt.scatter(pos_x,pos_y,c="#2d6a4f",marker=".")
    plt.savefig(str(walk)+".png")
    plt.show()
    plt.clf()
print("Creando gif")
duration = 0.1
#<-------------------------Nombres de las graficas--------------------------------->
filenames = sorted(filter(os.path.isfile, [x for x in os.listdir() if x.endswith(".png")]), key=lambda p: os.path.exists(p) and os.stat(p).st_mtime or time.mktime(datetime.now().timetuple()))
#<---------------------------Creacion del gif-------------------------->
create_gif(filenames, duration)
#<----------------------------Eliminacion de las grafias residuales--------------->
os.system("rm *.png")
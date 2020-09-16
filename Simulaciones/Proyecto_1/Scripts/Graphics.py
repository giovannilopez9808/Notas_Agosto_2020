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
dir_results="../Results/";dir_graphics="../Graphics/"
#<------------------Grafica la posicion inicial---------------------------------->
pos_x,pos_y=np.loadtxt(dir_results+"5_Cor_in.dat",unpack=True,usecols=[0,1])
plt.scatter(pos_x,pos_y)
plt.savefig(dir_graphics+"Cor_in.png")
plt.clf()
#<-_----------------------Grafica de la energía--------------------------------->
walks,e_kin,e_pot=np.loadtxt(dir_results+"8_T_U_P.dat",unpack=True,usecols=[0,1,2])
#plt.plot(walks,e_kin)
#plt.plot(walks,e_pot)
#plt.show()
#<------------------------------------Grafica de la distribucion radial------------------------->
r,hist=np.loadtxt(dir_results+"4_hr.dat",unpack=True)
plt.plot(r,hist)
plt.xlim(0.75,5)
plt.xlabel("Distancia radial")
plt.savefig(dir_graphics+"Dis_rad.png")
plt.clf()
#<-------------------------------Gif de la dinamica------------------------------------------->
n_walks=np.size(walks)
n_part=np.size(pos_x)
lim=np.arange(-30,35,5)
lim_real=np.arange(0,65,5)
for walk,walk_real in zip(range(n_walks),walks):
    pos_x,pos_y=np.loadtxt(dir_results+"3_coor.dat",unpack=True,usecols=[0,1],skiprows=walk*(n_part+1)+1,max_rows=n_part)
    plt.ylim(-30,30)
    plt.xlim(-30,30)
    plt.yticks(lim,lim_real)
    plt.xticks(lim,lim_real)
    plt.title("Walk N="+str(int(walk_real)))
    plt.scatter(pos_x,pos_y,c="#2d6a4f")
    plt.savefig(str(walk)+".png")
    plt.clf()
print("Creando gif")
duration = 0.1
filenames = sorted(filter(os.path.isfile, [x for x in os.listdir() if x.endswith(".png")]), key=lambda p: os.path.exists(p) and os.stat(p).st_mtime or time.mktime(datetime.now().timetuple()))
create_gif(filenames, duration)
os.system("rm *.png")
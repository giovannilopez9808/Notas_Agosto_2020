import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
#<------------------Grafica la posicion inicial---------------------------------->
pos_x,pos_y=np.loadtxt(dir_results+"5_Cor_in.dat",unpack=True,usecols=[0,1])
plt.scatter(pos_x,pos_y,c="#2d6a4f",marker=".")
#<----------------------------Limite de las posiciones------------------------->
lim=np.arange(-30,35,5)
#<--------------------------------Reposicion de las particulas---------------------->
lim_real=np.arange(0,65,5)
#<----------------------------Renombramiento de los bordes--------------------------_>
#plt.yticks(lim,lim_real);plt.xticks(lim,lim_real)
plt.yticks([]);plt.xticks([])
plt.savefig(dir_graphics+"Cor_in.png")
plt.clf()
#<------------------------------------Grafica de la distribucion radial------------------------->
r,hist=np.loadtxt(dir_results+"4_hr.dat",unpack=True)
plt.plot(r,hist,lw=3,color="#52b788")
plt.xlim(0.9,4)
plt.ylim(0,2.5)
plt.xticks(np.arange(0.9,4+0.3,0.3))
plt.yticks(np.arange(0,2.5+0.25,0.25))
plt.ylabel("$ \\rho (r)$")
plt.xlabel("Distancia radial (r)")
plt.savefig(dir_graphics+"Dis_rad.png")
plt.clf()
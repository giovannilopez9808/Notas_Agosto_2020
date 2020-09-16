import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
#<------------------Grafica la posicion inicial---------------------------------->
pos_x,pos_y=np.loadtxt(dir_results+"5_Cor_in.dat",unpack=True,usecols=[0,1])
plt.scatter(pos_x,pos_y)
plt.savefig(dir_graphics+"Cor_in.png")
plt.clf()
#<------------------------------------Grafica de la distribucion radial------------------------->
r,hist=np.loadtxt(dir_results+"4_hr.dat",unpack=True)
plt.plot(r,hist)
plt.xlim(0.75,5)
plt.ylabel("$ \\rho (r)$")
plt.xlabel("Distancia radial (r)")
plt.savefig(dir_graphics+"Dis_rad.png")
plt.clf()
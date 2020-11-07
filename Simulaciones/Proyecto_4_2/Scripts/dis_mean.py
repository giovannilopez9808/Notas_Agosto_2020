import numpy as np
import matplotlib.pyplot as plt
#<---------------------Direccion de los archivos-------------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
n=9;n_particle=np.arange(100,1000,100)
dis_mean=[]
for i in range(9):
    dis_i=np.sqrt(np.loadtxt(dir_results+"dis_if"+str(i+1)+".dat",usecols=1))
    mean=np.mean(dis_i)
    dis_mean=np.append(dis_mean,mean)
plt.plot(n_particle,dis_mean,color="#00a896",lw=3)
plt.scatter(n_particle,dis_mean,color="#05668d")
plt.xlabel("Número de partículas")
plt.ylabel("Distancia inicio-fin")
plt.xlim(100,900)
plt.xticks(n_particle)
plt.yticks(np.arange(0,450+50,50))
plt.ylim(0,450)
plt.grid(ls="--",color="grey",lw=2,alpha=0.3)
plt.savefig(dir_graphics+"dis.png",dpi=200)
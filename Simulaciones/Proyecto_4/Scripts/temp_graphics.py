import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import matplotlib.pyplot as plt
#<---------------------Direccion de los archivos-------------------------->
dir_results="../Results/";dir_graphics="../Graphics/"
n_part=50
n=1
for i in range(n):
    #<----------------------------------Pasos-------------------------------->
    walks,ekin_list=np.loadtxt(dir_results+"8_T_U_P_"+str(i)+".dat",usecols=[0,1],unpack=True)
    file=open(dir_results+"temp_"+str(i)+".dat","w")
    for walk,ekin in zip(walks,ekin_list):
        temp=ekin/(3*n_part)
        file.write(str(walk)+" "+str(temp)+"\n")
    file.close()
    temp=np.loadtxt(dir_results+"temp_"+str(i)+".dat",usecols=1)
    plt.plot(walks,temp)
    plt.show()
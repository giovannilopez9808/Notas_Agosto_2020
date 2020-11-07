import numpy as np
import os
#n=9;n_particle=np.arange(100,1000,100)
n=9;n_particle=np.arange(100,1000,100)
os.system("gfortran MD-n2.f -o MD-n2.out")
for i,i_part in zip(range(n),n_particle):
    file=open("../Input/rho.txt","w")
    file.write(str(i)+" "+str(int(i_part))+"\n")
    file.close()
    print("Corriendo simulación número "+str(i)+" con numero de particulas "+str(i_part))
    os.system("./MD-n2.out")
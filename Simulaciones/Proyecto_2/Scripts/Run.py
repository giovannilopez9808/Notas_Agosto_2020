import numpy as np
import os
rho_values=np.round(np.array([0.3,0.6,0.8]),2)
temp_values=np.round(np.arange(0.1,1.7,0.2),2)
os.system("gfortran MD-n2.f -o MD-n2.out")
for t in temp_values:
    for rho in rho_values:
        file=open("../Input/rho.txt","w")
        file.write(str(rho)+" "+str(t)+" _"+str(rho)+"_"+str(t))
        file.close()
        print("Corriendo para rho="+str(rho)+" y T="+str(t))
        os.system("./MD-n2.out")

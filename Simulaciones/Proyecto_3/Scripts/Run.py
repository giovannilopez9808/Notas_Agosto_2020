import numpy as np
import os
rho_values=np.round(np.array([0.3]),2)
os.system("gfortran MD-n2.f -o MD-n2.out")
for rho in rho_values:
    file=open("../Input/rho.txt","w")
    file.write(str(rho)+" _"+str(rho))
    file.close()
    print("Corriendo para rho=",str(rho))
    os.system("./MD-n2.out")

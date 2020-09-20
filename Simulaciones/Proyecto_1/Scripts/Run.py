import numpy as np
import os
rho_values=np.round(np.arange(0.1,1,0.1),2)
os.system("gfortran MD-n3.f -o MD-n3.out")
os.system("gfortran MD-n2.f -o MD-n2.out")
for rho in rho_values:
    file=open("../Input/rho.txt","w")
    file.write(str(rho)+" _"+str(rho))
    file.close()
    print("Corriendo para rho="+str(rho))
    print("Calculando para R2")
    os.system("./MD-n3.out")
    print("Calculando para R3")
    os.system("./MD-n2.out")

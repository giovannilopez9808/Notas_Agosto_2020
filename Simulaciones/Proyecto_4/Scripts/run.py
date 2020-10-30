import numpy as np
import os
n=9
os.system("gfortran MD-n2.f -o MD-n2.out")
for i in range(n):
    file=open("../Input/rho.txt","w")
    file.write(str(i))
    file.close()
    print("Corriendo simulación número "+str(i))
    os.system("./MD-n2.out")

import numpy as np
import os
n=10
os.system("gfortran MD-n2.f -o MD-n2.out")
for i in range(n):
    file=open("../Input/rho.txt","w")
    file.write(str(int(i)))
    file.close()
    print("Corriendo para rho=",str(rho))
    os.system("./MD-n2.out")

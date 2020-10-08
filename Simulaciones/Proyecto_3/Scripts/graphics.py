import numpy as np
import matplotlib.pyplot as plt
#<----------------------------Direcciones de los archivos-------------------->
dir_results2="../Results/";dir_graphics="../Graphics/"
rho=0.3
r2,hist2=np.loadtxt(dir_results2+"4_hr_"+str(rho)+"    .dat",unpack=True)
plt.plot(r2,hist2)
plt.show()
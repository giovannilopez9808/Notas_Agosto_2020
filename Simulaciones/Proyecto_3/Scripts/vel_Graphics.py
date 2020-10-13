import numpy as np
import matplotlib.pyplot as plt
n_pasos=20
n_part=784
x,y=[],[]
for i in range(20):
    data_x,data_y=np.loadtxt("../Results/2_velo_0.4.dat",unpack=True,skiprows=i*(n_part+1)+1,max_rows=n_part)
    x=np.append(x,data_x)
    x=np.append(x,data_y)
plt.hist(x,bins=200)
plt.show()
rho=0.3
r2,hist2=np.loadtxt("../Results/4_hr_"+str(rho)+".dat",unpack=True)
plt.plot(r2,hist2)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
n_pasos=20
n_part=784
x,y=[],[]
for i in range(20):
    data_x,data_y=np.loadtxt("../Results/2_velo_0.3    .dat",unpack=True,skiprows=i*(n_part+1)+1,max_rows=n_part)
    x=np.append(x,data_x)
    y=np.append(y,data_y)
plt.hist(x,bins=100)
plt.show()
plt.hist(y)
plt.show()
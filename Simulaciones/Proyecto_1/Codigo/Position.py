import numpy as np
import matplotlib.pyplot as plt
pos_x,pos_y=np.loadtxt("Results/5_Cor_in.dat",unpack=True,usecols=[0,1])
print(np.size(pos_x))
plt.scatter(pos_x,pos_y)
plt.show()
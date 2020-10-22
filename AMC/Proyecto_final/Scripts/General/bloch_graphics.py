from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
import os
vectors=[[0,0,1],[0,0,-1],[1,0,0],[-1,0,0]]
i=0
for vector in vectors:
    plot_bloch_vector(vector)
    plt.savefig(str(i)+".png")
    i+=1
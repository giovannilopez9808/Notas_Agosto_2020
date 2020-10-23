import numpy as np
import matplotlib.pyplot as plt
clasic=np.loadtxt("time_clasic.txt")
clasic=clasic*1e3
quantum=np.loadtxt("time_shor.txt")
quantum=quantum/4
quantum_ibm=quantum/1.5
x=np.arange(np.size(clasic))
plt.xlim(0,1000)
plt.scatter(x,clasic,marker=".",color="#03071e",label="Clásico")
plt.scatter(x,quantum,marker=".",color="#9d0208",label="Shor Local")
plt.scatter(x,quantum_ibm,marker=".",color="#f48c06",label="Shor IBM")
plt.legend(frameon=False,ncol=3,mode="expand",bbox_to_anchor=(0, 1.06,1,0.02),markerscale=2, scatterpoints=1,)
plt.ylim(0,0.12)
plt.yticks(np.arange(0,0.12+0.01,0.01))
plt.xticks(np.arange(0,1000+100,100))
plt.xlabel("Número de repeticiones")
plt.ylabel("Tiempo (ms)")
plt.subplots_adjust(left=0.121,bottom=0.112,right=0.943,top=0.898)
plt.savefig("time.png",dpi=200
import numpy as np
a=1/np.sqrt(2)
H=[[a,a],[a,-a]]
eval,evec=np.linalg.eig(H)
print(eval,evec)
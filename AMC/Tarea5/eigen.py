import numpy as np
a=1/np.sqrt(2)
H=[[a,a],[a,-a]]
eval,evec=np.linalg.eig(H)
evec=np.transpose(evec/evec[1,1])
print("Los eigenvalores son \n",eval)
print("Las eigenvectores son \n",evec)
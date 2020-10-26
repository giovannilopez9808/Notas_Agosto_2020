import numpy as np
import matplotlib.pyplot as plt
def pot(L,mu,M,G,r):
    v=L**2/(2*mu*r**2)-(G*M*mu/r)
    return v
def zero(L,G,M,mu):
    rc=L**2/(2*G*M*mu**2)
    return rc
def minimo(rc):
    return 2*rc
L=1;mu=1;M=1;G=1
x=np.arange(0.4,5+0.01,0.01)
y=pot(L,mu,M,G,r=x)
rc=zero(L,G,M,mu);pot_rc=pot(L,mu,M,G,rc)
mi=minimo(rc);pot_min=pot(L,mu,M,G,mi)
plt.plot(x,y,label="$V_{er}(r)$",lw=3,color="#f72585")
plt.plot([0,np.max(x)],[0,0],ls="--",color="#ff5400")
plt.plot([rc,rc],[-0.6,pot_rc],ls="--",label="r$_{c}$",lw=3,color="#4361ee")
plt.plot([mi,mi],[-0.6,pot_min],ls="--",label="r$_{min}$",lw=3,color="#90a955")
plt.xticks([rc,mi],["$r_{c}$","$r_{min}$"],fontsize=12);plt.yticks([0])
plt.ylim(-0.6,0.6);plt.xlim(0,5)
plt.xlabel("Coordenada radial",fontsize=12)
plt.ylabel("Potencial efectivo $V_{rf}(r)$",fontsize=12)
plt.legend(frameon=False,fontsize=14)
plt.subplots_adjust(left=0.088,bottom=0.11,right=0.962,top=0.962)
plt.savefig("../images/Pot_efe.png",dpi=200)
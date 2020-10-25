import numpy as np
import matplotlib.pyplot as plt
#<-----------------------------Potencial--------------------->
def potential_lj(r,e,sigma):
    v=4*e*((sigma/r)**12-(sigma/r)**6)
    return v
#<----------------------------Fuerza--------------------->
def force_lj(r,e,sigma):
    f=4*e*(12*sigma**12/r**13-6*sigma**6/r**7)
    return f
#
def potencial_atrac(r,e,ra):
    k=e
    v=4*e*(ra/r)**2*log(1-(ra/r)**2)
    return v
#
def force_atrac():

#<----------------------------Direcciones de los archivos-------------------->
dir_graphics="../Graphics/"
#<------------------------Parametros-------------------->
sigma=1;e=1
#<------------------------------Valores para el radio---------------------->
r=np.arange(sigma*0.5,2.5+0.01,0.01)
#<----------------------------Potencial-------------------->
v=potential(r,e,sigma)
#<--------------------------------Fuerza------------------->
f=force(r,e,sigma)
#<----------------------------Limites y posiciones caracteristicas------------>
v_min=np.min(v)
r_min=r[np.where(v_min==v)]
y_min,y_max=np.round(np.min(v))-0.5,np.round(np.max(v))+0.5
#<---------------------------------Sigma-------------------------------------->
plt.plot([r[0],sigma],[0,0],ls="--",color="#06d6a0",lw=3,label="$\sigma=1$")
#<-------------------------------Epsilon---------------------------------------->
plt.plot([r_min,r_min],[v_min,0],ls="--",color="#5390d9",lw=3,label="$\epsilon=1$")
#<-------------------------Grafica del potencial--------------------------->
plt.plot(r,v,lw=3,color="#6930c3",label="$V(r)$")
#<-------------------------Grafica de la fuerza--------------------------->
plt.plot(r,f,lw=3,color="#9d0208",label="$F(r)$",alpha=0.5)
#<-----------------------------------Eje x----------------------------------------->
plt.plot([r[0],r[-1]],[0,0],ls="--",color="black",lw=1,alpha=0.5)
#<-----------------------------------Limites de la grafica---------------------------------_>
plt.xlim(r[0],r[-1]);plt.ylim(-2.5,2.5)
#<---------------------------------Leyendas de los ejes-------------------->
plt.ylabel("V(r)");plt.xlabel("Distancia radial (r)")
plt.legend(frameon=False,ncol=2,loc="upper right",fontsize=12)
plt.yticks(np.arange(-2.5,2.5+0.5,0.5))
plt.savefig(dir_graphics+"Potencial.png",dpi=200)
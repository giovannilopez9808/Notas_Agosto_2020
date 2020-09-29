import numpy as np
import matplotlib.pyplot as plt
#<----------------------Funcion que calcula la distancia--------->
def distancia(x,y):
    return np.sqrt(x**2+y**2)
#<--------Funcion que calcula la pendiente----------------->
def m(x,y):
    if x!=0:
        m=y/x
    else:
        m=abs(y)
    return m
#<-------------------------------Formato------------------------------->
def format(value):
    if value>=0:
        value=str(round(value))
    else:
        value="$\\bar{"+str(round(abs(value)))+"}$"
    return value
#<-----------------Localización de carpetas------------------------->
dir_data="Data/";dir_graphics="Graphics/"
#<-------------------------Lectura de las posiciones---------------------->
pos_x,pos_y=np.loadtxt(dir_data+"pos.csv",delimiter=",",unpack=True,skiprows=1)
n_data=np.size(pos_x)
#<--------------------------Proporcion------------------------------->
#<----------Cuadriculas de una hoja con la presentacion a pantala completa------------->
prop=6.8/8.47
#<--------------------------------------Ploteo de los datos iniciales------------------>
plt.scatter(pos_x,pos_y,color="#065a60",marker=".")
#<-------------------------Origen--------------------------->
plt.scatter(0,0,c="#065a60",marker=".")
#<-----------------------------Eliminacion de ejes--------------------->
plt.xticks([]);plt.yticks([]);plt.axis("off")
plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
#<----------------------Barra de proporción--------------------->
plt.plot([5,5+prop*8.47],[-11,-11],color="black",lw="3")
plt.text(prop*8.47/2+5,-10.5,"8.47 nm$^{-1}$")
plt.savefig(dir_graphics+"inicial.png",dpi=200);plt.clf()
coor_x,coor_y,dis_list=[],[],[]
#<--------------------Guardado y eleccion de las distancias------------------>
for i in range(n_data-1):
    dis_i=distancia(pos_x[i],pos_y[i])
    m_i=m(pos_x[i],pos_y[i])
    for j in range(i+1,n_data):
        dis_j=distancia(pos_x[j],pos_y[j])
        m_j=m(pos_x[j],pos_y[j])
#<----Si las pendientes son iguales y distancias iguales entonces son puntos simetricos al origen-------->
        if m_i==m_j and dis_i==dis_j:
            for k in [i,j]:
#<---------------------Guardado-------------------------------->
                coor_x=np.append(coor_x,pos_x[k])
                coor_y=np.append(coor_y,pos_y[k])
                dis_list=np.append(dis_list,round(prop*10/dis_i,4))
#<-----------------------Ploteo de las lineas------------------------------>
            plt.scatter(pos_x,pos_y,c="#065a60",marker=".")
            plt.plot(pos_x[[i,j]],pos_y[[i,j]],color="#312244",ls="--",alpha=0.7)
#<-------------------------Origen--------------------------->
plt.scatter(0,0,c="#065a60",marker=".")
#<-----------------------------Eliminacion de ejes--------------------->
plt.xticks([]);plt.yticks([]);plt.axis("off")
plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
#<----------------------Barra de proporción--------------------->
plt.plot([5,5+prop*8.47],[-11,-11],color="black",lw="3")
plt.text(prop*8.47/2+5,-10.5,"8.47 nm$^{-1}$")
plt.savefig(dir_graphics+"distancia.png",dpi=200);plt.clf()
#<----------------------Lectura de las propiedades del material--------------------------->
spacing_list,h_list,k_list,l_list=np.loadtxt(dir_data+"data.csv",delimiter=",",usecols=[2,3,4,5],skiprows=1,unpack=True)
latitce_list_h,latitce_list_k,latitce_list_l=[],[],[]
#<-----------------------------Asignacion de los indices de miller------------------------->
for x,y,dis in zip(coor_x,coor_y,dis_list):
    r=100
    for spacing,h,k,l in zip(spacing_list,h_list,k_list,l_list):
        r_new=abs(dis-spacing)
#<--------Al existir error en las mediciones, se opto por asignar al que se acerque mas---------------->
        if r_new<r:
            h_new=h;k_new=k;l_new=l
            r=r_new
#<----------------------Guardad-------------------------------->
    latitce_list_h=np.append(latitce_list_h,h_new)
    latitce_list_k=np.append(latitce_list_k,k_new)
    latitce_list_l=np.append(latitce_list_l,l_new)
#<-----------------------Eliminacion de valores para asegurar que no se asigne de forma erronea------------->
    del h_new,k_new,l_new
#<-----------------------------Ploteo de los indices de miller arriba de cada punto------------------------->
for x,y,h,k,l,dis_list in zip(coor_x,coor_y,latitce_list_h,latitce_list_k,latitce_list_l,dis_list):
    a="("+str(int(h))+str(int(k))+str(int(l))+")"
    plt.text(x-0.5,y+0.5,a)
#<-----------------------------Eliminacion de ejes--------------------->
plt.xticks([]);plt.yticks([]);plt.axis("off")
#<-------------------------Origen------------------------>
plt.scatter(0,0,c="#065a60",marker=".")
#<------------------------Puntos------------------------->
plt.scatter(coor_x,coor_y,color="#065a60",marker=".")
#<-----------------------Leyenda de proporción-------------------->
plt.plot([5,5+prop*8.47],[-11,-11],color="black",lw="3")
plt.text(prop*8.47/2+5,-10.5,"8.47 nm$^{-1}$")
plt.subplots_adjust(left=0, bottom=0, right=1, top=0.97)
plt.savefig(dir_graphics+"indices.png",dpi=200)
plt.clf()
h_list,k_list,l_list=np.loadtxt(dir_data+"lattice.csv",delimiter=",",unpack=True,skiprows=1)
for x,y,h,k,l in zip(pos_x,pos_y,h_list,k_list,l_list):
    h_str=format(h);k_str=format(k);l_str=format(l)
    string="["+h_str+k_str+l_str+"]"
    plt.text(x-0.5,y+0.5,string)
#<-----------------------------Eliminacion de ejes--------------------->
plt.xticks([]);plt.yticks([]);plt.axis("off")
#<-------------------------Origen------------------------>
plt.scatter(0,0,c="#065a60",marker=".")
#<------------------------Puntos------------------------->
plt.scatter(coor_x,coor_y,color="#065a60",marker=".")
#<-----------------------Leyenda de proporción-------------------->
plt.plot([5,5+prop*8.47],[-11,-11],color="black",lw="3")
plt.text(prop*8.47/2+5,-10.5,"8.47 nm$^{-1}$")
plt.subplots_adjust(left=0, bottom=0, right=1, top=0.97)
#plt.savefig(dir_graphics+"indices.png",dpi=200)
plt.show()
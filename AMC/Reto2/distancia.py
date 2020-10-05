import numpy as np
import matplotlib.pyplot as plt
import os
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

def plot_image(image,path,name,cmap=None,bar=True):
    plt.axis("off")
    plt.imshow(image,cmap=cmap)
    if bar:
        plot_bar()
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.188)
    plt.savefig(path+name,dpi=200)
    plt.clf()
#<--------------------Funcion que grafica los puntos--------------------->
def plot_points(prop,path,name):
    #<-------------------------Origen--------------------------->
    plt.scatter(0,0,c="#065a60",marker=".")
    #<-----------------------------Eliminacion de ejes--------------------->
    plt.xticks([]);plt.yticks([]);plt.axis("off")
    plt.subplots_adjust(left=0, bottom=0, right=1, top=0.97)
    #<----------------------Barra de proporción--------------------->
    plt.plot([6.5,63.3],[-80,-80],color="black",lw="3")
    plt.text(17+5,-75,"5  1 nm$^{-1}$",fontsize=16)
    plt.savefig(path+name,dpi=200)
    plt.clf()
#<---------------------Funcion que grafica los indices de Miller-------------->
def plot_indices(pos_x,pos_y,h_list,k_list,l_list,color):
    for x,y,h,k,l in zip(pos_x,pos_y,h_list,k_list,l_list):
        h_str=format(h);k_str=format(k);l_str=format(l)
        string="("+h_str+k_str+l_str+")"
        plt.text(x-5,y+3,string,color=color)

def plot_hexa(hexa_x,hexa_y,color):
    n=np.size(hexa_x)
    for i in range(n):
        j=i+1
        if j==n: j=0
        pos=[i,j]
        plt.plot(hexa_x[pos],hexa_y[pos],lw=3,color=color)

def plot_bar():
    plt.plot([6.5,63.3],[247.4,247.4],color="black",lw=4)
    plt.text(2,238,"5  1nm$^{-1}$",fontsize=26)
#<-----------------Localización de carpetas------------------------->
dir_data="Data/";dir_graphics="Graphics/"
#<-------------------------Lectura de las posiciones---------------------->
pos_x,pos_y=np.loadtxt(dir_data+"pos.csv",delimiter=",",unpack=True,skiprows=1)
pos_x=pos_x-129
pos_y=pos_y-128.8
n_data=np.size(pos_x)
#<--------------------------Proporcion------------------------------->
#<----------Cuadriculas de una hoja con la presentacion a pantala completa------------->
prop=1/((63.3-6.5)*5)
#<--------------------------------------Ploteo de los datos iniciales------------------>
plt.scatter(pos_x,pos_y,color="#065a60",marker=".")
plot_points(prop,dir_graphics,"inicial.png")
coor_x,coor_y,dis_list=[],[],[]
#<--------------------Guardado y eleccion de las distancias------------------>
for i in range(n_data-1):
    dis_i=distancia(pos_x[i],pos_y[i])
    m_i=m(pos_x[i],pos_y[i])
    for j in range(i+1,n_data):
        dis_j=distancia(pos_x[j],pos_y[j])
        m_j=m(pos_x[j],pos_y[j])
#<----Si las pendientes son iguales y distancias iguales entonces son puntos simetricos al origen-------->
        if abs(m_i-m_j)<1.7 and abs(dis_i-dis_j)<8.75 and m_i/abs(m_i)==m_j/abs(m_j):
            for k in [i,j]:
#<---------------------Guardado-------------------------------->
                coor_x=np.append(coor_x,pos_x[k])
                coor_y=np.append(coor_y,pos_y[k])
                dis_list=np.append(dis_list,round(prop*10*dis_i,4))
#<-----------------------Ploteo de las lineas------------------------------>
            plt.plot(pos_x[[i,j]],pos_y[[i,j]],color="#312244",ls="--",alpha=0.7)
plt.scatter(pos_x,pos_y,c="#065a60",marker=".")
plot_points(prop,dir_graphics,"distancia")
#<----------------------Lectura de las propiedades del material--------------------------->
spacing_list,h_list,k_list,l_list=np.loadtxt(dir_data+"data.txt",usecols=[2,3,4,5],skiprows=16,unpack=True,max_rows=4)
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
for x,y,h,k,l in zip(coor_x,coor_y,latitce_list_h,latitce_list_k,latitce_list_l):
    a="["+str(int(h))+str(int(k))+str(int(l))+"]"
    plt.text(x-5,y+3,a)
plt.scatter(coor_x,coor_y,color="#065a60",marker=".")
plot_points(prop,dir_graphics,"indices.png")
#<------------------------------Ploteo de los indices de MIller a partir de un archivo----------------------->
h_list,k_list,l_list=np.loadtxt(dir_data+"lattice.csv",delimiter=",",unpack=True,skiprows=1)
plot_indices(pos_x,pos_y,h_list,k_list,l_list,'black')
plt.scatter(coor_x,coor_y,color="#065a60",marker=".")
plot_points(prop,dir_graphics,"lattice.png")
#<----------------------------Ploteo de las caras del cristal------------------------------>
from PIL import Image, ImageFilter
im=Image.open("Images/Imagen.tif")
f=np.fft.fft2(im)
f=np.fft.fftshift(f)
f=np.log(np.abs(f))
pos_x=pos_x+129
pos_y=pos_y+128.8
plt.imshow(f)
plot_indices(pos_x,pos_y,h_list,k_list,l_list,'black')
#<-----------------------------Eliminacion de ejes--------------------->
plt.xticks([]);plt.yticks([]);plt.axis("off")
plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
#<----------------------Barra de proporción--------------------->
plot_bar()
plt.savefig(dir_graphics+"caras.png")
plt.clf()
#<---------------Grafica del hexagono con los indices de miller------------------>
hexa_x,hexa_y=np.loadtxt("Data/hexa.csv",delimiter=",",unpack=True)
plot_hexa(hexa_x,hexa_y,'black')
plot_indices(pos_x,pos_y,h_list,k_list,l_list,'black')
plot_image(1000*f,dir_graphics,"hexa.png")
#<------------Grafica de la nanoparticula con los indices de Miller---------->
plot_indices(pos_x,pos_y,h_list,k_list,l_list,'white')
plot_hexa(hexa_x,hexa_y,'white')
plot_image(im,dir_graphics,'nano_ind.png',bar=False)
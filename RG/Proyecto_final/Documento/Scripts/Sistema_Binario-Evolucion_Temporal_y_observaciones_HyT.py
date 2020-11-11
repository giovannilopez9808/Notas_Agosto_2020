import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#<---------------definicion de la funcion da/de-------------->
def dotx(x,t):
    a = x[0]
    e = x[1]
    return [-(16/(5*a**3))*(1+(73/24)*e**2+(37/96)*e**4)/((1-e**2)**(7/2)),
            -(76/(15*a**4))*e*(1+(121/304)*e**2)/((1-e**2)**(5/2))]
#<-----------------definicion del periodo orbital y el semieje mayor------------------->
def a(T_s):
    return (m_sol*M*(c*T_s/(2*np.pi))**2)**(1/3)
#<..................definicion del periodo orbital y el semieje mayor----------------->
def T(a_m):
    return (2*np.pi/c)*(a_m**3/(M*m_sol))**(1/2)
#<---------------definicion de la funcion que realiza la solucion de la ecuacion diferecnial-------------->
def solucion(x0,tt_int):
    #<------------Solucion de la ecuacion diferencial---------------------->
    sol = odeint(dotx,x0,tt_int)
    at_todos = sol[:,0]
    # verifica si at llega a 2. En caso positivo corta el arreglo de soluciones
    restriccion = np.where(at_todos<2)[0]
    if len(restriccion)!=0:
        #<------------------Deternima el tiempo donde at=2------------->
        pos_ttmax = restriccion[0]
        print('Acortando intervalo a tt_max = '+str(tt_int[pos_ttmax]))
    else: 
        pos_ttmax = len(tt_int)
    tt = tt_int[:pos_ttmax]
    #<------------tiempo en años--------------->
    t_a = tt*R_ast/c/31557600
    at = sol[:pos_ttmax,0]
    e = sol[:pos_ttmax,1]
    #<-------------soluciion de a en metros------------------>
    a_m = at*R_ast
    #<--------------solucion de T en segundos-------------------->
    T_s = T(a_m)
    return tt,t_a,at,e,a_m,T_s
#<-----------Definicion de la funcion g(e)------------------>
def g(e):
    return e**(12/19)*(1+121*e**2/304)**(870/2299)/(1-e**2)
dir_graphics="../images/"
#<--------------Periodo inicial en dias---------------->
T0_d = 0.322997448911
#<-----------------Excentricidad inicial------------------->
e0 = 0.6171334
#<--------Masa del cuerpo orbitante en masas solares---------->
M_c = 1.3886
#<--------------------------Masa del pulsar en masas solares------------->
M_p = 1.4398
#---------------------Raṕidez de la luz en m/s---------------------->
c = 299792458
#<------------------- MG/C^3------------------------>
MGcm3 = 4.925490947E-6
#<-----Para metro de la masa del sol en metros m=GM/c^2---------------------->
m_sol = MGcm3*c
#<-------------Masa total en masas solares------------------------>
M = M_c+M_p
#<-----------------Masa reducida en masas solares------------------>
mu = (M_c*M_p)/M
#<--------------R* en metros------------------------->
R_ast = m_sol*(4*mu*M**2)**(1/3)
#<-------------Periodo inicial en segundos------------------>
T0_s = T0_d*86400
#<----------------Semieje mayor a en metros----------------->
a0_m = a(T0_s)
#<-------a adimensional inicial----------------------------->
at0 = a0_m/R_ast
#<----------Tiempo adimensional------------------->
tt_int_max = 10**22
#<-------------Tiempos de calculo-------------------------->
tt_int = np.linspace(0,tt_int_max,100000)
#<--------------Tiempo de integracion en años-------------------->
t_max_a = 30
#<------------------------Valores iniciales---------------------->
x0 = [at0,e0]
#<---------------------Calculo de la solucion---------------------->
tt,t_a,at,e,a_m,T_s = solucion(x0,tt_int) 
#<--------------------Valores rescalados---------------------->
a_m=a_m*1e-9
t_a=t_a*1e-8
#<---------Ploteo del semieje mayor con la excentricidad en el tiempo----------->
plt.plot(t_a,a_m,color="#006466",lw=3,label="semieje mayor")
plt.plot(t_a,e,color="#52b788",lw=3,label="excentricidad")
plt.xticks(np.arange(0,3+0.25,0.25));plt.yticks(np.arange(0,2+0.2,0.2))
plt.xlim(0,3);plt.ylim(0,2)
#<-------------Ploteo de los label--------------->
plt.xlabel('tiempo ($10^8$)');plt.ylabel('Distancia ($10^9$m) / excentricidad')
plt.grid(ls="--",color="grey")
plt.legend(frameon=False,ncol=2,bbox_to_anchor=(0, 1,1,0.02),mode="expand")
plt.subplots_adjust(left=0.124,bottom=0.14,right=0.964,top=0.894)
plt.savefig(dir_graphics+"a_adim.png",dpi=200)
plt.clf()
#<--------------Ploteo de la evolucion del periodo--------------->
T_h = T_s/3600
plt.plot(t_a,T_h,lw=3,color="#006466")
plt.xlim(0,3);plt.ylim(0,8)
plt.xticks(np.arange(0,3+0.25,0.25))
plt.yticks(np.arange(0,8+0.5,0.5))
plt.xlabel('tiempo $(años 10^{8})$');plt.ylabel('Periodo (horas)')
plt.grid(ls="--",color="grey")
plt.subplots_adjust(left=0.098,bottom=0.11,right=0.957,top=0.948)
plt.savefig(dir_graphics+"periodo.png",dpi=200)
plt.clf()
#<------------------Ploteo de la relacion entre g y e----------------->
ee=np.linspace(0,1,100)
plt.plot(ee,g(ee),color="#16db93",lw=3)
plt.yscale('log');plt.xticks(np.arange(0,1+0.1,0.1));plt.xlim(0,1)
plt.ylim(0,100)
plt.xlabel('excentricidad $(e)$',fontsize=14);plt.ylabel('función $g(e)$',fontsize=14)
plt.grid(ls="--",color="grey")
plt.savefig(dir_graphics+"gvse.png",dpi=200)
plt.clf()
#<-----------Ploteo de la solucion analitica y la numerica------------>
plt.plot(e,at*R_ast*1e-9,color="#0582ca",label='sol. numérica')
ee = np.linspace(min(e),e0,10)
a_an = a0_m*g(ee)*1e-9/g(e0)
plt.plot(ee,a_an,'o',color="#051923",label='sol. analítica')
plt.xticks(np.arange(0,0.65+0.05,0.05));plt.yticks(np.arange(0,2+0.2,0.2))
plt.xlim(0,0.65);plt.ylim(0,2)
plt.xlabel('excentricidad $(e)$');plt.ylabel('semieje mayor $(10^{9})$')
plt.legend(frameon=False,ncol=2,bbox_to_anchor=(0, 1,1,0.02),mode="expand",fontsize=13)
plt.grid(ls="--",color="grey")
plt.subplots_adjust(left=0.09,bottom=0.117,right=0.971,top=0.883)
plt.savefig(dir_graphics+"solana_solnum.png",dpi=200)
plt.clf()
#<-----------------------Solucion para datos observacionales---------------------->
#<--------------Tiempo adimensional maximo de integracion-------------------->
tt_int_max = 31557600*c*t_max_a/R_ast
tt_int = np.linspace(0,tt_int_max,100000)
tt,t_a,at,e,a_m,T_s = solucion(x0,tt_int)
dota = dotx(x0,0)[0]
dotT = (3/2)*(c/R_ast)*(T0_s/at0)*dota
data = np.loadtxt("data-HW.csv",delimiter=",")
t_exp = data[:,0]-data[0,0]
Delta_t_exp = data[:,1]
n = np.arange(40000)
t_n = (n*T0_s+dotT*T0_s*n*(n-1)/2.)/31557600. # tiempo, en años
Delta_t_n = dotT*T0_s*n*(n-1)/2 #retraso acumulado, en segundos
plt.plot(t_n,Delta_t_n,color="#3fc1c0",label='Relatividad general',lw=3)
plt.hlines(0,0,40, color='#4f772d',label='Newtoniano',lw=3)
plt.xlabel('tiempo (años)');plt.ylabel('Retraso acumulado (s)')
plt.xlim(0,33);plt.ylim(-45,5)
plt.xticks(np.arange(0,33+3,3));plt.yticks(np.arange(-45,5+5,5))
plt.plot(t_exp,Delta_t_exp,'o',color="#1d4e89",label='Datos observacionales')
plt.legend(loc=3,frameon=False,ncol=3,bbox_to_anchor=(0, 1,1,0.02),mode="expand")
plt.grid(ls="--",color="grey")
plt.subplots_adjust(left=0.09,bottom=0.095,right=0.967,top=0.91)
plt.savefig(dir_graphics+"exp.png",dpi=200)
plt.clf()
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dotx(x,t):
    a = x[0]
    e = x[1]
    return [-(16/(5*a**3))*(1+(73/24)*e**2+(37/96)*e**4)/((1-e**2)**(7/2)),
            -(76/(15*a**4))*e*(1+(121/304)*e**2)/((1-e**2)**(5/2))]
def a(T_s):
    return (m_sol*M*(c*T_s/(2*np.pi))**2)**(1/3)

def T(a_m):
    return (2*np.pi/c)*(a_m**3/(M*m_sol))**(1/2)
def solucion(x0,tt_int):
    print ('Se resuelve con at0 = %2.f y e0 = %2.f'%(x0[0],x0[1]))
    sol = odeint(dotx,x0,tt_int)
    at_todos = sol[:,0]
    # verifica si at llega a 2. En caso positivo corta el arreglo de soluciones
    restriccion = np.where(at_todos<2)[0]
    if len(restriccion)!=0:
        pos_ttmax = restriccion[0] # determina el tiempo en el que at=2
        print('Acortando intervalo a tt_max = '+str(tt_int[pos_ttmax]))
    else: 
        pos_ttmax = len(tt_int)
    tt = tt_int[:pos_ttmax]
    t_a = tt*R_ast/c/31557600 # el tiempo, en años
    at = sol[:pos_ttmax,0]
    e = sol[:pos_ttmax,1]
    a_m = at*R_ast # solución de a, en metros
    T_s = T(a_m) # solución de T, en segundos
    return tt,t_a,at,e,a_m,T_s
def g(e):
    return e**(12/19)*(1+121*e**2/304)**(870/2299)/(1-e**2)
dir_graphics="../images/"
T0_d = 0.322997448911 # periodo inicial, en días
e0 = 0.6171334 # excentricidad inicial
M_c = 1.3886 # masa de la compañera, en masas solares
M_p = 1.4398 # masa del pulsar, en masas solares
c = 299792458 # rapidez de la luz, en metros por segundo
MGcm3 = 4.925490947E-6 # MG/c^3, en segundos
m_sol = MGcm3*c # parametro de masa del Sol m=GM/c^2, en metros
M = M_c+M_p # masa total, en masas solares
mu = (M_c*M_p)/M # masa reducida, en masas solares
R_ast = m_sol*(4*mu*M**2)**(1/3) # R_\ast en metros
T0_s = T0_d*86400 # periodo inicial, en segundos
a0_m = a(T0_s) # a inicial, en metros
at0 = a0_m/R_ast # a tilde inicial
tt_int_max = 10**22 # tiempo adimensional máximo de integración. Con este valor se llega hasta a=2
tt_int = np.linspace(0,tt_int_max,100000) # tiempos en los que se integrará el sistema
print('tt_int_max = '+str(tt_int_max))
x0 = [at0,e0] # valores iniciales
tt,t_a,at,e,a_m,T_s = solucion(x0,tt_int) # calcula y asigna valores de la solución
a_m=a_m*1e-9
t_a=t_a*1e-8
plt.plot(t_a,a_m,color="#b76935",lw=3,label="semieje mayor")
plt.plot(t_a,e,color="#143642",lw=3,label="excentricidad")
plt.yticks(np.arange(0,2+0.2,0.2))
plt.ylim(0,2)
plt.xlim(0,3)
plt.xlabel(r'Tiempo ($10^8$)')
plt.ylabel(r'Distancia ($10^9$m) / excentricidad')
plt.grid(ls="--",color="grey")
plt.legend(frameon=False,fontsize=13)
plt.subplots_adjust(left=0.124,bottom=0.14,right=0.95,top=0.964)
plt.savefig(dir_graphics+"a_adim.png",dpi=200)
plt.clf()

T_h = T_s/3600. # periodo orbital, en horas
plt.figure(figsize=(8,5))
plt.plot(t_a,T_h,lw=3,color="#1a5b92")
plt.xlim(0,3)
plt.ylim(0,8)
plt.xlabel(u'$t$ (años)')
plt.ylabel(r'$T$ (horas)')
plt.grid(ls="--",color="grey")
plt.savefig(dir_graphics+"periodo.png",dpi=200)
plt.clf()

ee=np.linspace(0,1,100)
plt.plot(ee,g(ee),color="#16db93",lw=3)
plt.yscale('log')
plt.ylim(0,100)
plt.xlim(0,1)
plt.xlabel(r'$e$',fontsize=15)
plt.ylabel(r'$g$',fontsize=15)
plt.grid(ls="--",color="grey")
plt.savefig(dir_graphics+"gvse.png",dpi=200)
plt.clf()

plt.plot(e,at*R_ast,color="#0582ca",label=u'sol. numérica')
ee = np.linspace(min(e),e0,10)
a_an = a0_m*g(ee)/g(e0)
plt.plot(ee,a_an,'o',color="#051923",label=u'sol. analítica')
plt.ylim(0,2e9)
plt.xlim(0,0.7)
plt.xlabel(r'$e$')
plt.ylabel(r'$a$')
plt.legend(frameon=False,fontsize=14)
plt.grid(ls="--",color="grey")
plt.savefig(dir_graphics+"solana_solnum.png",dpi=200)
plt.clf()

t_max_a = 30 # tiempo de integración, en años
tt_int_max = 31557600*c*t_max_a/R_ast #tiempo adimensional máximo de integración

tt_int = np.linspace(0,tt_int_max,100000)
print('tt_int_max = '+str(tt_int_max))

tt,t_a,at,e,a_m,T_s = solucion(x0,tt_int)
dota = dotx(x0,0)[0]
dotT = (3/2)*(c/R_ast)*(T0_s/at0)*dota
data = np.loadtxt("data-HW.csv",delimiter=",")
t_exp = data[:,0]-data[0,0]
Delta_t_exp = data[:,1]
n = np.arange(40000)
t_n = (n*T0_s+dotT*T0_s*n*(n-1)/2.)/31557600. # tiempo, en años
Delta_t_n = dotT*T0_s*n*(n-1)/2 #retraso acumulado, en segundos
plt.plot(t_n,Delta_t_n,color="#3fc1c0",label='RG',lw=3)
plt.hlines(0,0,40, color='#4f772d',label='Newtoniano',lw=3)
plt.xlabel(u'Tiempo (años)')
plt.ylabel(r'Retraso acumulado (s)')
plt.xlim(0,35)
plt.ylim(-45,1)
plt.plot(t_exp,Delta_t_exp,'o',color="#1d4e89",label='Datos')
plt.legend(loc=3,frameon=False,fontsize=14)
plt.grid(ls="--",color="grey")
plt.savefig(dir_graphics+"exp.png",dpi=200)
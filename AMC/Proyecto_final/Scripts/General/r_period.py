import Functions as oq
import numpy as np
import matplotlib.pyplot as plt
N = 35
a = 3
# Calculate the plotting data
xvals = np.arange(35)
yvals = [np.mod(a**x, N) for x in xvals]
# Use matplotlib to display it nicely
fig, ax = plt.subplots()
ax.plot(xvals, yvals,lw=3,color="#6930c3",alpha=0.5,ls="--")
ax.scatter(xvals,yvals,c="#4ea8de")
ax.set(xlabel='$x$', ylabel='$%i^x$ mod $%i$' % (a, N),
       title="Ejemplo de la función periodo en un Algoritmo de Shor")
r = yvals[1:].index(1) +1 
plt.annotate(text='', xy=(0,1), xytext=(r,1), arrowprops=dict(arrowstyle='<->'))
plt.annotate(text='$r=%i$' % r, xy=(r/3,1.5))
plt.savefig("../../Graphics/period.png",dpi=200)
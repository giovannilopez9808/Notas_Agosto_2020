import Functions as oq
import numpy as np
import matplotlib.pyplot as plt
N = 35
a = 3
# Calculate the plotting data
xvals = np.arange(36)
yvals = [np.mod(a**x, N) for x in xvals]
# Use matplotlib to display it nicely
fig, ax = plt.subplots()
ax.set_yticks(np.arange(0,40,4))
ax.set_xticks(np.arange(0,40,5))
ax.set_ylim(0,36)
ax.set_xlim(0,35)
ax.grid(ls="--",color="grey",alpha=0.7)
ax.plot(xvals, yvals,lw=3,color="#6930c3",alpha=0.7,ls="--")
ax.scatter(xvals,yvals,c="#4ea8de")
ax.set(xlabel='$x$', ylabel='$%i^x$ mod $%i$' % (a, N),)
r = yvals[1:].index(1) +1 
plt.annotate(text='', xy=(0,1), xytext=(r,1), arrowprops=dict(arrowstyle='<->'))
plt.annotate(text='$r=%i$' % r, xy=(r/3,1.5))
plt.savefig("../../Graphics/period.png",dpi=200)
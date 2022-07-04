import matplotlib.pyplot as plt
import numpy as np


N = int(1e6)

tri = np.loadtxt('tri.dat')

x = np.linspace(-4,4,40,dtype='double')

cdf = []

for i in range(0,40):

    n_arr = np.nonzero(tri<x[i])
    n = np.size(n_arr)
    cdf.append(n/N)


def t_cdf(x):
    if(x<=0): return 0
    if(x>0 and x<=1) : return (x*x/2)
    if(x>1 and x<=2) : return (2*x - x*x/2 -1)
    else: return 1
vec_tri_cdf = np.vectorize(t_cdf,otypes=[float])
plt.plot(x,cdf,'bo')
plt.plot(x,vec_tri_cdf(x),'orange')
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(['Simulation','Analysis'])
plt.savefig('../figs/tri_cdf.png')
plt.show()
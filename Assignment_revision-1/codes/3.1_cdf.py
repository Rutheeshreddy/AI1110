import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
N = int(1e6)

gau = np.loadtxt('rand.dat')

x = np.linspace(-4,4,30,dtype='double')

cdf = []

for i in range(0,30):

    n_arr = np.nonzero(gau<x[i])
    n = np.size(n_arr)
    cdf.append(n/N)
def V(x):
    if(x<=0): 
        return 0
    else: 
        return (1 -mp.exp(-x/2) ) 
v = np.vectorize(V,otypes=[float])
plt.plot(x,cdf,'bo')
plt.plot(x,v(x),'orange')
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(['Simulation','Analysis'])
plt.savefig('../figs/rand_cdf.png')
plt.show()
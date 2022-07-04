import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp

N = int(1e6)

gau = np.loadtxt('gau.dat')

x = np.linspace(-4,4,30,dtype='double')

cdf = []

for i in range(0,30):

    n_arr = np.nonzero(gau<x[i])
    n = np.size(n_arr)
    cdf.append(n/N)

def Q(x):
    return (mp.erfc(x/mp.sqrt(2))/2)
def g_cdf(x):
    return 1 - Q(x)
vec_gau_cdf = np.vectorize(g_cdf,otypes=[float])
plt.plot(x,cdf,'bo')
plt.plot(x,vec_gau_cdf(x),'orange')
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(['Simulation','Analysis'])
plt.savefig('../figs/gauss_cdf.png')
plt.show()



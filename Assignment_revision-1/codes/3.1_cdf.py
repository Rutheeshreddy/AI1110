import matplotlib.pyplot as plt
import numpy as np

N = int(1e6)

gau = np.loadtxt('rand.dat')

x = np.linspace(-4,4,30,dtype='double')

cdf = []

for i in range(0,30):

    n_arr = np.nonzero(gau<x[i])
    n = np.size(n_arr)
    cdf.append(n/N)

plt.plot(x,cdf)
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.savefig('../figs/rand_cdf.png')
plt.show()
import matplotlib.pyplot  as plt
import numpy as np

N = int(1e6)

uni_array = np.loadtxt('uni.dat',dtype='double')
cdf = []
x = np.linspace(-4,4,30)

for i in range(0,30):
   n_arr = np.nonzero(uni_array<x[i])
   n = np.size(n_arr)
   cdf.append(n/N)

plt.plot(x,cdf)
plt.grid()
plt.xlabel('$x$'); plt.ylabel('$F_X(x)$')
plt.savefig('../figs/uni_cdf.png')
plt.show()



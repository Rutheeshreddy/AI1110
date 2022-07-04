import matplotlib.pyplot  as plt
import numpy as np

N = int(1e6)

uni_array = np.loadtxt('uni.dat',dtype='double')
cdf = []
x = np.linspace(-4,4,40)

for i in range(0,40):
   n_arr = np.nonzero(uni_array<x[i])
   n = np.size(n_arr)
   cdf.append(n/N)
y = np.concatenate([np.zeros(20) , np.linspace(0,1,5) ,np.ones(15)])
plt.plot(x,cdf,'bo')
plt.plot(x,y,'orange')
plt.grid()
plt.xlabel('$x$'); plt.ylabel('$F_X(x)$')
plt.legend(['Simulation','Analysis'])
plt.savefig('../figs/uni_cdf.png')
plt.show()



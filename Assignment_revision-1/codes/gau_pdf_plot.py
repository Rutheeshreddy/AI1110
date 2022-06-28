import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt



points=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,points)
N = int(1e6) 
cdf = [] 
pdf = [] 
h = 2*maxlim/(points-1)

randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,points):
	cdf_ind = np.nonzero(randvar < x[i]) 
	cdf_n = np.size(cdf_ind) 
	cdf.append(cdf_n/N) 

	
for i in range(0,points-1):
	test = (cdf[i+1]-cdf[i])/(x[i+1]-x[i]) # approximating differential
	pdf.append(test)

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)

plt.plot(x[0:(points-1)].T,pdf,'o')
plt.plot(x,vec_gauss_pdf(x))
plt.grid() 
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../figs/gauss_pdf.png')

plt.show()


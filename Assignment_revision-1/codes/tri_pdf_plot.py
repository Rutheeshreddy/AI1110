import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt



points=100
maxlim=6.0
x = np.linspace(-maxlim,maxlim,points)
N = int(1e6) 
cdf = [] 
pdf = [] 
h = 2*maxlim/(points-1)

randvar = np.loadtxt('tri.dat',dtype='double')

for i in range(0,points):
	cdf_ind = np.nonzero(randvar < x[i]) 
	cdf_n = np.size(cdf_ind) 
	cdf.append(cdf_n/N) 

	
for i in range(0,points-1):
	test = (cdf[i+1]-cdf[i])/(x[i+1]-x[i]) # approximating differential
	pdf.append(test)

def tri_pdf(x):
    if(x<=0): return 0
    if(x>0 and x<=1):
         return x
    if(x>1 and x<=2): 
        return 2-x
    else: return 0
   
 

vec_tri_pdf = scipy.vectorize(tri_pdf,otypes=[float])

plt.plot(x[0:(points-1)].T,pdf,'o')
plt.plot(x,vec_tri_pdf(x))
plt.grid() 
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Simulation","Analysis"])

plt.savefig('../figs/tri_pdf.png')

plt.show()

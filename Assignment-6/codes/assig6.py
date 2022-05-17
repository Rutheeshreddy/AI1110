import numpy as np
from scipy.stats import bernoulli 
N= int(1e5) 

X = bernoulli.rvs(p=0.5,size=N)

n1 = np.count_nonzero(X==0)
n2 = np.count_nonzero(X==1)

Y1 = bernoulli.rvs(p=7/12,size=n1)
Y2 = bernoulli.rvs(p=5/12,size=n1)

#Probability that Y==0

p = (np.count_nonzero(Y1==0)+np.count_nonzero(Y2==0))/N

print("Theoretical probability is 0.5. Practical probability is {}",format(p))
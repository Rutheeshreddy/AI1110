# C.Rutheesh Reddy
# CS21BTECH11014

import numpy as np

N = 100000

T1 = np.random.randint(1,7,size=N)
T2 = np.random.randint(1,7,size=N)
T3 = np.random.randint(1,7,size=N)
D = [T1,T2,T3]
x = 0
for i in range(0,N):
 x = x + np.count_nonzero(D[0][i]==4 and D[1][i]==5 and D[2][i]==6)
p1 = x/N
x1 = 0
for i in range(0,N):
 x1 = x1 + np.count_nonzero(D[0][i]==4 and D[1][i]==5 )
p2 = x1/N

print("Theoretical probability is 0.1666. Practical probability is {}",format(p1/p2))
        

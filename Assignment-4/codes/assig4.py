# C.Rutheesh Reddy
# CS21BTECH11014

import numpy as np

N = 10000

T = np.random.randint(0,5,size=N)

p1 = np.count_nonzero(T==1)/N    #Choosing 0 as we can choose any number between 0 and 4

print("Theoretical probability for (i) is 0.2.\nPractical probability for (i) ",p1)

T1 = np.random.randint(0,5,size=N)

T2 = T - T1

p2 =(np.count_nonzero(T2==-1)+np.count_nonzero(T2==-1))/(N)

print("Theoretical probability for (ii) is 0.32.\nPractical probability for (ii) is ",p2)
        

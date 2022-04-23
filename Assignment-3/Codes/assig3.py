import numpy as np
import pandas as pd

df = pd.read_excel('assig3.xlsx')
data=np.array(df)
print(data)
C0 = [data[i][1]  for i in range(0,5,1)]
C1 = [data[i][2]  for i in range(0,5,1)]
C2 = [data[i][3]  for i in range(0,5,1)]
C3 = [data[i][4]  for i in range(0,5,1)]

N=sum(C0)+sum(C1)+sum(C2)+sum(C3) 
print('Total number of families is {}'.format(N))

p1 = data[2][3]/N 
print('Probability of families earning Rs.10000 – 13000 per \
 month and owning 2 vehicles is {0:.3f}'.format(p1))

p2 = data[4][2]/N
print('Probability of families earning Rs.16000 or more per \
 month and owning 1 vehicle is {0:.3f}'.format(p2))

p3 = data[0][1]/N
print('Probability of families earning Rs.7000 or less per \
 month and owning no vehicle is {0:.4f}'.format(p3))

p4 = data[3][4]/N
print('Probability of families earning Rs.13000 – 16000 per \
 month and owning more than 2 vehicles is {0:.4f}'.format(p4))

n=sum(C0)+sum(C1)
p5=n/N
print('Probability of families owning not more than 1 vehicle is {0:.3f}'.format(p5))


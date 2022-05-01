import numpy as np
import pandas as pd

df = pd.read_excel('assig3.xlsx')
cols_sum = df.iloc[:,1:5].sum(axis=0)
N=sum(cols_sum) 
print('Total number of families is {}'.format(N))

p1 = df.iat[2,3]/N 
print('Probability of families earning Rs.10000 – 13000 per \
 month and owning 2 vehicles is {0:.3f}'.format(p1))

p2 = df.iat[4,2]/N
print('Probability of families earning Rs.16000 or more per \
 month and owning 1 vehicle is {0:.3f}'.format(p2))

p3 = df.iat[0,1]/N
print('Probability of families earning Rs.7000 or less per \
 month and owning no vehicle is {0:.4f}'.format(p3))

p4 = df.iat[3,4]/N
print('Probability of families earning Rs.13000 – 16000 per \
 month and owning more than 2 vehicles is {0:.4f}'.format(p4))

partial_sum=df.iloc[:,1:3].sum(axis=0)
n=sum(partial_sum)
p5=n/N
print('Probability of families owning not more than 1 vehicle is {0:.3f}'.format(p5))

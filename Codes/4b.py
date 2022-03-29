import matplotlib.pyplot as plt
import numpy as np

plt.axis('equal')

x=np.arange(-5,10,1)

y=(3*x-7)/5
plt.plot(x,y)

y1=(-5*(4*x+9))/12
plt.plot(x,y1)
plt.legend()
plt.show()
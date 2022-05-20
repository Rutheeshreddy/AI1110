import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

x=np.arange(0,6)
y=binom.pmf(x,5,0.8)
plt.stem(x,y)
plt.show()
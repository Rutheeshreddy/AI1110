from scipy.stats import binom

x=binom.pmf(4,5,0.8)

print("Required probability is {0:.3f}".format(x))
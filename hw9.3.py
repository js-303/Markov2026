import numpy as np

k = np.arange(0, 21, 1)

ks = []
for i in k:
    k = np.exp((-2/3))*(((2/3)**i)/np.math.factorial(i))
    ks.append(k)
prob = np.cumsum(ks)
print(prob,ks)
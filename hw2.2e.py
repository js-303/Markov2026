import numpy as np
from math import log,e
import matplotlib.pyplot as plt

n = 10**6

def sample(n):
    X = []
    for _ in range(n):
        w_1 = np.random.uniform(0, 1)
        w_2 = np.random.uniform(0, 1)
        u_1 = np.random.uniform(0, 1)
        t = -log(w_1*w_2)
        y = t*u_1
        z = t - y
        x = y+z
        X.append(x)
    return X

X = sample(n)

print(X)

xx = np.linspace(0, 10, 1000)
f = lambda x: x*e**(-x)

fig, ax = plt.subplots(figsize=(8,6))
ax.set_title("Comparison of Theoretical PDF and Samples of X")
ax.plot(xx, f(xx), color='red', label='Theoretical PDF')
ax.hist(X, bins=100, density=True, label='Samples of X')
ax.set_xlabel('x')
ax.set_ylabel("$f_{X}(x)$")
plt.legend(loc='upper right')
plt.show()



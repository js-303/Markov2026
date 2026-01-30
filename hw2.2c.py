import numpy as np
from math import e
import time
import matplotlib.pyplot as plt

start = time.time()
f = lambda x: x*e**(-x)
g = lambda x: (1/2)*e**(-x/2)
c = 4/e
n = 10**6

def AR(f, g, c, n):
    X = []
    count = 0
    h = lambda x: f(x)/(c*g(x))
    while count < n:
        w_1 = np.random.uniform(0, 1)
        y = -2*np.log(w_1)
        u_2 = np.random.uniform(0, 1)
        if u_2 < h(y):
            X.append(y)
            count += 1
    return X

X = AR(f, g, c, n)

end = time.time()

print("Execution time:", end - start)

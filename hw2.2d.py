import numpy as np
from math import log,e
import time

start = time.time()
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

Z = sample(n)
end = time.time()
print(Z)
print("Execution time:", end - start)



    
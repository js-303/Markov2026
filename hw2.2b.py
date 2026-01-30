import numpy as np
from scipy import optimize
from math import e
import time

start = time.time()
n = 10**6

F = lambda x: -x*e**(-x)-e**(-x)+1

def generate(F, n):
    U = np.random.uniform(0, 1, n)
    R = []
    for u in U:
        g = lambda x: F(x) - u
        r = optimize.newton(g, x0=1)
        if r >= 0:
            R.append(r)
    return R

R = generate(F, n)

end = time.time()

print("Execution time:", end - start)

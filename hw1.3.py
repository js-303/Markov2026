import numpy as np
from scipy import integrate
from math import floor
import matplotlib.pyplot as plt

A = np.arange(1,5.1,0.1)
M = []

for i in range(len(A)):
    M.append(floor(10**A[i]))

def uniform_points(x_min,x_max,y_min,y_max, N):
    x_cord = np.random.uniform(low=x_min,high=x_max,size=N)
    y_cord = np.random.uniform(low=y_min,high=y_max,size=N)
    return np.vstack((x_cord,y_cord))

xx = np.linspace(0,1,1000)
f = lambda xx: (xx**4)/(1+xx**6)

fig, ax = plt.subplots(figsize=(8,6))

def estimate(points):
    success = 0
    fail = 0
    for i in range(len(points[0])):
        x_cord = points[0][i]
        if points[1][i] < f(x_cord):
            success += 1
        else:
            fail += 1
    return(success/(fail+success))

def E(N):
    E = []
    for n in range(len(N)):
        points = uniform_points(0,1,0,1,N[n])
        e = round(estimate(points),4)
        E.append(e)
    return E

I, error = integrate.quad(f,0,1)
I = round(I,4)
error = round(error,4)
print("I: ", I, "err: ",error)
ax.set_title("Comparison of E(N) and I")
ax.set_ylabel("E(N) estimate")
ax.set_xlabel("N (log)")
ax.set_xscale('log')
ax.axhline(I, label='numerical solution to I')
ax.scatter(M, E(M), label='estimate at N')
ax.legend(loc='upper right')
plt.show()
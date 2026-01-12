import numpy as np
from scipy import integrate 
import matplotlib.pyplot as plt

def uniform_points(x_min,x_max,y_min,y_max, num_points):
    x_cord = np.random.uniform(low=x_min,high=x_max,size=num_points)
    y_cord = np.random.uniform(low=y_min,high=y_max,size=num_points)
    return np.vstack((x_cord,y_cord))

points = uniform_points(0,1,0,1,5000)
"""
for i in range(len(points[0])):
    x_cord = points[0][i]
    g = lambda x_cord: (x_cord**4)/(1+x_cord**6)
    if g <= points[1][i]:
        ax.scatter(x_cord,g, color=r)
"""
xx = np.linspace(0,1,1000)
f = lambda xx: (xx**4)/(1+xx**6)
success = 0
fail = 0
fig, ax = plt.subplots(figsize=(8,6))
for i in range(len(points[0])):
    x_cord = points[0][i]
    print("x cord: ",x_cord)
    #g = lambda x_cord: (x_cord**4)/(1+x_cord**6)
    if points[1][i] <= f(x_cord):
        print("success! ", "g(x cord): ",f(x_cord), "y points: ", points[1][i])
        ax.scatter(points[0][i],points[1][i], color='red')
        success += 1
    else:
        print("fail! ","g(x cord): ",f(x_cord), "y points: ", points[1][i])
        ax.scatter(points[0][i],points[1][i], color='blue')
        fail += 1
print("success: ", success, "fail: ", fail, "ratio: ", (success)/(fail))

I, error = integrate.quad(f,0,1)
print("I: ", I, "err: ",error)
ax.plot(xx, f(xx), color='black')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
plt.show()
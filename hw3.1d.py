import numpy as np
import matplotlib.pyplot as plt
from math import exp, sqrt



f = lambda x: (1/3)*x*(1+x)*np.exp(-x)
g = lambda x: a**2*x*np.exp(-a*x)
c = lambda a: (1/(3*a**2))*(1/(1-a))*np.exp(-a)

a = sqrt(3)-1

xx = np.linspace(0,10,1000)
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(xx, f(xx), color='black', label='f(x)')
ax.plot(xx, c(a)*g(xx), color='red', label=r'$c(a^{*})g_{a*}(x))$')
ax.set_title(r"f(x) and $c(a^{*})g_{a*}(x)$")
ax.set_ylabel(r"f(x) / $c(a^{*})g_{a*}(x)$")
ax.set_xlabel("x")
ax.legend(loc='upper right')
plt.show()
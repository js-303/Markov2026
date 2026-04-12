import numpy as np
from math import factorial
import matplotlib.pyplot as plt

f = lambda t: np.exp(-3.5*(1-t/90)) * sum((3*(1-t/90)**2)**g / factorial(g)**2 for g in range(13))
tt = np.linspace(0, 90, 1000)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(tt, f(tt), label='f(t)', color='blue')
ax.set_xlabel('Time (minutes)')
ax.set_ylabel('Probability')
ax.set_title('Probability of Tie')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

y = lambda m: np.log(m)
m = np.arange(2, 2000)

max_m = m.max()
k = np.arange(1, max_m)              
H_cumsum = np.cumsum(1.0 / k)        
tau_m = H_cumsum[m - 2]

y = lambda m: np.log(m)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(m, y(m), label='Deterministic')
ax.plot(m, tau_m, label='Stochastic')
ax.set_xlabel('m')
ax.set_ylabel('Hitting Time')
ax.set_title('Stochastic vs Deterministic Hitting Time')
ax.legend()
plt.show()
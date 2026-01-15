import numpy as np
import matplotlib.pyplot as plt

N = 10**6
t = np.linspace(0, 60, 1000)
T = lambda t: (3*t**2/(60)**3)

def arivals(a,b,N):
    moe = np.random.uniform(low=a, high=b, size=N)
    agnes = np.random.uniform(low=a, high=b,size=N)
    dorothy = np.random.uniform(low=a, high=b,size=N)
    t_random = [] 
    for i in range(N):
        t_random.append(max(moe[i],agnes[i],dorothy[i]))
    return t_random

T_sim = arivals(0,60,N)

fig, ax = plt.subplots(figsize = (8,6))
ax.plot(t, T(t), label='Theoretical PDF')
ax.hist(T_sim, bins=1000, density=True, label='Simulated T')
ax.set_title("Comparison of Randomly Generated T and the PDF of T")
ax.set_xlabel("t")
ax.set_ylabel("$f_{T}(t)$")
ax.legend(loc='upper right')
plt.show()

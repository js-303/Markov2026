import numpy as np
import matplotlib.pyplot as plt

k = np.arange(2,11,1)
N = []
for i in range(len(k)):
    n = 2**k[i]
    N.append(n)

sims = 10**6

def simulate_Y_n(N, sims):
    Y_vals = {}
    for n in N:
        X_i = np.random.poisson(lam=1, size=(sims,n))
        Y = (np.sum(X_i, axis=1)-n)/np.sqrt(n)
        Y_vals[n] = np.mean(Y**3)
    return Y_vals

S_sim = simulate_Y_n(N,sims)

xx = np.linspace(N[0], N[-1], 10000)
f = lambda x: 1/np.sqrt(x)
fig, ax = plt.subplots(figsize=(8,6))
ax.set_title(r"Comparison of Theoretical and Numerical Skewness")
ax.set_xlabel("n (log)")
ax.set_ylabel(r"S(n)/$E[Y_n^3]$ (log)")
ax.set_ylim(1e-2, 1)
ax.scatter(list(S_sim.keys()), list(S_sim.values()), color='black', label=r'Numerical $E[Y_{n}^3]$')
ax.loglog(xx, f(xx), color='red',label=r'Theoretical S(n)=$\frac{1}{\sqrt{n}}$')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()
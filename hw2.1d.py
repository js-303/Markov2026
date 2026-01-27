import numpy as np
import matplotlib.pyplot as plt

N = [100,1000,10000]

def sample(N):
    U = {}
    for n in N:
        U[n] = np.random.uniform(0, 1, n)
    return U

U = sample(N)

def generate(U,N):
    X = {}
    X_vals = {}
    for n in N:
        print(n, U[n])
        X_vals[n] = []
        for u in U[n]:
            x = (10/np.cbrt(1-u))
            print(x)
            X_vals[n].append(x)
        X[n] = np.array(X_vals[n])
    return X

X = generate(U,N)
print(X)

xx = np.linspace(10.1, 60, 1000)
f = lambda x: 3000*x**-4

fig, axs = plt.subplots(1,3,figsize=(8,6))
fig.suptitle("Comparison of Theoretical and Simulated PDF of X")
axs[0].plot(xx, f(xx), color='red', label='Theoretical PDF')
axs[0].hist(X[100], bins=100, density=True, label='Samples n=100')
axs[0].set_title('n = 100')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Density')
axs[0].legend()
axs[0].set_xlim(10, 60)
axs[1].plot(xx, f(xx), color='red', label='Theoretical PDF')
axs[1].hist(X[1000], bins=100, density=True, label='Samples n=1000 ')
axs[1].set_title('n = 1000')
axs[1].set_xlabel('x')
axs[1].set_ylabel('Density')
axs[1].legend()
axs[1].set_xlim(10, 60)
axs[2].plot(xx, f(xx), color='red', label='Theoretical PDF')
axs[2].hist(X[10000], bins=100, density=True, label='Samples n=10000')
axs[2].set_title('n = 10000')
axs[2].set_xlabel('x')
axs[2].set_ylabel('Density')
axs[2].legend()
axs[2].set_xlim(10, 60)

plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

S = [0,1,2,3,4]


p = np.array([[0,1,0,0,0],
              [1/3,0,2/3,0,0],
              [0,1/2,0,1/2,0],
              [0,0,2/3,0,1/3],
              [0,0,0,1,0]])
A = p.T

evals, evecs = np.linalg.eig(A)

print(f"Eigenvalues: {evals}")
print(f"Eigenvectors: {evecs}")

q_50 = np.linalg.matrix_power(A, 50) @ np.array([0,0,1,0,0])
pi = np.array([1/12,1/4,1/3,1/4,1/12])

print(q_50)

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(S, q_50, label=(r'$q_{50}$'))
ax.scatter(S, pi, label=(r'$\pi$'))
ax.legend() 
ax.set_title(r'Comparison of $q_{50}$ and $\pi$')
ax.set_xlabel('State')
ax.set_xticks(S)
ax.set_ylabel('Probability')
plt.show()


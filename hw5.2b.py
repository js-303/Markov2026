import numpy as np

K = 0.1
a = 0.04
b = 0.16

S = [1,2,3,4,5]
p = np.zeros((5,5))

for n in S:
    if n+1 <= S[-1]:
        p_n = K*np.exp(a*n)
        p[n-1][n] = p_n
    if n-1 >= S[0]:
        q_n = K*np.exp(b*(n-1))
        p[n-1][n-2] = q_n
    if n-1 >= S[0] and n+1 <= S[-1]:
        p[n-1][n-1] = 1 - p[n-1][n] - p[n-1][n-2]
    elif n-1 < S[0]:
        p[n-1][n-1] = 1 - p[n-1][n]
    elif n+1 > S[-1]:
        p[n-1][n-1] = 1 - p[n-1][n-2]

P_T = p.T
evals, evecs = np.linalg.eig(P_T)
for i in range(len(evals)):
    if np.isclose(evals[i], 1, atol=1e-13):
        print("eval:", i)
        print("evec:", evecs[:, i])
        selected_evec = evecs[:, i]
        evec_sd = selected_evec/np.linalg.norm(selected_evec, ord=1)

print("evecs: ", evecs)
print("evals: ", evals)
print("evec_sd: ", evec_sd)
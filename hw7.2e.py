import numpy as np

n = 10**5
t= 48

results = {}
D = {}

for i in range(n):
    N = np.random.poisson(lam=6*t)
    N_A_given_N = np.random.binomial(N, p=0.5)
    N_B_given_N = N - N_A_given_N
    results[i] = [N_A_given_N, N_B_given_N]

for i in range(n):
    N_A = results[i][0]
    N_B = results[i][1]
    D[i] = 2*(N_A - N_B)

E_D = np.mean(list(D.values()))
V_D = np.mean([D[i]**2 for i in range(n)]) - E_D**2
count = 0
for i in range(n):
    if D[i] == 0:
        count += 1
P = count/n
print(D)
print(f"E[D(t)]: {E_D}")
print(f"Var[D(t): {V_D}")
print(f"P(D(t) = 0): {P}")

import numpy as np
import matplotlib.pyplot as plt

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

    
print(p)


n = 10**6

def m_process(p, start_state, n):
    state_index = S.index(start_state)
    state_sequence = [start_state]

    for _ in range(n):
        state_index = np.random.choice(range(len(S)), p=p[state_index])
        state_sequence.append(S[state_index])

    return state_sequence

process = m_process(p, 2, n)

counts = {}
ratios = {}
for s in S:
    counts[s] = 0
for state in process:
    counts[state] += 1
for s in S:
    ratios[s] = counts[s] / n

print(f"counts: {counts}")
print(f"ratios: {ratios}")

pi_1 = 0.29651
db_sd = [pi_1, pi_1*np.exp(-0.12), pi_1*np.exp(-0.36), pi_1*np.exp(-0.72), pi_1*np.exp(-1.2)]

P_T = p.T
evals, evecs = np.linalg.eig(P_T)
for i in range(len(evals)):
    if np.isclose(evals[i], 1, atol=1e-13):
        print("eval:", i)
        print("evec:", evecs[:, i])
        selected_evec = evecs[:, i]
        evec_sd = selected_evec/np.linalg.norm(selected_evec, ord=1)

barwidth = 0.2
x = np.arange(len(S))
fig, ax1 = plt.subplots(figsize=(8,6))
ax1.bar(x+1, ratios.values(), width=barwidth, edgecolor='blue', linewidth=0.5, alpha=0.9,label='% of time in state')
ax1.bar(x+1-barwidth, db_sd, width=barwidth, edgecolor='orange', linewidth=0.5, alpha=0.3, label='Detailed Balance')
ax1.bar(x+1+barwidth, evec_sd, width=barwidth, edgecolor='green', linewidth=0.5, alpha=0.3, label='Eigenvector')
ax1.set_title("Fraction of Time Spent in Each State/ \n Detailed Balance/ \n Eigenvector Stationary Distribution")
ax1.set_xlabel("State")
ax1.set_ylabel("Fraction of Time/Probability")
ax1.set_xticks(S)
ax1.legend()  
plt.tight_layout()
plt.show()


import numpy as np

S = np.arange(0,21,1)

L = 20
alpha = 1
beta = 1

def simulate_ctmc(n_0, L, alpha, beta):
    t = 0.0
    times = [0.0]
    states = [n_0]
    n = n_0
    while n < L+1:
        if n == 0:
            hold = np.random.exponential(1/alpha)
            t+=hold
            n+=1
        elif 0<n<20:
            hold = np.random.exponential(1/(alpha+beta))
            t+=hold
            if np.random.rand() < alpha/(alpha+beta):
                n+=1
            else:
                n-=1
        elif n == L:
            break
        times.append(t)
        states.append(n)
    return np.array(times), np.array(states)

def simulate_many(n_0, L, N, alpha, beta):
    hit_L = []
    hit_L2 = []
    for i in range(N):
        times, states = simulate_ctmc(n_0, L, alpha, beta)
        hit_L.append(times[-1])
        hit_L2.append(times[-1]**2)
        hit_L_sum = np.sum(hit_L)
        hit_L2_sum = np.sum(hit_L2)
        var = (hit_L2_sum / N) - (hit_L_sum / N)**2
    return (hit_L_sum / N), var

m_0_sim, var = simulate_many(0, L, 1000, alpha, beta)
m_0_theo = L*(L+1) / 2

print(f"m_0_sim = {m_0_sim}, m_0_theo = {m_0_theo}, var = {var}")
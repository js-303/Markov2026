import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

N_1 = 100
N_2 = 1000
N_3 = 10000
N_4 = 100000
N = [N_1, N_2, N_3, N_4]

S = np.array([1, 2, 3, 4])
init_prob = np.array([1/3, 2/3, 0, 0])

Q = np.array([[-1, 1, 0, 0],
              [0, -1, 1, 0],
              [0, 0, -1, 1],
              [1, 0, 0, -1]])


def simulate_ctmc(Q, start_state, max_time=5.0):
    times = [0.0]
    states = [int(start_state)]
    current_state = int(start_state)
    current_index = current_state - 1
    current_time = 0.0

    while current_time < max_time:
        rate = -Q[current_index, current_index]
        if rate <= 0:
            break

        holding_time = np.random.exponential(1 / rate)
        current_time += holding_time
        if current_time > max_time:
            break

        transition_rates = Q[current_index].copy()
        transition_rates[current_index] = 0.0
        transition_probs = transition_rates / transition_rates.sum()
        next_index = np.random.choice(len(Q), p=transition_probs)
        next_state = next_index + 1

        times.append(current_time)
        states.append(int(next_state))
        current_state = next_state
        current_index = next_index

    return np.array(times), np.array(states)


def get_state_at(times, time_jumps, states):
    state_values = np.zeros(len(times))
    idx = 0
    for i, t in enumerate(times):
        while idx + 1 < len(time_jumps) and time_jumps[idx + 1] <= t:
            idx += 1
        state_values[i] = states[idx]
    return state_values

def simulate_many(Q, N, times):
    count_state1 = np.zeros(len(times))
    for i in range(N):
        start_state = np.random.choice(S, p=init_prob)
        time_jumps, states_jumps = simulate_ctmc(Q, start_state, max_time=times[-1])
        state_values = get_state_at(times, time_jumps, states_jumps)
        count_state1 += (state_values == 1)
    return count_state1 / N

g = lambda t: (1/4)-(1/12)*np.exp(-2*t)+np.exp(-t)*((1/6)*np.cos(t)-(1/3)*np.sin(t))

tt = np.linspace(0, 5, 200)
plt.figure(figsize=(10, 6))

for n in N:
    f_t = simulate_many(Q, n, tt)
    plt.plot(tt, f_t, label=f"N={n}", alpha=1)
plt.plot(tt, g(tt), 'r-', linewidth=2, label="Theoretical", color='grey', alpha=0.8)
plt.xlim(0, 5)
plt.ylim(0, 0.5)
plt.xlabel("t")
plt.ylabel("Fraction in state 1")
plt.title("Simulation vs Theoretical Convergence\n Stationary Distribution for State 1")
plt.legend()
plt.show()
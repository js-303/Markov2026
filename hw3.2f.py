import numpy as np

states = ["G","S","D"]

P = np.array([[9/10,1/10,0],
              [0,7/8,1/8],
              [2/5,0,3/5]])

steps = 10000

def m_process(P, start_state, steps):
    state_index = states.index(start_state)
    state_sequence = [start_state]

    for _ in range(steps):
        state_index = np.random.choice(range(len(states)), p=P[state_index])
        state_sequence.append(states[state_index])

    return state_sequence

process = m_process(P, "G", steps)

count_G = 0
for s in process:
    if s == "G":
        count_G += 1
        ratio = count_G/steps

print(ratio)
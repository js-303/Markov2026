import numpy as np

states = ["1","2","3","4","5","6"]

P = np.array([[1/2,1/2,0,0,0,0],
              [0,1/2,1/2,0,0,0],
              [1/3,0,1/3,1/3,0,0],
              [0,0,0,1/2,1/2,0],
              [0,0,0,0,0,1],
              [0,0,0,0,1,0]])

n = 10000

steps = 5

def m_process(P, start_state, steps):
    state_index = states.index(start_state)
    state_sequence = [start_state]

    for _ in range(steps):
        state_index = np.random.choice(range(len(states)), p=P[state_index])
        state_sequence.append(states[state_index])

    return state_sequence

process = m_process(P, "1", steps)

def count_X_5(process, P, n, steps):
    count = 0
    for _ in range(n):
        process = m_process(P, "1", steps)
        if process[5] == '4':
            count += 1
    ratio = count/n
    return ratio 

print(count_X_5(process, P, n, steps))
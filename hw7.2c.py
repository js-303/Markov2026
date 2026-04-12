import numpy as np
import matplotlib.pyplot as plt

T_i = np.array([])
T_A = np.array([0])
A_score = np.array([0])
while T_A[-1] < 48:
    t_i = np.random.exponential(scale=(1/3))
    T_i = np.append(T_i, t_i)
    A_score = np.append(A_score, A_score[-1] + 2)
    print(T_i)
    T_A = np.cumsum(T_i)
    print(T_A)  


T_j = np.array([])
T_B = np.array([0])
B_score = np.array([0])
while T_B[-1] < 48:
    t_j = np.random.exponential(scale=(1/3))
    T_j = np.append(T_j, t_j)
    B_score = np.append(B_score, B_score[-1] + 2)
    print(T_j)
    T_B = np.cumsum(T_j)
    print(T_B)
    

print(A_score)
print(B_score)

fig, ax = plt.subplots(figsize=(8,6))
ax.bar([T_A[i] for i in range(len(T_A)) if T_A[i] < 48], A_score[:len(T_A)-1],width=0.15, label='Team A', color='red')
ax.bar([T_B[i] for i in range(len(T_B)) if T_B[i] < 48], B_score[:len(T_B)-1],width=0.15, label='Team B', color='blue')
ax.set_xlabel('Time (minutes)') 
ax.set_xlim(0, 48)
ax.set_ylabel('Score')
ax.set_title('Score Progression of Team A and Team B')
ax.legend()
plt.show()
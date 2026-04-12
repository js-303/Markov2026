import numpy as np
import matplotlib.pyplot as plt

T = np.array([0])
T_i = np.array([0])
while T[-1] < 48:
    t_i = np.random.exponential(scale=(1/6))
    T_i = np.append(T_i, t_i)
    T = np.cumsum(T_i)
  
T_i_A = np.array([0])
T_i_B = np.array([0])
T_B = np.array([0])
T_A = np.array([0])
score_A = np.array([0])
score_B = np.array([0])
for i in range(len(T)):
    t_div = np.random.choice(['A','B'], p=[0.5, 0.5])
    if t_div == 'A':
        t_i_A = T[i]
        T_i_A = np.append(T_i_A, t_i_A)
        score_A = np.append(score_A, score_A[-1] + 2)
    elif t_div == 'B':
        t_i_B = T[i]
        T_i_B = np.append(T_i_B, t_i_B)
        score_B = np.append(score_B, score_B[-1] + 2)


print(T_i_A)
print(T_i_B)
print(score_A)
print(score_B)

fig, ax = plt.subplots(figsize=(8,6))
times_A = [T_i_A[i] for i in range(1, len(T_i_A)) if T_i_A[i] < 48]
scores_A = [score_A[i] for i in range(1, len(score_A)) if T_i_A[i] < 48]
ax.bar(times_A, scores_A, width=0.15, label='Team A', color='red')
times_B = [T_i_B[i] for i in range(1, len(T_i_B)) if T_i_B[i] < 48]
scores_B = [score_B[i] for i in range(1, len(score_B)) if T_i_B[i] < 48]
ax.bar(times_B, scores_B, width=0.15, label='Team B', color='blue')
ax.set_xlabel('Time (minutes)') 
ax.set_xlim(0, 48)
ax.set_ylabel('Score')
ax.set_title('Score Progression of Team A and Team B')
ax.legend()
plt.show()
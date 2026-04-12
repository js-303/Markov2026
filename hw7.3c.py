import numpy as np
import matplotlib.pyplot as plt

time_T = 120

lam = lambda t: 0.5*(1+(t/30)**2)
lam_max = lam(time_T)
tt = np.linspace(0, time_T, 1000)
plt.plot(tt, lam(tt))
plt.xlabel('Time')  
plt.ylabel('Lambda(t)')
plt.title('Time-varying Rate Function')
plt.grid()
plt.show()

T_n = [0]
T_i = np.array([])
T = np.array([0])
while T[-1] < time_T:
    t_i = np.random.exponential(scale=1/lam_max)
    T_i = np.append(T_i, t_i)
    T = np.cumsum(T_i)

print(T)
T = T[:len(T)-1]
sample = np.array([])
for i in range(len(T)):
    print(lam(T[i])/lam_max, (1-lam(T[i])/lam_max))
    random = np.random.choice([1, 0], p=[lam(T[i])/lam_max, 1-lam(T[i])/lam_max ])
    if random == 1:
        sample = np.append(sample, T[i])
print(sample)
print(len(T), len(sample))

fig, ax = plt.subplots()
ax.hist(sample, bins=time_T, alpha=0.6, color='g')
ax.set_xlabel('Time(Days)')
ax.set_ylabel('Reports per Day')
ax.set_title('Histogram of Sampled Reports')
plt.show()

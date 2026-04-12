import numpy as np
import matplotlib.pyplot as plt

f = lambda t : np.exp(-(7/6)*(1-(t/30)))*((1/2)*(1-(t/30)))
tt = np.linspace(0,30,1000)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(tt, f(tt), label='f(t)', color='blue')
ax.set_xlabel('Time (minutes)')
ax.set_ylabel('Probability')
ax.set_title('Probability of a Tie After A Scores at 60 Minutes')
plt.show()
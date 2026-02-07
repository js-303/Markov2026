import numpy as np

P = np.array([[9/10,1/10,0],
              [0,7/8,1/8],
              [2/5,0,3/5]])

P_50 = np.linalg.matrix_power(P, 50)

print(P_50)
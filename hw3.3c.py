import numpy as np

P = np.array([[1,0,0,0,0],
     [1/3,0,2/3,0,0],
     [0,1/3,0,2/3,0],
     [0,0,1/3,0,2/3],
     [0,0,0,0,1]])

P_4 = np.linalg.matrix_power(P, 4)

print(P_4)
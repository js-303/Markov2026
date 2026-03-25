import numpy as np


def GW(X_0,generations):
    X = X_0
    X_list = []
    X_list.append(X)
    for n in range(generations):
        if X == 0:
            break
        else:
            Z = np.random.binomial(X, 1/2)
            X = 2*Z
            X_list.append(X)
    return X_list

n = 10**3
results = []
for i in range(n):
    X_list = GW(1, 10**3)
    print(X_list, sum(X_list))
    S = sum(X_list)
    results.append(S)

count = 0
for s in results:
    if s == 3:
        count += 1
ratio = count/n

print(f"ratio: {ratio}")
import numpy as np

a = 0.49


def GW(X_0, a, generations):
    X = X_0
    X_list = []
    X_list.append(X)
    for n in range(generations):
        if X == 0:
            break
        else:
            Z = np.random.binomial(X, 1-a)
            X = 2*Z
            X_list.append(X)
    return X_list

n = 10**3
count = 0

for i in range(n):
    gw = GW(1, a, 200)
    print(gw, len(gw))
    if len(gw) != 201:
        count += 1 

ratio = count/n
print(f"ratio = {ratio}")
print(f"count = {count}")

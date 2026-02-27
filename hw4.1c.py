import numpy as np  

p = 1/4
q = 1/2
s = 1-p-q
states = ["i-1", "i", "i+1"]
transitions = [q,s,p]
i = 10

n = 10000


def gamblers(transitions, i, n):
    j_count = 0
    minus_count = 0 
    plus_count = 0
    broke_count = 0
    winnings = []
    for _ in range(n):
        j = i
        while j > 0:
            gamble = np.random.choice(states, p=transitions)
            if gamble == "i":
                j_count += 1
                winnings.append(j)
                break
            elif gamble == "i+1":
                j = j+1
                plus_count += 1
            elif gamble == "i-1":
                j = j-1
                minus_count += 1
        else:
            broke_count += 1
            winnings.append(0)
    avg_win = np.average(winnings)
    return j_count, broke_count, avg_win

print(gamblers(transitions, i, n))
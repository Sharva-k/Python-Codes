import numpy as np
n = [2,2,2,2]
n.sort()
output = []
t = 0
le = len(n)
for i in range(le-3):
    for j in range(i+1,le-2):
        for k in range(j+1,le-1):
            for l in range(k+1,le):
                if n[i] + n[j] + n[k] + n[l] == t:
                    output.append([n[i],n[j],n[k],n[l]])
result = np.unique(n)
print(result)
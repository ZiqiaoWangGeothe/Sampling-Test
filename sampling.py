import random

dist = [0.1, 0.2, 0.2, 0.05, 0.05, 0.4]

def sampling(dist):
    d = dist.copy()
    l = len(d)
    for i in range(l):
        if i > 0:
            d[i] += d[i-1]
    u = random.random() * d[-1]
    for i in range(l):
        if d[i] >= u:
            break
    return i+1,d,u

times = [0]*6
for i in range(100001):
    result,d,u = sampling(dist)
    times[result - 1] += 1

print(times)
print(times[0]/100000,times[1]/100000,times[2]/100000,times[3]/100000,times[4]/100000,times[5]/100000)
#print(d,u)        
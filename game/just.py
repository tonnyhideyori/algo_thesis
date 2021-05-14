import numpy as np
from harmoni import Harmonic
from result import result
snakes = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [
    16, 6], [47, 26], [49, 11], [56, 53], [62, 19], [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
dist = []
countlist=[]
nth = Harmonic(100)
for d in range(1, 101):
    dist.append(1.0/(d*nth.harmonic()))
u=[]
for o in range(0,100):
    u.append(o+1)

def simuharmonic(dice, sl):
    count = 0
    path = []
    token = 0
    while token < 100:
        roll = np.random.choice(range(1,101), size=1, p=dist, replace=False)[0]
        token += roll
        count += 1
        if token > 100:
            token -= roll
            count += 1
        for trans in sl:
            if token == trans[0]:
                token = trans[1]
                break
        path.append(token)
    return [count, path]
for i in range(0,10000):
    countlist.append(simuharmonic(100,snakes))
re = result(countlist)
re.results()
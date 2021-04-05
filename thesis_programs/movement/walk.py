import numpy as np
total = []

def walks():
    stop = "U"
    count = 0
    path = []
    while stop != "B":
        if stop == "U":
            stop = "K"
            count += 1
            path.append(stop)
        if stop == "K":
            stop = np.random.choice(
                ["BS", "S"], size=1, replace=True, p=[0.7, 0.3])[0]
            count += 1
            path.append(stop)
        if stop == "S":
            stop = np.random.choice(
                ["K", "BS"], size=1, replace=True, p=[0.20, 0.8])[0]
            count += 1
            path.append(stop)
        if stop == "BS":
            stop = np.random.choice(
                ["K", "S", "B"], size=1, replace=True, p=[0.05, 0.15, 0.80])[0]
            count += 1
            path.append(stop)
    return [count, path]


for i in range(0, 100000):
    total.append(walks())
sums = 0
#find the average
for ele in total:
    sums += ele[0]
print(f'average walk is {sums/len(total)}')
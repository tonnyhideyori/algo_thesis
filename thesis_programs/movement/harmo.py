#for the demo purpose
import random
dist=[]
for i in range(0,100):
    roll=random.choice(range(1,101),weight=dist,k=1)[0]
    dist.append(roll)
print(dist)
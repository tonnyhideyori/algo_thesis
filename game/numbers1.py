from simulation import game

from snake_ladder import Snakes
from result import result

pecurialsnakes=[[68, 58], [60, 50], [51, 41], [26, 16], [90, 80], [82, 72], [15, 5], [24, 14], [22, 12], [64, 54], [20, 10], [59, 49], [19, 9], [45, 35], [21, 11], [52, 42], [46, 36], [23, 13], [76, 66], [57, 47], [39, 29]]
aveg=[]
for x in range(2,101):
    countlist=[]
    snake=Snakes(0,0)
    sim=game(x,snake.snakes_ladders)
    for i in range(0,100000):
        countlist.append(sim.gamesimulation())
    re = result(countlist)
    print(re.results())
    aveg.append(re.results())
with open("D:\\maths\\thesis\\algo_thesis\\results\simulation2_100.txt","a") as fp:
    for f in aveg:
        fp.write(str(f)+"\n")
        


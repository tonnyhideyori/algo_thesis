from simulation import game

from snake_ladder import Snakes
from result import result
uu=[[4,13],[14,7],[6,3]]
aveg=[]
for x in range(2,3):
    countlist=[]
    snake=Snakes(0,0)
    sim=game(100,snake.snakes_ladders)
    for i in range(0,100000):
        countlist.append(sim.simuharmonic())
    re = result(countlist)
    print(re.results())
    aveg.append(re.results())


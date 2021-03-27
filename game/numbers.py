from snake_ladder import Snakes
from simulation import game
from result import result
countlist=[]
snake=Snakes(0,0)
sim = game(sl=snake.snakes_ladders)
for i in range(0,10000):
    countlist.append(sim.gamesimulation())
re = result(countlist)
re.results()

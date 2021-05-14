import os,sys
dir_path=os.path.dirname("C:\\Users\\edway\\Desktop\\maths\\thesis\\algo_thesis\\game")
sys.path.append(dir_path)
from markov_og import Markov
from game.snake_ladder import Snakes

import ast
lists=[]
avg=[]


uu=[[4,13],[14,7],[6,3]]
for i in range(2,3):
    snake=Snakes(0,0)
    markov=Markov(16,16)
    trans=markov.transition_harmonic()
    sl=markov.snake_ladder(trans,uu)
    result=markov.fundamental_form(trans)
    print(result)
    
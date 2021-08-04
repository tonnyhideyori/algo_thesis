import os,sys
dir_path=os.path.dirname("D:\\maths\\thesis\\algo_thesis\\game")
sys.path.append(dir_path)
from markov_og import Markov
from game.snake_ladder import Snakes

import ast
lists=[]
avg=[]
with open("D:\maths\\thesis\\algo_thesis\\results\list_random_ladders_snakes_fixed5.txt","r") as fil:
    for f in fil:
        x=ast.literal_eval(f.strip())
        lists.append(x)
for l in lists:
    #snake=Snakes(0,0)
    markov=Markov(6,100)
    trans=markov.transition_matrix1()
    sl=markov.snake_ladder(trans,l)
    result=markov.fundamental_form(trans)
    avg.append(result)
with open("D:\maths\\thesis\\algo_thesis\\results\\avg_random_ladders_snakes_fixed5.txt","a") as fp:
    for av in avg:
        fp.write(str(av)+"\n")
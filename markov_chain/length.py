import os,sys
dir_path=os.path.dirname("D:\\maths\\thesis\\algo_thesis\\game")
sys.path.append(dir_path)
from markov_og import Markov
from game.snake_ladder import Snakes

import ast
lists=[]
avg=[]

snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80,100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19], [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
uu=[[16, 6], [47, 26], [49, 11], [56, 53], [62, 19],[64, 60], [87, 24]]
tt=[[1, 38], [4, 14], [9, 31], [21, 42], [28, 84],  [51, 67], [71, 91], [80, 100],[12,39]]
zz=[[3, 44], [67, 68], [12, 42], [72, 91], [20, 27], [6, 22], [4, 32], [59, 81], [39, 65], [16, 96]]
#uu=[[68, 58], [50, 60], [51, 41], [26, 16], [90, 80], [82, 72], [15, 5], [24, 14], [22, 12], [64, 54], [20, 10], [59, 49], [19, 9], [45, 35], [21, 11], [52, 42], [46, 36], [13, 23], [66, 76], [57, 47], [29, 39]]

for i in range(2,3):
    snake=Snakes(0,0)
    markov=Markov(100,100)
    trans=markov.transition_matrix1()
    #sl=markov.snake_ladder(trans,snakes_ladders)
    result=markov.fundamental_form(trans)
    print(result)
    avg.append(result)
"""with open("D:\\maths\\thesis\\algo_thesis\\results\\markov1_100.txt","a") as fp:
    for av in avg:
        fp.write(str(av)+ "\n")"""
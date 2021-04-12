from markov_og import Markov
import ast
lists=[]
avg=[]

with open("C:\\Users\\edway\\Desktop\\maths\\thesis\\algo_thesis\\list_random_ladders_snakes.txt") as fil :
    for f in fil:
        x=ast.literal_eval(f.strip())
        lists.append(x)

for i in range(21000,22000):
    markov=Markov(6,100)
    trans=markov.transition_matrix1()
    sl=markov.snake_ladder(trans,lists[i])
    result=markov.fundamental_form(sl)
    avg.append(result)
    
#print(avg)
print(sum(avg)/len(avg))
for av in avg:
        with open("average_length_s_l_up_all.txt","a") as fp:
            fp.write(str(av)+"\n")
from snake_ladder import Snakes
lists=[]
lists2=[]
for i in range(11,12):
    sl=Snakes(i,i)
    for j in range(0,1000):
        lists.append(sl.random_snakes_ladders(20))
        lists2.append(sl.random_snakes_ladders(30))
fp=open("D:\\maths\\thesis\\algo_thesis\\results\\list_random_ladders_snakes_fixed20.txt","a")
for x in lists:
    fp.write(str(x)+"\n")
fp.close()
ff=open("D:\\maths\\thesis\\algo_thesis\\results\\list_random_ladders_snakes_fixed30.txt","a")
for x in lists2:
    ff.write(str(x)+"\n")
ff.close()

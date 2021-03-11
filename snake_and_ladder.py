# @author : Edwin Ismail
import random
import pickle
import more_itertools
from numba import njit
from numba.typed import List
# initializing size of the dance
dice = 6

#randomizing original snakes and ladders


def originalRandom():
    ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [
        28, 84], [36, 44], [51, 67], [71, 91], [80, 100]]
    snakes = [[16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
            [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
    ele1 = []
    ele2 = []
    ele3 = []
    ele4 = []
    for x in ladders:
        ele1.append(x[0])
        ele2.append(x[1])
    for x in snakes:
        ele3.append(x[0])
        ele4.append(x[1])
    random.shuffle(ele1)
    random.shuffle(ele2)
    random.shuffle(ele3)
    random.shuffle(ele4)
    la = list(more_itertools.zip_equal(ele1, ele2))
    sn = list(more_itertools.zip_equal(ele3, ele4))
    sl = [list(x) for x in la]
    sn = [list(x) for x in sn]
    for ele in sn:
        if ele[0] < ele[1]:
            ele[0], ele[1] = ele[1], ele[0]
    for ele in sl:
        if ele[0] > ele[1]:
            ele[0], ele[1] = ele[1], ele[0]
    return sn+sl

# snakes and ladders for the game for a snake element[0]<element[1] and for a ladder element[0]<element[1]
snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
                  [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]

# random snakes generator



def randomSnakes(num):
    randomSnake = []
    countSnake = 0
    s_l_set = set()
    s_l_set.update([])
    while len(randomSnake) < (num):
        x = random.randint(1, 99)
        y = random.randint(1, 99)
        if y > x and countSnake < (num):
            if not y in s_l_set and not x in s_l_set:
                randomSnake.append([y, x])
                countSnake += 1
        for ele in randomSnake:
            s_l_set.update(ele)
    return randomSnake

# random ladders generator



def randomLadders(num):
    randomLadder = []
    countLadder = 0
    s_l_set = set()
    s_l_set.update([])
    while len(randomLadder) < (num):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        if y < x and countLadder < (num):
            if not y in s_l_set and not x in s_l_set:
                randomLadder.append([y, x])
                countLadder += 1
        for ele in randomLadder:
            s_l_set.update(ele)
    return randomLadder
#random snakes nad ladders generator for equal size i.e 5 


def RandomSnake1(numSnake, numLadder):
    randomSnake = []
    countSnake = 0
    countLadder = 0
    s_l_set = set()
    s_l_set.update([])
    while len(randomSnake) < (numSnake+numLadder):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        if y > x and countSnake < (numSnake) and (y-x) < 7 and y != 100:
            if not y in s_l_set and not x in s_l_set:
                randomSnake.append([y, x])
                countSnake += 1
        if y < x and countLadder < (numLadder) and (x-y) > 7:
            if not y in s_l_set and not x in s_l_set:
                randomSnake.append([y, x])
                countLadder += 1
        for ele in randomSnake:
            s_l_set.update(ele)
    # just verifying if snakes and ladders are unique
    """df=pd.DataFrame(list(s_l_set),columns=['just'])
    print(df['just'].value_counts())"""
    return randomSnake

# random snake and ladder generator


def RandomSnake(numSnake, numLadder):
    randomSnake = []
    countSnake = 0
    countLadder = 0
    s_l_set = set()
    s_l_set.update([])
    while len(randomSnake) < (numSnake+numLadder) :
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        if y > x and countSnake < (numSnake) and y != 100:
            if not y in s_l_set and  not x in s_l_set:
                randomSnake.append([y, x])
                countSnake += 1
        if y < x and countLadder < (numLadder):
            if not y in s_l_set and not x in s_l_set:
                randomSnake.append([y, x])
                countLadder += 1
        for ele in randomSnake:
            s_l_set.update(ele)
    # just verifying if snakes and ladders are unique
    """df=pd.DataFrame(list(s_l_set),columns=['just'])
    print(df['just'].value_counts())"""
    return randomSnake



# this is the simulation of the game snakes and ladders

def gamesimulation(sl, dice):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
    count = 0
    path = []
    token = 0
    while token < 100:
        roll = random.randint(1, dice)
        token = token + roll
        count += 1
        #contorls token should land exactly at 100
        if token > 100:
            token = token - roll
        for trans in sl:
            if token == trans[0]:
                token = trans[1]
                break
        path.append(token)
    return [count, path]

# this function command how many times the game should be played


def NumberOfGame(number):
    countlist = []
    for num in range(0, number):
        countlist.append(gamesimulation(
            originalRandom(),dice))
    return countlist

# this function is to present the result of the game


def results(countlist):
    # print((min(countlist))[1])
    """print("The minimum lenght of the game is {} \n the shortest path is {}".format(
        (min(countlist))[0], (min(countlist))[1]))
    print("The maximum lenght of the game is {} \n the longest path is {}".format(
        (max(countlist))[0], (max(countlist))[1]))
    sums = 0
    for ele in countlist:
        sums += ele[0]
    print("Average length of the game is {}".format(sums/len(countlist)))"""
    return countlist
#minimumlength
def MiniLength(countlist):
   return (min(countlist))[1]
for i in range(0,10):
    countlist=results(NumberOfGame(100000))
    with open('game_random_snake_og_se', 'wb') as fp:
        pickle.dump(countlist, fp)
"""listmin=[]
for i in range(0,100):
    listmin.append(MiniLength(NumberOfGame(1000)))
#print(listmin)"""


def gamesimulation2(sl, dice):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
    count = 0
    path = []
    token = 0
    while token < 100:
        roll = random.randint(1, dice)
        token = token + roll
        count += 1
        #contorls token should land exactly at 100
        if token > 100:
            token = token - roll
        for trans in sl:
            if token == trans[0]:
                token = trans[1]
                break
        path.append(token)
    return [count, path,sl]


listmin = []
for i in range(0, 1000):
    listmin.append(NumberOfGame(100))
#print(listmin)
#saving files to byte for later analysis
with open('avg_random_og', 'wb') as fp:
    pickle.dump(listmin, fp)


"""with open('minimumlength', 'rb') as fp:
    itemlist = pickle.load(fp)
print(itemlist)"""

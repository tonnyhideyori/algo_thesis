# @author : Edwin Ismail
import random
# initializing size of the dance
dice = 6
countlist = []


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
    for num in range(0, number):
        countlist.append(gamesimulation(
            snakes_ladders,dice))
    return countlist

# this function is to present the result of the game


def results(countlist):
    # print((min(countlist))[1])
    print("The minimum lenght of the game is {} \n the shortest path is {}".format(
        (min(countlist))[0], (min(countlist))[1]))
    print("The maximum lenght of the game is {} \n the longest path is {}".format(
        (max(countlist))[0], (max(countlist))[1]))
    sums = 0
    for ele in countlist:
        sums += ele[0]
    print("Average length of the game is {}".format(sums/len(countlist)))


results(NumberOfGame(1000000))

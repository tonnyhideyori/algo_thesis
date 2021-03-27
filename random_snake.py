import random
import pickle
import more_itertools
import json
dice=6
def RandomSnake(numSnake, numLadder):
    randomSnake = []
    countSnake = 0
    countLadder = 0
    s_l_set = set()
    s_l_set.update([])
    while len(randomSnake) < (numSnake+numLadder):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        if y > x and countSnake < (numSnake) and y != 100:
            if not y in s_l_set and not x in s_l_set:
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


def gamesimulation2(sl, dice):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
    count = 0
    path = []
    token = 0
    while token < 100:
        roll = random.randint(1, dice)
        token = token + roll
        count += 1
        # contorls token should land exactly at 100
        if token > 100:
            token = token - roll
        for trans in sl:
            if token == trans[0]:
                token = trans[1]
                break
        path.append(token)
    return [count, path, sl]


def NumberOfGame2(number):
    countlist = []
    for num in range(0, number):
        x = RandomSnake(10, 9)
        countlist.append(gamesimulation2(
            x, dice))
    return countlist



for u in range(0,10):
    print(u)
    lists = []
    for i in range(0, 20):
        print(i)
        x = NumberOfGame2(100)
        lists.append(x)
    with open('random_snake_new.txt', 'a') as fp:
        for s in lists:
            fp.write(str(s)+"\n")

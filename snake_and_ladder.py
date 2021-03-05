#@author : Edwin Ismail
import random
# initializing size of the dance
dice = 6
countlist = []

# snakes and ladders for the game for a snake element[0]<element[1] and for a ladder element[0]<element[1]
snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
                  [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]

# this is the simulation of the game snakes and ladders
def gamesimulation(sl, dice):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
    count = 0
    path = []
    token = 0
    while token < 100:
        roll = random.randint(1, dice)
        token = token+roll
        count += 1
        if token > 100:
            token = token-roll
        for trans in sl:
            if token == trans[0]:
                token = trans[1]
                break
        path.append(token)
    return [count, path]

# this function command how many times the game should be played
def NumberOfGame(number):
    for num in range(0, number):
        countlist.append(gamesimulation(snakes_ladders, dice))
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


results(NumberOfGame(1000))

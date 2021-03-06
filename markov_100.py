"""
@author Edwin Ismail
This is a demo for snakes and ladder which has one snake and one ladder.
you can vary the size of the dice and size of the board
"""

import numpy as np
import random
board = 100
state = board+1
result = []
# M = np.zeros((state, state), dtype=float)
# list of snakes and ladder
ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [
    28, 84], [36, 44], [51, 67], [71, 91], [80, 100]]
snakes = [[16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
          [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
                  [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]

# random randomLadders


def randomLadders(num):
    randomLadder = []
    countLadder = 0
    s_l_set = set()
    s_l_set.update([])
    while len(randomLadder) < (num):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        if y < x and countLadder < (num):
            if not y in s_l_set:
                randomLadder.append([y, x])
                countLadder += 1
        for ele in randomLadder:
            s_l_set.update(ele)
    return randomLadder

# random snakes only


def randomSnakes(num):
    randomSnake = []
    countSnake = 0
    s_l_set = set()
    s_l_set.update([])
    while len(randomSnake) < (num):

        x = random.randint(1, 99)
        y = random.randint(1, 99)
        if y > x and countSnake < (num):
            if not y in s_l_set:
                randomSnake.append([y, x])
                countSnake += 1
        for ele in randomSnake:
            s_l_set.update(ele)
    return randomSnake

# random snake and ladder generator


def RandomSnake(numSnake, numLadder):
    countSnake = 0
    countLadder = 0
    randomSnake = []
    s_l_set = set()
    s_l_set.update([])
    while len(randomSnake) < (numSnake+numLadder):

        x = random.randint(0, 99)
        y = random.randint(0, 99)
        if y > x and countSnake < (numSnake):
            if not y in s_l_set:
                randomSnake.append([y, x])
                countSnake += 1
        if y < x and countLadder < (numLadder):
            if not y in s_l_set:
                randomSnake.append([y, x])
                countLadder += 1
        for ele in randomSnake:
            s_l_set.update(ele)
    # just verifying if snakes and ladders are unique
    """df=pd.DataFrame(list(s_l_set),columns=['just'])
    print(df['just'].value_counts())"""
    return randomSnake
# no snake or ladder transition matrix


def transition_matrix1(dice, board, state):
    M = np.zeros((state, state), dtype=float)
    for i in range(0, state):
        for j in range(1, state):
            if j <= dice and i <= board-dice:
                M[i, j+i] = 1/dice
            if i >= board-dice:
                M[i, i] = ((dice-board)+i)/dice
                if j+i < len(M):
                    M[i, j+i] = 1/dice
    return M
# transition matrix with  snake and ladder ####ladders=0,


def snake_ladder(M, snakes, state):
    for i in range(0, state):
        for snake in snakes:
            if i < snake[0]:
                M[i, snake[1]] = M[i, snake[1]] + M[i, snake[0]]
            M[snake[0], i] = 0
            M[i, snake[0]] = 0
        """for ladder in ladders:
            if i < ladder[0]:
                M[i, ladder[1]] = M[i, ladder[1]] + M[i, ladder[0]]
            M[ladder[0], i] = 0
            M[i, ladder[0]] = 0"""
    return M


# calculating length of the game based on fundamental form
def fundamental_form(M):
    Q = M[:-1, :-1]
    N = np.linalg.inv(np.identity(len(Q))-Q)
    length = np.matmul(N, np.ones((len(N), 1)))
    return length[0][0]


# list all length of the game for different size of the dice


def expectationdice():
    for dice in range(2, 101, 1):
        result.append(fundamental_form(snake_ladder(
            transition_matrix1(dice, board, state), snakes_ladders, state)))
    print(result, sum(result)/len(result), min(result), max(result))

# function which find expectation where dice change and snakes and ladders are randomized with dice
def expectation100dice():
    for dice in range(2, 101, 1):
        result.append(fundamental_form(snake_ladder(
            transition_matrix1(dice, board, state), RandomSnake(10, 9), state)))
    print(result, sum(result)/len(result), min(result), max(result))

# function for calcualating expected length for randomized snakes and ladders with dice fixed at 6
def expectation100():
    for dice in range(0, 100):
        result.append(fundamental_form(snake_ladder(
            transition_matrix1(6, board, state), RandomSnake(10, 9), state)))
    print(result, sum(result)/len(result), min(result), max(result))

# function which find expected length of the game when varying the dice but randomize snake and ladder once
def expectationOnce():
    s_n_l = RandomSnake(10, 9)
    print(s_n_l)
    for dice in range(2, 101,1):
        result.append(fundamental_form(snake_ladder(
                transition_matrix1(dice, board, state), s_n_l, state)))
    print(result, sum(result)/len(result), min(result), max(result))


# RandomSnake(10, 9, randomSnake)
#expectationOnce()
expectation100dice()

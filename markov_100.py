"""
@author Edwin Ismail
This is a demo for snakes and ladder which has one snake and one ladder.
you can vary the size of the dice and size of the board
"""

import numpy as np
board =100 
state = board+1
result=[]
#M = np.zeros((state, state), dtype=float)
#list of snakes and ladder
ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [
    28, 84], [36, 44], [51, 67], [71, 91], [80, 100]]
snakes = [[16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
          [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]

#no snake or ladder transition matrix


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
#transition matrix with  snake and ladder


def snake_ladder(M,snakes, ladders, state):
    for i in range(0, state):
        for snake in snakes:
            if i < snake[0]:
                M[i, snake[1]] = M[i, snake[1]] + M[i, snake[0]]
            M[snake[0], i] = 0
            M[i, snake[0]] = 0
        for ladder in ladders:
            if i < ladder[0]:
                M[i, ladder[1]] = M[i, ladder[1]] + M[i, ladder[0]]
            M[ladder[0], i] = 0
            M[i, ladder[0]] = 0
    return M


#calculating length of the game based on fundamental form
def fundamental_form(M):
    Q = M[:-1, :-1]
    N = np.linalg.inv(np.identity(len(Q))-Q)
    length = np.matmul(N, np.ones((len(N), 1)))
    return length[0][0]

#list all length of the game for different size of the dice
for dice in range(2,101,1): 
    result.append(fundamental_form(snake_ladder(
    transition_matrix1(dice, board, state), snakes, ladders, state)))
print(result)
"""
@author Edwin Ismail
This is a demo for snakes and ladder which has one snake and one ladder.
you can vary the size of the dice and size of the board
"""

import numpy as np
print("please enter size of the dice")
dice = int(input())
print("please enter size of the board")
board = int(input())
state = board+1
M = np.zeros((state, state), dtype=float)
#list of snakes and ladder
ladders = [[2,6]]
snakes = [[8,3]]

#no snake or ladder transition matrix
def transition_matrix1(dice,board,state):
    for i in range(0, state):
        for j in range(1, state):
            if j<=dice and i<=board-dice:
                M[i, j+i] = 1/dice
            if i>= board-dice:
                M[i,i]=((dice-board)+i)/dice
                if j+i<len(M):
                    M[i,j+i]=1/dice
#transition matrix with  snake and ladder        
def snake_ladder(snakes,ladders,state):
    for i in range(0,state):
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
#calculating length of the game based on fundamental form
def fundamental_form(M):
    Q=M[:-1,:-1]
    N=np.linalg.inv(np.identity(len(Q))-Q)
    length=np.matmul(N,np.ones((len(N),1)))
    return length[0][0]
transition_matrix1(dice,board,state)
snake_ladder(snakes,ladders,state)
print("the average length of the game with {} sqaure board and die size of {} is  {}".format(board,dice,fundamental_form(M)))


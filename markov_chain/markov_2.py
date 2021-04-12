import numpy as np
board = 100
dice=6
state = board+1+(2*dice)


snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
                  [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]

def transition_matrix1(dice, board, state):
    M = np.zeros((state, state), dtype=float)
    for i in range(0, state):
        for j in range(1, state):
            if j <= (2*dice) and i <= board-(2*dice):
                M[i, j+i] = (dice - abs(j-(dice+1)))/(dice*dice)
            if i >= board-(2*dice):
                if i < board and (state-j)<=(2*dice):
                    M[i, state-j+i] = (dice - abs((state-j)-(dice+1)))/(dice*dice)
            """if i >= board-(2*dice) :
                #M[i, i] = ((dice-board)+i)/dice
                if i < board  and state-j<=2*dice:
                    M[i, state-j+i] = (dice - abs(j-(dice+1)))/(dice*dice)"""
            if i>=board:
                M[i,i]=1
    return M
# transition matrix with  snake and ladder ####ladders=0,


def snake_ladder(M, snakes, state):
    for i in range(0, state):
        for snake in snakes:
            if i < snake[0]:
                M[i, snake[1]] = M[i, snake[1]] + M[i, snake[0]]
            M[snake[0], i] = 0
            M[i, snake[0]] = 0
    return M


# calculating length of the game based on fundamental form
def fundamental_form(M):
    Q = M[:-((2*dice)+1), :-((2*dice)+1)]
    N = np.linalg.inv(np.identity(len(Q))-Q)
    length = np.matmul(N, np.ones((len(N), 1)))
    return length[0][0]
def expectation():
    print(fundamental_form(snake_ladder(
            transition_matrix1(dice, board, state), snakes_ladders, state)))

expectation()
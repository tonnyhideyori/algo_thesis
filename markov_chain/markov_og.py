import numpy as np
class Markov(object):
    snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51,67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19],[64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
    def __init__(self,dice,board):
        self.dice=dice
        self.board=board
        self.state=board+1
    
    def transition_matrix1(self):
        M = np.zeros((self.state, self.state), dtype=float)
        for i in range(0, self.state):
            for j in range(1, self.state):
                if j <= (self.dice) and i <= (self.board-self.dice):
                    M[i, j+i] = 1/self.dice
                if i >= self.board-self.dice:
                    M[i, i] = ((self.dice-self.board)+i)/self.dice
                    if j+i < len(M):
                        M[i, j+i] = 1/self.dice
        return M
    def snake_ladder(self,M, snakes):
        for i in range(0, self.state):
            for snake in snakes:
                if i < snake[0]:
                    M[i, snake[1]] = M[i, snake[1]] + M[i, snake[0]]
                M[snake[0], i] = 0
                M[i, snake[0]] = 0
        return M
    def fundamental_form(self,M):
        Q = M[:-1, :-1]
        N = np.linalg.inv(np.identity(len(Q))-Q)
        length = np.matmul(N, np.ones((len(N), 1)))
        return length[0][0]
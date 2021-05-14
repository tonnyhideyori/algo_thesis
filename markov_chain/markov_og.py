import os,sys
dir_path=os.path.dirname("C:\\Users\\edway\\Desktop\\maths\\thesis\\algo_thesis\\game")
sys.path.append(dir_path)
import numpy as np
from game.harmoni import Harmonic

class Markov(object):
    snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [
        16, 6], [47, 26], [49, 11], [56, 53], [62, 19], [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]

    def __init__(self, dice, board):
        self.dice = dice
        self.board = board
        self.state = board+1
        self.dist=[]
        nth=Harmonic(self.dice)
        
        for d in range(1,self.dice+1):
            self.dist.append(1/(d*nth.harmonic()))
        #print(self.dist[0])
        #print(sum(self.dist))
        if sum(self.dist)>1:
            #print(1-sum(self.dist))
            self.dist[len(self.dist)-1]=self.dist[len(self.dist)-1]+(1-sum(self.dist))
            if sum(self.dist)<1:
               self.dist[len(self.dist)-1]=self.dist[len(self.dist)-1]+(1-sum(self.dist)) 
        else:
            self.dist[len(self.dist)-1]=self.dist[len(self.dist)-1]+(1-sum(self.dist))
        #print(sum(self.dist))
    def bmatrix(self, a):
        """Returns a LaTeX bmatrix

        :a: numpy array
        :returns: LaTeX bmatrix as a string
        """
        if len(a.shape) > 2:
            raise ValueError('bmatrix can at most display two dimensions')
        lines = str(a).replace('[', '').replace(']', '').splitlines()
        rv = [r'\left(\begin{array}{*{17}c}']
        rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
        rv += [r'\end{array}\right)']
        return '\n'.join(rv)
    
    def transition_matrix2(self):
        self.state=self.state + self.dice - 1
        M = np.zeros((self.state, self.state), dtype=float)
        for i in range(0, self.state):
            for j in range(1, self.state):
                if j <= self.dice and i <= (self.board - self.dice):
                    M[i, j+i] = 1/self.dice
                if i >= (self.board-self.dice):
                    if i < self.board  and (self.state-j)<=self.dice:
                        M[i, self.state-j+i] = 1/self.dice
                if i>=self.board:
                    M[i,i]=1
        return M
    
    #more tha one dice
    def transition_matrix3(self):
        acc=0
        Tdice=2*self.dice
        M=np.zeros((self.state,self.state),dtype=float)
        for i in range(0,self.state):
            for j in range(1,self.state):
                if j <= (Tdice) and i <= (self.board):
                    if j+i <= len(M):
                        M[i,i+j-1]=(self.dice - abs(j-(self.dice+1)))/(self.dice*self.dice)
                """if i > self.board-Tdice and i<=self.board:
                    if j+i <= len(M):
                        M[i, j+i-1]=(self.dice - abs(j-(self.dice+1)))/(self.dice*self.dice)"""
        for i in range(0,self.state):
            for j in range(1,self.state):
                acc += M[i,j]
            M[i,i]=1-acc
            acc=0
        return M
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
    def transition_harmonic(self):
        acc=0
        M = np.zeros((self.state, self.state), dtype=float)
        for i in range(0, self.state):
            for j in range(1, self.state):
                if j <= (self.dice) and i <= (self.board-self.dice):
                    M[i, j+i] = self.dist[j-1]
                if i>self.board - self.dice:
                    if j+i<=self.board:
                        M[i,j+i]=self.dist[j-1]
        for i in range(0,self.state):
            for j in range(1,self.state):
                acc += M[i,j]
            M[i,i]=1-acc
            acc=0
        return M
                
    def snake_ladder(self, Y, snakes):
        for i in range(0, self.state):
            for j in range(0, self.state):
                for snake in snakes:
                    if j == snake[0]:
                        x = Y[i, snake[0]]
                        Y[snake[0]] = 0
                        Y[i, snake[1]] = Y[i, snake[1]] + x
                        Y[i, snake[0]] = 0

        return Y
    
    def fundamental_form(self, M):
        Q = M[:-1, :-1]
        N = np.linalg.inv(np.identity(len(Q)) - Q)
        length = np.matmul(N, np.ones((len(N), 1)))
        # print(self.bmatrix(length))
        return length[0][0]

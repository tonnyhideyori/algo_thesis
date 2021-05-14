import numpy as np
board = 9
dice=2
state = board+(2*dice)


snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
                  [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
def bmatrix(a):
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

def transition_matrix1(dice, board, state):
    M = np.zeros((state, state), dtype=float)
    for i in range(0, state):
        for j in range(2, state):
            if j <= (2*dice) and i <= board-(2*dice):  
                M[i, j+i] = (dice - abs(j-(dice+1)))/(dice*dice)
            if i >= board-(2*dice):
                if i < board and (state-j)<=(2*dice):
                    M[i, state-j+i] = (dice - abs((state-j)-(dice+1)))/(dice*dice)
            """if i >= board-(2*dice) :
                #M[i, i] = ((dice-board)+i)/dice
                if i < board  and state-j<=2*dice:
                    M[i, state-j+i] = (dice - abs(j-(dice+1)))/(dice*dice)"""
            if i%2 !=0:
                M[i]=0
            if i>=board:
                M[i,i]=1
    return M
# transition matrix with  snake and ladder ####ladders=0,


def snake_ladder(self,M, snakes):
        for i in range(0, self.state):
            for j in range(0,self.state):
                for snake in snakes:
                    if j == snake[0]:
                        x=M[i, snake[0]]
                        M[snake[0]]=0
                        M[i, snake[1]] = M[i, snake[1]] + x
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
print(bmatrix(transition_matrix1(dice, board, state)))
#expectation()
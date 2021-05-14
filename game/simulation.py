import random
from harmoni import Harmonic
class game(object):
    
    def __init__(self,dice=6,sl=None):
        self.dice =dice
        self.sl = sl
        self.dist=[]
        self.our=[]
        nth=Harmonic(self.dice)
        for d in range(1,self.dice+1):
            self.dist.append(1/(d*nth.harmonic()))
        if sum(self.dist)>1:
            self.dist[len(self.dist)-1]=self.dist[len(self.dist)-1]+(1-sum(self.dist))
            if sum(self.dist)<1:
               self.dist[len(self.dist)-1]=self.dist[len(self.dist)-1]+(1-sum(self.dist)) 
        else:
            self.dist[len(self.dist)-1]=self.dist[len(self.dist)-1]+(1-sum(self.dist))

    def gamesimulation(self):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
        count = 0
        path = []
        token = 0
        while token < 100:
            roll = random.randint(1, self.dice)
            token = token + roll
            count += 1
            # contorls token should land exactly at 100
            if token > 100:
                token = token - roll
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path]

    def gamesimulation2(self):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
        count = 0
        path = []
        token = 0
        while token < 100:
            roll = random.randint(1, self.dice)
            token = token + roll
            count += 1
            # contorls token should land exactly at 100
            if token > 100:
                token = token - roll
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path, self.sl]

    def gamesimulation3(self):
        # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
            count = 0
            path = []
            token = 0
            while token < 100:
                roll = random.randint(1, self.dice)
                token = token + roll
                count += 1
                for trans in self.sl:
                    if token == trans[0]:
                        token = trans[1]
                        break
                path.append(token)
            return [count, path]
    def gamesimulation4(self):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
        count = 0
        path = []
        token = 0
        while token < 100:
            roll = random.randint(1, self.dice)
            roll2=random.randint(1,self.dice)
            #roll3=random.randint(1,self.dice)
            token = token + roll + roll2 
            count += 1
            # contorls token should land exactly at 100
            if token > 100:
                token = token - (roll + roll2)  
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path]
    def gamesimulation5(self):
    # initialization of parameters count for counting the length of game, path records the step of the game to completion, token is actual element moving through the game
        count = 0
        path = []
        token = 0
        while token < 100:
            roll = random.randint(1, self.dice)
            roll2=random.randint(1,self.dice)
            #roll3=random.randint(1,self.dice)
            token = token + roll + roll2 
            count += 1
            # contorls token should land exactly at 101 or 100
            if token > 101:
                token = token - (roll + roll2)
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path]
    def demo(self):
        count = 0
        path = []
        token = 0
        while token < 16:
            roll = random.randint(1, self.dice)
            token = token + roll
            count += 1
            if token > 16:
                token = token - roll
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path]
    def demo2(self,i):
        count = 0
        path = []
        token = i
        while token < 16:
            roll = random.randint(1, self.dice)
            token = token + roll
            count += 1
            """if token > 16:
                token = token - roll"""
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path]
    
    def demo3(self):
        count = 0
        path = []
        token = 0
        while token < 16:
            roll = random.randint(1, self.dice)
            roll2=random.randint(1,self.dice) -1
            token = token + roll + roll2
            count += 1
            if token > 16:
                token = token - roll - roll2
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path]
    
    def simuharmonic(self):
        count = 0
        path = []
        token = 0
        while token < 100:
            roll=random.choices(population=range(1,self.dice+1),k=1,weights=self.dist)[0]
            token+=roll
            count+=1
            if token>100:
                token-=roll
                count+=1
            for trans in self.sl:
                if token == trans[0]:
                    token = trans[1]
                    break
            path.append(token)
        return [count, path]
    
    def demoharmonic(self):
        count = 0
        path = []
        token = 0
        while token < 16:
            roll=random.choices(population=range(1,self.dice+1),k=1,weights=self.dist)[0]
            #roll=random.choices(population=self.our,k=1,weights=self.dist)[0]
            token=token+roll
            count+=1
            if token > 16:
                token=token - roll
                count+=1
            try:
                for trans in self.sl:
                    if token == trans[0]:
                        token = trans[1]
                        break
            except TypeError:
                pass
            path.append(token)
        return [count, path]
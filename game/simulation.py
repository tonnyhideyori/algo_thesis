import random
class game(object):
    def __init__(self,dice=6,sl=None):
        self.dice =dice
        self.sl = sl

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
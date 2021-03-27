import random
import more_itertools
class Snakes(object):
    #original snake and ladder set
    snakes_ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19],[64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
    def __init__(self,numbersnake=0,numberladder=0):
        self.numbersnake = numbersnake
        self.numberladder = numberladder
    def randomsnake(self):
        randomSnake = []
        countSnake = 0
        s_l_set = set()
        s_l_set.update([])
        while len(randomSnake) < (self.numbersnake):
            x = random.randint(1, 99)
            y = random.randint(1, 99)
            if y > x and countSnake < (self.numbersnake):
                if not y in s_l_set and not x in s_l_set:
                    randomSnake.append([y, x])
                    countSnake += 1
            for ele in randomSnake:
                s_l_set.update(ele)
        return randomSnake

    def randomladders(self):
        randomLadder = []
        countLadder = 0
        s_l_set = set()
        s_l_set.update([])
        while len(randomLadder) < (self.numberladder):
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if y < x and countLadder < (self.numberladder):
                if not y in s_l_set and not x in s_l_set:
                    randomLadder.append([y, x])
                    countLadder += 1
            for ele in randomLadder:
                s_l_set.update(ele)
        return randomLadder
#random snake generator which choose the length og the snake and ladder
    def RandomSnake1(self,length):
        randomSnake = []
        countSnake = 0
        countLadder = 0
        s_l_set = set()
        s_l_set.update([])
        while len(randomSnake) < (self.numbersnake+self.numberladder):
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if y > x and countSnake < (self.numbersnake) and (y-x) < length and y != 100:
                if not y in s_l_set and not x in s_l_set:
                    randomSnake.append([y, x])
                    countSnake += 1
            if y < x and countLadder < (self.numberladder) and (x-y) > length:
                if not y in s_l_set and not x in s_l_set:
                    randomSnake.append([y, x])
                    countLadder += 1
            for ele in randomSnake:
                s_l_set.update(ele)
        return randomSnake

    def random_snakes_ladders(self):
        randomSnake = []
        countSnake = 0
        countLadder = 0
        s_l_set = set()
        s_l_set.update([])
        while len(randomSnake) < (self.numbersnake+self.numberladder):
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if y > x and countSnake < (self.numbersnake) and y != 100:
                if not y in s_l_set and not x in s_l_set:
                    randomSnake.append([y, x])
                    countSnake += 1
            if y < x and countLadder < (self.numberladder):
                if not y in s_l_set and not x in s_l_set:
                    randomSnake.append([y, x])
                    countLadder += 1
            for ele in randomSnake:
                s_l_set.update(ele)
        return randomSnake

    def originalRandom(self):
        ladders = [[1, 38], [4, 14], [9, 31], [21, 42], [
            28, 84], [36, 44], [51, 67], [71, 91], [80, 100]]
        snakes = [[16, 6], [47, 26], [49, 11], [56, 53], [62, 19],
                [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
        ele1 = []
        ele2 = []
        ele3 = []
        ele4 = []
        for x in ladders:
            ele1.append(x[0])
            ele2.append(x[1])
        for x in snakes:
            ele3.append(x[0])
            ele4.append(x[1])
        random.shuffle(ele1)
        random.shuffle(ele2)
        random.shuffle(ele3)
        random.shuffle(ele4)
        la = list(more_itertools.zip_equal(ele1, ele2))
        sn = list(more_itertools.zip_equal(ele3, ele4))
        sl = [list(x) for x in la]
        sn = [list(x) for x in sn]
        for ele in sn:
            if ele[0] < ele[1]:
                ele[0], ele[1] = ele[1], ele[0]
        for ele in sl:
            if ele[0] > ele[1]:
                ele[0], ele[1] = ele[1], ele[0]
        return sn+sl

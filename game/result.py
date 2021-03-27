class result(object):
    def __init__(self,countlist):
        self.countlist = countlist
    def results(self):
        # print((min(countlist))[1])
        print("The minimum lenght of the game is {} \n the shortest path is {}".format(
            (min(self.countlist))[0], (min(self.countlist))[1]))
        print("The maximum lenght of the game is {} \n the longest path is {}".format(
            (max(self.countlist))[0], (max(self.countlist))[1]))
        sums = 0
        for ele in self.countlist:
            sums += ele[0]
        print("Average length of the game is {}".format(sums/len(self.countlist)))

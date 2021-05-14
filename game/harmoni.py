#harmonic number algorithm
class Harmonic(object):
    def __init__(self,term=1):
        self.term = term
    
    def harmonic(self):
        h=1
        for i in range(2,self.term+1):
            h+=1/i
        return h

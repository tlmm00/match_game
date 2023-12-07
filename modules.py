class Player:
    def __init__(self):
        self.score=0
    
    def getScore(self):
        return self.score
    
    def addScore(self):
        self.score+=1
    
    def setScoreZero(self):
        self.score = 0


class Card:
    def __init__(self, value):
        self.width = 50
        self.height = 50
        self.value = value
        # self.x = x
        # self.y = y

    def getValue(self):
        return self.value

    # def getPos(self):
    #     return [self.x, self.y]

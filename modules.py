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
    def __init__(self, value, x, y):
        self.width = 50
        self.height = 50
        self.value = value
        self.show = False
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        
    def restore(self):
        self.show = False
        self.color = (255,0,0)

    def isShow(self):
        return self.show

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def onClick(self):
        self.color = (255, 150, 150)
        self.show = True

    def getPoints(self):
        maxX = self.x + self.width
        maxY = self.y + self.height

        return [self.x, self.y, maxX, maxY]

from modules import *
import pygame

class Game:
    def __init__(self):
        
        self.width = 750
        self.height = 750

        self.running = True
        self.display = None

        self.gameOver = False
        
        self.p1 = None
        self.p2 = None

        self.cards = []

    def onInit(self):
        self.display=pygame.display.set_mode((self.width, self.height))
        self.running = True

        self.p1 = Player()
        self.p2 = Player()

        for i in range(14):
            if i<7:
                new_card = Card(i) 
            else:
                new_card = Card(i-7)

            self.cards.append(new_card)

        pygame.init()
    
    def onCleanUp(self):
        pygame.quit()

    def onEvent(self, event):
        if event == pygame.QUIT:
            self.running = False
    
    def onRender(self):
        dx1 = 0
        dx2 = 0
        for card in self.cards:
            # print(card.getValue())
            if card.getValue()%2 == 0:
                pygame.draw.rect(self.display, (255,0,0), pygame.Rect(30+dx1, 30, 50, 50))
                dx1+=75

            else:
                pygame.draw.rect(self.display, (255,0,0), pygame.Rect(30+dx2, 130, 50, 50))
                dx2+=75
            
                
        
    
    
    
        pygame.display.flip()
            

    def onLoop(self):
        pass

    def onExecute(self): 
        if self.onInit() == False:
            self.running = False

        while (self.running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.onLoop()
            self.onRender()
        self.onCleanup()



if __name__ == "__main__":
    game = Game()
    game.onExecute()
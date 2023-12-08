from modules import *
import pygame
import time
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.width = 560
        self.height = 600

        self.running = True
        self.display = pygame.display.set_mode((self.width, self.height))

        self.isOver = False
        
        # jogadores
        self.p1 = Player()
        self.p2 = Player()

        self.activePlayer = self.p1
        self.turn = 1

        self.cards = []

        # cartas selecionadas
        self.c1 = None
        self.c2 = None

        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def changeTurn(self):
        if self.turn == 1:
            self.activePlayer = self.p2
            self.turn = 2
        
        elif self.turn == 2:
            self.activePlayer = self.p1
            self.turn = 1

    def onInit(self):

        self.running = True
        self.cards = []

        value_dict = {0: ["A", 0], 1: ["B", 0], 2: ["C", 0], 3: ["D", 0], 4: ["E", 0], 5: ["1", 0], 6: ["2", 0], 7: ["3", 0], 8: ["4", 0], 9: ["5", 0], 10: ["6", 0], 11: ["7", 0], 12: ["8", 0], 13: ["9", 0]}
        dx1=0
        dx2=0
        dx3=0
        dx4=0

        for i in range(len(value_dict)*2):

            v = random.randint(0, len(value_dict) - 1)
            
            while value_dict[v][1] >= 2:
                v = random.randint(0, len(value_dict) - 1)            

            if i < len(value_dict)/2:
                new_card = Card(value_dict[v][0], 30+dx1, 30)
                dx1+=75
            elif i < len(value_dict):
                new_card = Card(value_dict[v][0], 30+dx2, 110)
                dx2+=75
            elif i < 1.5*len(value_dict):
                new_card = Card(value_dict[v][0], 30+dx3, 190)
                dx3+=75
            else:
                new_card = Card(value_dict[v][0], 30+dx4, 270)
                dx4+=75

            value_dict[v][1] += 1
            self.cards.append(new_card)

    
    def onCleanUp(self):
        pygame.quit()

    def onEvent(self, event):
        # print(event)
        if event == pygame.QUIT:
            self.running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                if self.isOver:
                    x,y = event.pos
                    if (x>2*self.width/5-35 and x<2*self.width/5+165 and y>self.height/2 and y<self.height/2 + 20):
                        pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(2*self.width/5-35, self.height/2, 200, 30))
                        self.display.blit(self.font.render('jogar novamente', False, (0, 0, 0)), (2*self.width/5 - 20, self.height/2+5))       

                        score1 = self.p1.getScore()
                        score2 = self.p2.getScore()

                        if score1>score2:
                            self.display.blit(self.font.render('PLAYER 1 GANHOU!', False, (0, 0, 0)), (self.width/3,400))
                        else:
                            self.display.blit(self.font.render('PLAYER 2 GANHOU!', False, (0, 0, 0)), (self.width/3,400))

                        self.isOver = False
                        for card in self.cards:
                            card.restore()

                        self.p1.setScoreZero()
                        self.p2.setScoreZero()
                        
                        self.onInit()
                                    

                for card in self.cards:
                    x,y = event.pos
                    minX,minY,maxX,maxY = card.getPoints()
                    isTurned = card.isShow()
                    if (x>minX and x<maxX and y>minY and y<maxY) and not isTurned:
                        
                        if self.c1==None:
                            self.c1 = card
                            self.c1.onClick()

                        elif self.c2==None and card!=self.c1:
                            self.c2 = card
                            self.c2.onClick()
                        
                        if self.c1!=None and self.c2!=None:
                            if self.c1.getValue() != self.c2.getValue():
                                self.onRender()
                                time.sleep(1)

                                self.c1.restore()
                                self.c2.restore()

                                self.changeTurn()
                                
                            else:

                                if self.turn == 1:
                                    print("limpa 1")
                                    self.display.blit(self.font.render(str(self.p1.getScore()), False, (0, 0, 0)), (40,450))
                                elif self.turn == 2:
                                    print("limpa 2")
                                    self.display.blit(self.font.render(str(self.p2.getScore()), False, (0, 0, 0)), (80,450))

                                self.activePlayer.addScore()
                                
                            self.c1 = None
                            self.c2 = None

    def onRender(self):
        for card in self.cards:
            x, y = card.getPoints()[0:2]
            color = card.getColor()
            
            pygame.draw.rect(self.display, color, pygame.Rect(x, y, 50, 50))
            self.display.blit(self.font.render(str(card.getValue()), False, (255, 0, 0)), (x+20,y+20))

        
        if self.turn == 1: # turno jogador 1
            self.display.blit(self.font.render('player 2', False, (0, 0, 0)), (self.width/2 - 35,400))
            self.display.blit(self.font.render('player 1', False, (0, 255, 0)), (self.width/2 - 35,400))
        elif self.turn == 2: # turno jogador 2
            self.display.blit(self.font.render('player 1', False, (0, 0, 0)), (self.width/2 - 35,400))
            self.display.blit(self.font.render('player 2', False, (0, 0, 255)), (self.width/2 - 35,400))

        
        if self.turn == 1:
            self.display.blit(self.font.render(str(self.p1.getScore()), False, (0, 0, 0)), (40,450))
        elif self.turn ==2:
            self.display.blit(self.font.render(str(self.p2.getScore()), False, (0, 0, 0)), (80,450))


        self.display.blit(self.font.render(str(self.p1.getScore()), False, (0, 255, 0)), (40,450))
        self.display.blit(self.font.render(str(self.p2.getScore()), False, (0, 0, 255)), (80,450))
        
        if self.isOver:
            self.display.fill((0,0,0))

            score1 = self.p1.getScore()
            score2 = self.p2.getScore()

            if score1>score2:
                self.display.blit(self.font.render('PLAYER 1 GANHOU!', False, (0, 255, 0)), (self.width/3,400))
            elif score2>score1:
                self.display.blit(self.font.render('PLAYER 2 GANHOU!', False, (0, 0, 255)), (self.width/3,400))
            else:
                self.display.blit(self.font.render('EMPATE', False, (255, 255, 255)), (self.width/3,400))

            pygame.draw.rect(self.display, (170, 170, 170), pygame.Rect(2*self.width/5-35, self.height/2, 200, 30))
            self.display.blit(self.font.render('jogar novamente', False, (10, 10, 10)), (2*self.width/5 - 20, self.height/2+5))
        
        pygame.display.flip()
            
    def onLoop(self):
        self.isOver = True
        for card in self.cards:
            if card.isShow() == False:
                self.isOver = False

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
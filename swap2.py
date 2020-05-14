import Game
import pygame, sys
import board
from  CheckBoardState import CheckBoardState
from Globals import BOARDSIZE, screen
from AI import AI
from Player import Player
import copy

class Swap2(Game.Game):
    def __init__(self,player1,player2,onMove):
        super(Swap2, self).__init__()
        self.player1=player1
        self.player2=player2
        self.onMove=onMove
        self.change=True
    def changePlayer(self):
        temp=self.player1
        self.player1=self.player2
        self.player2=temp
        del(temp)
    def chooseColor(self):
        self.b1.white()
        self.b2.black()
        pygame.display.update()
    def playgame(self):
        self.b.draw()
        pygame.draw.rect(screen, (102, 51, 0), (700, 200, 60, 60))
        while self.run:
            pygame.display.update()
            pygame.time.delay(100)
            # handle events
            if self.moveNumber == 3:
                self.chooseColor()
                while self.change:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit(0)
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos=pygame.mouse.get_pos()
                            if self.b1.rect.collidepoint(pos):
                                print("Clicked b1")
                                self.changePlayer()
                                self.change = False
                            if self.b2.rect.collidepoint(pos):
                                print("Clicked b1")
                                self.change = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.buttonSettings.graphic.collidepoint(pos):
                        return True
                    for i in range(0, BOARDSIZE):
                        for j in range(0, BOARDSIZE):
                            if self.b.square[i][j].graphic.collidepoint(pos) and self.b.square[i][j].value == '_':
                                print("Wykonuje ruch:",self.onMove.name)
                                if self.onMove.name !="AI" :
                                    self.makeMove(i, j)
                                    pygame.display.update()
                                else:
                                    i,j=self.ai.playBest(self.playedMoves)
                                    self.makeMove(i,j)
                                    pygame.display.update()

                                if self.arbiter.checkBoardState(self.moveNumber,self.onMove.name):
                                    break
                    pygame.display.update()


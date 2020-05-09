import pygame, sys, time, Globals, math
import board
from  CheckBoardState import CheckBoardState
from Globals import BOARDSIZE, WIN, screenWidth, screenHeight, screen, maxDepth, maxMoveTime
from AI import AI



class Game:
    def __init__(self):
        self.run = True
        self.moveNumber = 1
        self.b = board.Board()
        self.button=board.Button()
        self.onMove = "white"
        self.arbiter=CheckBoardState(self.b)
        self.ai=AI(self.b,self.moveNumber)
        self.onMoveGUI=board.OnMove()
        self.onMoveGUI.white()
        self.playedMoves=set()


    def makeMove(self, i, j):
        print("Ruch numer:",self.moveNumber)
        if self.onMove == "white":
            self.b.square[i][j].whiteSquare(i, j)
            self.b.square[i][j].value = "white"
            self.onMove = "black"
            self.onMoveGUI.black()
        else:
            self.b.square[i][j].blackSquare(i, j)
            self.b.square[i][j].value = "black"
            self.onMove = "white"
            self.onMoveGUI.white()
        self.moveNumber += 1
        self.playedMoves.add((i,j))
        self.ai.addNeighboursSquares(i, j, 0,self.playedMoves)


    def playgame(self):
        screen.fill((0, 0, 0))
        self.b.draw()
        pygame.draw.rect(screen, (102, 51, 0), (700, 200, 60, 60))
        while self.run:
            pygame.display.update()
            pygame.time.delay(100)
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.button.graphic.collidepoint(pos):
                        return True
                    for i in range(0, BOARDSIZE):
                        for j in range(0, BOARDSIZE):
                            if self.b.square[i][j].graphic.collidepoint(pos) and self.b.square[i][j].value == '_':
                                if self.onMove == "white":
                                    self.makeMove(i, j)
                                    pygame.display.update()
                                if self.arbiter.checkBoardState(self.moveNumber):
                                    break
                                if self.onMove == "black":
                                    #starTime = time.time()
                                    i,j=self.ai.playBest(self.playedMoves)
                                    self.makeMove(i,j)
                                    #print("Minelo tyle czasu", starTime - time.time())
                                    pygame.display.update()
                                if self.arbiter.checkBoardState(self.moveNumber):
                                    break
                    pygame.display.update()


import pygame, sys, time, Globals, math
import board
from  CheckBoardState import CheckBoardState
from Globals import BOARDSIZE, WIN, screenWidth, screenHeight, screen, maxDepth, maxMoveTime
from AI import AI

IMPORTANT = math.inf
WHITE_WIN = -100000
BLACK_WIN = 100000

class Game:
    def __init__(self):
        self.run = True
        self.moveNumber = 1
        self.b = board.Board()
        self.onMove = "white"
        self.arbiter=CheckBoardState(self.b)
        self.ai=AI(self.b,self.moveNumber)


    def makeMove(self, i, j):
        if self.onMove == "white":
            self.b.square[i][j].whiteSquare(i, j)
            self.b.square[i][j].value = "white"
            self.onMove = "black"
            pygame.draw.circle(screen, (0, 0, 0), (700 + 30, 200 + 30), 30)
        else:
            self.b.square[i][j].blackSquare(i, j)
            self.b.square[i][j].value = "black"
            self.onMove = "white"
            pygame.draw.circle(screen, (255, 255, 255), (700 + 30, 200 + 30), 30)
        self.moveNumber += 1
        self.ai.addNeighboursSquares(i, j, 0)



    def playgame(self):
        screen.fill((0, 0, 0))
        self.b.draw()
        pygame.draw.rect(screen, (102, 51, 0), (700, 200, 60, 60))
        pygame.draw.circle(screen, (255, 255, 255), (700 + 30, 200 + 30), 30)
        while self.run:
            pygame.display.update()
            pygame.time.delay(100)
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for i in range(0, BOARDSIZE):
                        for j in range(0, BOARDSIZE):
                            if self.b.square[i][j].graphic.collidepoint(pos) and self.b.square[i][j].value == '_':
                                if self.onMove == "white":
                                    self.makeMove(i, j)
                                    pygame.display.update()
                                if self.arbiter.checkWin(0):
                                    self.board.messageWin()
                                    break
                                elif self.arbiter.checkDraw(self.moveNumber):
                                    self.arbiter.draw()
                                    break
                                if self.onMove == "black":
                                    starTime = time.time()
                                    i,j=self.ai.playBest()
                                    self.makeMove(i,j)
                                    print("Minelo tyle czasu", starTime - time.time())
                                    pygame.display.update()
                                if self.arbiter.checkWin(0):
                                    board.messageWin()
                                    break
                                elif self.arbiter.checkDraw(self.moveNumber):
                                    board.messageDraw()
                    pygame.display.update()


game = Game()
game.playgame()
time.sleep(5)
sys.exit(0)

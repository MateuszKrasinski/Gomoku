import pygame, sys
import board
from  CheckBoardState import CheckBoardState
from Globals import BOARDSIZE, screen
from AI import AI
import Game
class swap2(Game.Game):
    def __init__(self):
        super(swap2, self).__init__()
        super()
    def playgame(self):
        screen.fill((0, 0, 0))
        self.b.draw()
        pygame.draw.rect(screen, (102, 51, 0), (700, 200, 60, 60))
        while self.run:
            pygame.display.update()
            pygame.time.delay(100)
            # handle events
            for event in pygame.event.get():
                if self.moveNumber==3:
                    board.message("Choose your stone_color",400,70)
                    black=board.ChooseColor()
                    pygame.display.update()
                else:
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if self.button.graphic.collidepoint(pos):
                            return True
                        for i in range(0, BOARDSIZE):
                            for j in range(0, BOARDSIZE):
                                if self.b.square[i][j].graphic.collidepoint(pos) and self.b.square[i][j].value == '_':
                                    if self.moveNumber<3:
                                        print("Na ruchu :",self.onMove)
                                        if self.onMove == self.player1:
                                            self.makeMove(i, j)
                                            pygame.display.update()
                                        elif self.onMove == self.player2:
                                            self.makeMove(i, j)
                                            pygame.display.update()
                                    else:
                                        if self.onMove.get_stone_color() == "white":
                                            self.makeMove(i, j)
                                            pygame.display.update()
                                        if self.arbiter.checkBoardState(self.moveNumber,self.onMove.name):
                                            break
                                        if self.onMove.get_stone_color() == "black":
                                            # starTime = time.time()
                                            i, j = self.ai.playBest(self.playedMoves)
                                            self.makeMove(i, j)
                                            # print("Minelo tyle czasu", starTime - time.time())
                                            pygame.display.update()
                                        if self.arbiter.checkBoardState(self.moveNumber,self.onMove.name):
                                            break
                    pygame.display.update()


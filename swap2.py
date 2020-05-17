from Game import Player, Game
import pygame, sys

BOARDSIZE = 15


class Swap2(Game):
    def __init__(self, player1, player2, onMove):
        super(Swap2, self).__init__()
        self.player1 = player1
        self.player2 = player2
        self.onMove = onMove
        self.change = True

    def changePlayer(self):
        temp = self.player1
        self.player1 = self.player2
        self.player2 = temp
        self.onMove = self.player1
        del (temp)

    def chooseColor(self):
        self.b1.white()
        self.b2.black()
        pygame.display.update()

    def hideColor(self):
        self.b1.hide()
        pygame.display.update()
        pygame.time.delay(200)

    def selectColor(self):
        self.chooseColor()
        while self.change:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if self.onMove.name == "AI":
                    self.change = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.b1.rect.collidepoint(pos):
                        print("Clicked b1")
                        self.onMoveGUI.black("Gracz1")
                        self.changePlayer()
                        self.change = False
                    if self.b2.rect.collidepoint(pos):
                        print("Clicked b2")
                        self.change = False

    def playgame(self):
        self.b.draw()
        while True:
            pygame.display.update()
            pygame.time.delay(100)
            if self.onMove.name == "AI":
                bestMove = self.ai.playBest(self.playedMoves)
                self.makeMove(bestMove[0], bestMove[1])
                if self.arbiter.checkBoardState(self.moveNumber,
                                                self.onMove.name):
                    self.run = False
                self.nextTurn()
                pygame.display.update()
            if self.moveNumber == 3:
                self.selectColor()
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.buttonSettings.graphic.collidepoint(pos):
                        return "Menu"
                    if self.buttonNewGame.graphic.collidepoint(pos):
                        return "Restart"
                    if self.run:
                        for i in range(0, BOARDSIZE):
                            for j in range(0, BOARDSIZE):
                                if self.b.square[i][j].graphic.collidepoint(
                                        pos) and self.board[i][j] == '_':
                                    print("Wykonuje ruch:", self.onMove.name)
                                    if self.onMove.name != "AI":
                                        self.makeMove(i, j)
                                        pygame.display.update()
                                    if self.arbiter.checkBoardState(
                                            self.moveNumber, self.onMove.name):
                                        self.run = False
                                        break
                                    self.nextTurn()
                    pygame.display.update()

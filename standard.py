from Game import Player, Game
import pygame, sys

BOARDSIZE = 15


class Standard(Game):
    def __init__(self, player1, player2, onMove):
        super(Standard, self).__init__()
        self.player1 = player1
        self.player2 = player2
        self.onMove = onMove

    def playgame(self):
        self.b.draw()
        while True:
            pygame.display.update()
            # pygame.time.delay(100)
            if self.onMove.name == "AI":
                bestMove = self.ai.playBest(self.playedMoves)
                self.makeMove(bestMove[0], bestMove[1])
                if self.arbiter.checkBoardState(self.moveNumber,
                                                self.onMove.name):
                    self.run = False
                self.nextTurn()
                pygame.display.update()
            # handle events
            for event in pygame.event.get():
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
                                    if self.onMove.name != "AI":
                                        self.makeMove(i, j)
                                        pygame.display.update()
                                    if self.arbiter.checkBoardState(
                                            self.moveNumber, self.onMove.name):
                                        self.run = False
                                        break
                                    self.nextTurn()
                    pygame.display.update()

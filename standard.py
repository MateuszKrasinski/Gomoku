import sys
import pygame
import gui
from game import Game

BOARDSIZE = 15


class Standard(Game):
    def __init__(self, player1, player2, on_move):
        super(Standard, self).__init__()
        self.player1 = player1
        self.player2 = player2
        self.on_move = on_move

    def playgame(self):
        gui.draw_board(self.board_gui)
        while True:
            pygame.display.update()
            pygame.time.delay(100)
            if self.on_move.name == "AI":
                self.ai_move()
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.buttton_menu.graphic.collidepoint(pos):
                        return "Menu"
                    if self.buttton_new_game.graphic.collidepoint(pos):
                        return "Restart"
                    if self.run:
                        for i in range(0, BOARDSIZE):
                            for j in range(0, BOARDSIZE):
                                if self.board_gui[i][j].graphic.collidepoint(
                                        pos) and self.board[i][j] == '_':
                                    if self.on_move.name != "AI":
                                        self.make_move(i, j)
                                        pygame.display.update()
                                    if self.arbiter.checkBoardState(self.move_number,
                                                                    self.on_move.name):
                                        self.run = False
                                        break
                                    self.next_turn()
                    pygame.display.update()

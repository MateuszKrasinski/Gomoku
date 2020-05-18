import sys
import pygame
from game import Game

BOARDSIZE = 15


class Swap2(Game):
    def __init__(self, player1, player2, on_move):
        super(Swap2, self).__init__()
        self.player1 = player1
        self.player2 = player2
        self.on_move = on_move
        self.change = True

    def change_player(self):
        temp = self.player1
        self.player1 = self.player2
        self.player2 = temp
        self.on_move = self.player1
        del temp

    def choose_color(self):
        self.b1.white()
        self.b2.black()
        pygame.display.update()


    def select_color(self):
        self.choose_color()
        while self.change:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if self.on_move.name == "AI":
                    self.change = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.b1.rect.collidepoint(pos):
                        print("Clicked b1")
                        self.on_move_gui.black("Gracz1")
                        self.change_player()
                        self.change = False
                    if self.b2.rect.collidepoint(pos):
                        print("Clicked b2")
                        self.change = False

    def playgame(self):
        self.b.draw()
        while True:
            pygame.display.update()
            pygame.time.delay(100)
            if self.on_move.name == "AI":
                best_move = self.ai.play_best(self.played_moves)
                self.make_move(best_move[0], best_move[1])
                if self.arbiter.checkBoardState(self.moveNumber,
                                                self.on_move.name):
                    self.run = False
                self.next_turn()
                pygame.display.update()
            if self.moveNumber == 3:
                self.select_color()
            for event in pygame.event.get():
                pygame.display.update()
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
                                if self.b.square[i][j].graphic.collidepoint(
                                        pos) and self.board[i][j] == '_':
                                    print("Wykonuje ruch:", self.on_move.name)
                                    if self.on_move.name != "AI":
                                        self.make_move(i, j)
                                        pygame.display.update()
                                    if self.arbiter.checkBoardState(
                                            self.moveNumber, self.on_move.name):
                                        self.run = False
                                        break
                                    self.next_turn()
                    pygame.display.update()

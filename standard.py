"""Module contains class Standard which allows to start game on standard rules"""
import sys

import pygame

import gui
import game
import constants

BOARD_SIZE = 15
WHITE = "white"
BLACK = "black"
EMPTY = "_"
AI = "AI"


class Standard(game.Game):
    """Class contains all methods and attributes to play game on standard rules."""

    def __init__(self, player1, player2, on_move):
        """Init from base class init and override with arguments chosen in game menu."""
        super(Standard, self).__init__()
        self.player1 = player1
        self.player2 = player2
        self.player_on_move = on_move
        if self.player_on_move.stone_color == WHITE:
            self.gui_on_move.white(self.player_on_move.name)
        else:
            self.gui_on_move.black(self.player_on_move.name)

    def playgame(self):
        """Starts game on standard rules restart or back to menu depending of clicked button."""
        gui.draw_board(self.gui_board)
        while True:
            pygame.display.update()
            pygame.time.delay(100)
            if self.player_on_move.name == AI:
                self.ai_move()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if self.button_menu.graphic.collidepoint(pos):
                            return constants.MENU
                        if self.button_new_game.graphic.collidepoint(pos):
                            return constants.RESTART
                        if self.game_running and self.player_on_move.make_move(pos,
                                                                               self.gui_board,
                                                                               self.game_board):
                            i, j = self.player_on_move.make_move(pos, self.gui_board,
                                                                 self.game_board)
                            self.make_move(i, j)
                            if self.game_arbiter.check_board_state(self.player_on_move.name):
                                self.game_running = False
                                break
                            self.next_turn()
                    pygame.display.update()

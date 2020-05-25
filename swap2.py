"""Module contains class Swap2 which allows to start game on swap2 rules."""
import sys
import random

import pygame

import gui
import game
import constants


class Swap2(game.Game):
    """Class contains all methods and attributes to play game on standard rules."""

    def __init__(self, player1, player2, on_move):
        """Init from base class init and override with arguments chosen in game menu."""
        super(Swap2, self).__init__()
        self.player1 = player1
        self.player2 = player2
        self.player_on_move = on_move
        self.change = True
        if self.player_on_move.stone_color == constants.WHITE:
            self.gui_on_move.white(self.player_on_move.name)
        else:
            self.gui_on_move.black(self.player_on_move.name)

    def game_opening(self):
        """Method allows starting player to put 3 stones before selecting colors"""
        if self.game_move_number == 0 and self.player_on_move.name == constants.AI:
            random_number = []
            counter = 0
            while counter < 3:
                number = (random.randint((constants.BOARD_SIZE - 1) // 2 - 1,
                                         (constants.BOARD_SIZE - 1) // 2 + 1),
                          random.randint((constants.BOARD_SIZE - 1) // 2 - 1,
                                         (constants.BOARD_SIZE - 1) // 2 + 1))
                if number not in random_number:
                    random_number.append(number)
                    counter += 1
            self.gui_on_move.change_message(self.player2.name)
            self.make_move(random_number[0][0], random_number[0][1])
            self.next_turn()
            self.gui_on_move.change_message(self.player2.name)
            self.make_move(random_number[1][0], random_number[1][1])
            self.next_turn()
            self.gui_on_move.change_message(self.player2.name)
            self.make_move(random_number[2][0], random_number[2][1])
            self.next_turn()
        else:
            if self.player_on_move == self.player1 and self.game_move_number == 0:
                name = self.player1.name
            elif self.player_on_move == self.player2 and self.game_move_number == 0:
                name = self.player2.name
            else:
                name = self.player1.name
            self.gui_on_move.change_message(name)

    def change_player(self):
        """Method allows to change player's stone color according to swap2 rules."""
        if self.player_on_move == self.player2:
            self.player1.stone_color = constants.BLACK
            self.player2.stone_color = constants.WHITE
            self.player_on_move = self.player1
        else:
            self.player1.stone_color = constants.BLACK
            self.player2.stone_color = constants.WHITE
            self.player_on_move = self.player2

    def choose_color(self):
        """Method shows on left-top of the screen choosing color graphic"""
        self.button_white_stone.white()
        self.button_black_stone.black()
        pygame.display.update()

    def select_color(self):
        """Method allows to select color at move 3 according to swap2 rules"""
        self.choose_color()
        while self.change:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if self.player_on_move.name == constants.AI:
                    self.game_arbiter.check_board_state(self.player_on_move.name)
                    if self.game_arbiter.evaluate() >= 0:
                        if self.player_on_move.stone_color == constants.WHITE:
                            self.change_player()
                            self.button_white_stone.hide()
                        else:
                            self.change = False
                            self.button_white_stone.hide()
                    else:
                        if self.player_on_move.stone_color == constants.WHITE:
                            self.change = False
                            self.button_white_stone.hide()
                        else:
                            self.change_player()
                            self.button_white_stone.hide()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.button_white_stone.graphic.collidepoint(pos):
                        if self.player_on_move == self.player2:
                            self.gui_on_move.black(self.player1.name)
                            self.change_player()
                            self.change = False
                            self.button_white_stone.hide()
                        else:
                            self.change = False
                            self.button_white_stone.hide()
                    if self.button_black_stone.graphic.collidepoint(pos):
                        if self.player_on_move == self.player2:
                            self.change = False
                            self.button_white_stone.hide()
                        else:
                            self.gui_on_move.white(self.player2.name)
                            self.change_player()
                            self.change = False
                            self.button_white_stone.hide()

    def playgame(self):
        """Starts game on swap2 rules restart or back to menu depending of clicked button."""
        gui.draw_board(self.gui_board)
        while True:
            if self.game_move_number < 3:
                self.game_opening()
            if self.player_on_move.name == constants.AI and self.game_move_number >= 3:
                self.ai_move()
            if self.game_move_number == 3 and self.change:
                self.select_color()
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.button_menu.graphic.collidepoint(pos):
                        return constants.MENU
                    if self.button_new_game.graphic.collidepoint(pos):
                        return constants.RESTART
                    if self.game_running:
                        for i in range(0, constants.BOARD_SIZE):
                            for j in range(0, constants.BOARD_SIZE):
                                if self.gui_board[i][j].graphic.collidepoint(
                                        pos) and self.game_board[i][j] == constants.EMPTY:
                                    if self.player_on_move.name:
                                        self.make_move(i, j)
                                        pygame.display.update()
                                    if self.game_arbiter.check_board_state(
                                            self.player_on_move.name):
                                        self.game_running = False
                                        break
                                    self.next_turn()
                    pygame.display.update()

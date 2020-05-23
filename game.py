"""Module contains class Player and Game which allows to create base of the game"""
import sys
from dataclasses import dataclass

import pygame

import gui
from check_board_state import CheckBoardState
from ai import AI

BOARDSIZE = 15
EMPTY = "_"
WHITE = "white"
BLACK = "black"
PLAYER1_NAME = "Gracz1"
PLAYER2_NAME = "Gracz2"


@dataclass
class Player:
    """Class creating player object with attributes name, stone_color"""
    name: str
    stone_color: str


class Game:
    """Class set up all need operations and attributes to play game."""

    def __init__(self):
        """Init Game with all needed attributes. """

        gui.draw_background()
        self.game_running = True
        self.game_move_number = 0
        self.game_board = [[EMPTY for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.game_arbiter = CheckBoardState(self.game_board)
        self.ai = AI(self.game_board)
        self.played_moves = set()
        self.player1 = Player(PLAYER1_NAME, WHITE)
        self.player2 = Player("AI", BLACK)
        self.player_on_move = self.player1
        self.game_mode = "standard"
        self.gui_board = [[gui.Square() for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.gui_on_move = gui.OnMove()
        self.button_new_game = gui.ButtonRightMenu(0, "New Game")
        self.button_menu = gui.ButtonRightMenu(1, "Menu")
        self.button_white_stone = gui.ButtonChooseColor(0)
        self.button_black_stone = gui.ButtonChooseColor(1)
        self.button_ai_opponent = gui.ButtonChooseOpponent(0)
        self.button_ai_player = gui.ButtonChooseOpponent(1)
        self.button_standard_game_mode = gui.ButtonChooseMode(0)
        self.button_swap2_game_mode = gui.ButtonChooseMode(1)
        self.last_move = tuple()

    def menu(self):
        """Setting up on screen menu where player can choose game options before start. """
        self.gui_on_move.white(self.player_on_move.name)
        self.button_white_stone.white(selected=True)
        self.button_black_stone.black()
        self.button_ai_opponent.AI(selected=True)
        self.button_ai_player.player()
        self.button_standard_game_mode.standard(selected=True)
        self.button_swap2_game_mode.swap2()
        pygame.display.update()
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.button_new_game.graphic.collidepoint(pos):
                        self.game_running = False
                        return self.player1, self.player2, self.player_on_move, self.game_mode
                    if self.button_white_stone.graphic.collidepoint(pos):
                        self.player_on_move = self.player1
                        self.gui_on_move.white(self.player1.name)
                        self.button_white_stone.white(selected=True)
                        self.button_black_stone.black(selected=False)
                    if self.button_black_stone.graphic.collidepoint(pos):
                        self.gui_on_move.black(self.player2.name)
                        self.button_white_stone.white(selected=False)
                        self.button_black_stone.black(selected=True)
                        self.player_on_move = self.player2
                    if self.button_ai_opponent.graphic.collidepoint(pos):
                        self.player2.name = "AI"
                        if self.player_on_move == self.player2:
                            self.gui_on_move.black(self.player2.name)
                        self.button_ai_opponent.AI(selected=True)
                        self.button_ai_player.player(selected=False)
                    if self.button_ai_player.graphic.collidepoint(pos):
                        self.player2.name = PLAYER2_NAME
                        if self.player_on_move == self.player2:
                            self.gui_on_move.black(self.player2.name)
                        self.button_ai_opponent.AI(selected=False)
                        self.button_ai_player.player(selected=True)
                    if self.button_standard_game_mode.graphic.collidepoint(pos):
                        self.game_mode = "standard"
                        self.button_standard_game_mode.standard(selected=True)
                        self.button_swap2_game_mode.swap2(selected=False)
                    if self.button_swap2_game_mode.graphic.collidepoint(pos):
                        self.game_mode = "swap2"
                        self.button_standard_game_mode.standard()
                        self.button_swap2_game_mode.swap2(True)
                    pygame.display.update()

    def ai_move(self):
        """Playing the best found movie in AI module using mini max alghoritm."""
        if self.player_on_move.stone_color == "black":
            best_move = self.ai.play_best(self.played_moves)
        else:
            best_move = self.ai.play_best(self.played_moves, black_color=False)
        self.make_move(best_move[0], best_move[1])
        if self.game_arbiter.check_board_state(self.player_on_move.name):
            self.game_running = False
        self.next_turn()
        pygame.display.update()

    def next_turn(self):
        """Method changes player on move and all GUI about it."""
        if self.player_on_move == self.player1:
            self.player_on_move = self.player2
            if self.player_on_move.stone_color == WHITE:
                self.gui_on_move.white(self.player_on_move.name)
            else:
                self.gui_on_move.black(self.player_on_move.name)
        elif self.player_on_move == self.player2:
            self.player_on_move = self.player1
            if self.player_on_move.stone_color == WHITE:
                self.gui_on_move.white(self.player_on_move.name)
            else:
                self.gui_on_move.black(self.player_on_move.name)

    def make_move(self, i, j):
        """Making move on given i,j from ai_move or selected by user."""
        if self.player_on_move.stone_color == WHITE:
            if self.game_move_number > 0:
                self.gui_board[i][j].draw_empty_square(self.last_move[0], self.last_move[1])
                self.gui_board[i][j].draw_black_stone(self.last_move[0], self.last_move[1])
            self.gui_board[i][j].draw_white_stone(i, j, True)
            self.game_board[i][j] = WHITE
        else:
            if self.game_move_number > 0:
                self.gui_board[i][j].draw_empty_square(self.last_move[0], self.last_move[1])
                self.gui_board[i][j].draw_white_stone(self.last_move[0], self.last_move[1])
            self.gui_board[i][j].draw_black_stone(i, j, True)
            self.game_board[i][j] = BLACK
        self.game_move_number += 1
        self.played_moves.add((i, j))
        self.ai.add_neighbours_squares(i, j, 0, self.played_moves)
        self.last_move = i, j

    def playgame(self):
        """Base function handling all game rules  chosen in menu mode"""

"""Module contains class Player and Game which allows to create base of the game"""
import sys
import collections

import pygame

import gui
import check_board_state
import players
import constants

GameSettings = collections.namedtuple("GameSettings", "player1 player2 player_on_move game_mode")
LastMove = collections.namedtuple("LastMove", "i j")


class Game:
    """Class set up all need operations and attributes to play game."""

    def __init__(self, screen):
        """Init Game with all needed attributes. """
        self.screen = screen
        self.gui = gui.Gui(self.screen)
        self.gui.draw_background()
        self.game_running = True
        self.game_move_number = 0
        self.game_board = check_board_state.create_board()
        self.game_arbiter = check_board_state.CheckBoardState(self.screen, self.game_board)
        self.played_moves = []
        self.player1 = players.HumanPlayer(constants.PLAYER1_NAME, constants.WHITE)
        self.player2 = players.AiPlayer(self.screen, self.game_board, constants.BLACK)
        self.player_on_move = self.player1
        self.game_mode = constants.STANDARD
        self.gui_board = [[gui.Square(self.screen) for i in range(constants.BOARD_SIZE)] for j in
                          range(constants.BOARD_SIZE)]
        self.gui_on_move = gui.OnMove(self.screen)
        self.button_new_game = gui.ButtonRightMenu(self.screen, 0, constants.RESTART)
        self.button_menu = gui.ButtonRightMenu(self.screen, 1, constants.MENU)
        self.button_white_stone = gui.ButtonChooseColor(self.screen, 0)
        self.button_black_stone = gui.ButtonChooseColor(self.screen, 1)
        self.button_ai_opponent = gui.ButtonChooseOpponent(self.screen, 0)
        self.button_ai_player = gui.ButtonChooseOpponent(self.screen, 1)
        self.button_standard_game_mode = gui.ButtonChooseMode(self.screen, 0)
        self.button_swap2_game_mode = gui.ButtonChooseMode(self.screen, 1)
        self.last_move = LastMove

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
                        return GameSettings(player1=self.player1, player2=self.player2,
                                            player_on_move=self.player_on_move,
                                            game_mode=self.game_mode)
                    if self.button_white_stone.graphic.collidepoint(pos):
                        self.player_on_move = self.player1
                        self.gui_on_move.white(self.player1.name)
                        self.button_white_stone.white(selected=True)
                        self.button_black_stone.black(selected=False)
                    if self.button_black_stone.graphic.collidepoint(pos):
                        self.player_on_move = self.player2
                        self.gui_on_move.black(self.player2.name)
                        self.button_white_stone.white(selected=False)
                        self.button_black_stone.black(selected=True)
                    if self.button_ai_opponent.graphic.collidepoint(pos):
                        self.player2 = players.AiPlayer(self.screen, self.game_board,
                                                        self.player2.stone_color)
                        if self.player_on_move.stone_color == self.player2.stone_color:
                            self.player_on_move = self.player2
                            self.gui_on_move.black(self.player2.name)
                        self.button_ai_opponent.AI(selected=True)
                        self.button_ai_player.player(selected=False)
                    if self.button_ai_player.graphic.collidepoint(pos):
                        self.player2 = players.HumanPlayer(constants.PLAYER2_NAME,
                                                           self.player2.stone_color)
                        if self.player_on_move.stone_color == self.player2.stone_color:
                            self.player_on_move = self.player2
                            self.gui_on_move.black(self.player2.name)
                        self.button_ai_opponent.AI(selected=False)
                        self.button_ai_player.player(selected=True)
                    if self.button_standard_game_mode.graphic.collidepoint(pos):
                        self.game_mode = constants.STANDARD
                        self.button_standard_game_mode.standard(selected=True)
                        self.button_swap2_game_mode.swap2(selected=False)
                    if self.button_swap2_game_mode.graphic.collidepoint(pos):
                        self.game_mode = constants.SWAP2
                        self.button_standard_game_mode.standard()
                        self.button_swap2_game_mode.swap2(True)
                    pygame.display.update()

    def ai_move(self):
        """Playing the best found movie in AI module using mini max alghoritm."""
        if self.player_on_move.stone_color == constants.BLACK:
            best_move = self.player_on_move.make_move(self.game_board, self.played_moves)
        else:
            best_move = self.player_on_move.make_move(self.game_board, self.played_moves, False)
        self.make_move(best_move[0], best_move[1])
        if self.game_arbiter.check_board_state(self.player_on_move.name):
            self.game_running = False
        self.next_turn()
        pygame.display.update()

    def next_turn(self):
        """Method changes player on move and all GUI about it."""
        if self.player_on_move == self.player1:
            self.player_on_move = self.player2
            if self.player_on_move.stone_color == constants.WHITE:
                self.gui_on_move.white(self.player_on_move.name)
            else:
                self.gui_on_move.black(self.player_on_move.name)
        elif self.player_on_move == self.player2:
            self.player_on_move = self.player1
            if self.player_on_move.stone_color == constants.WHITE:
                self.gui_on_move.white(self.player_on_move.name)
            else:
                self.gui_on_move.black(self.player_on_move.name)

    def make_move(self, i, j):
        """Making move on given i,j from ai_move or selected by user."""
        if self.player_on_move.stone_color == constants.WHITE:
            if self.game_move_number > 0:
                self.gui_board[i][j].draw_empty_square(self.last_move[0], self.last_move[1])
                self.gui_board[i][j].draw_black_stone(self.last_move[0], self.last_move[1])
            self.gui_board[i][j].draw_white_stone(i, j, True)
            self.game_board[i][j] = constants.WHITE
        else:
            if self.game_move_number > 0:
                self.gui_board[i][j].draw_empty_square(self.last_move[0], self.last_move[1])
                self.gui_board[i][j].draw_white_stone(self.last_move[0], self.last_move[1])
            self.gui_board[i][j].draw_black_stone(i, j, True)
            self.game_board[i][j] = constants.BLACK
        self.game_move_number += 1
        self.played_moves.append((i, j))
        self.last_move = i, j

    def playgame(self):
        """Base function handling all game rules  chosen in menu mode"""

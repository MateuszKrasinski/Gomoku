import sys
import pygame
import gui
from check_board_state import CheckBoardState
from ai import AI

BOARDSIZE = 15
EMPTY = "_"
WHITE = "white"
BLACK = "black"


class Player():
    def __init__(self, name_="Gracz", stone_=WHITE):
        self.name = name_
        self.stone_color = stone_

    def get_stone_color(self):
        return str(self.stone_color)

    def stone_white(self):
        self.stone_color = WHITE

    def stone_black(self):
        self.stone_color = BLACK

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Game:
    def __init__(self):
        self.run = True
        self.move_number = 0
        gui.Background()
        self.board = [[EMPTY for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.board_gui = [[gui.Square() for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.buttton_new_game = gui.Button(0, "New Game")
        self.buttton_menu = gui.Button(1, "Menu")
        self.arbiter = CheckBoardState(self.board)
        self.ai = AI(self.board, self.move_number)
        self.played_moves = set()
        self.player1 = Player("Gracz1", WHITE)
        self.player2 = Player("AI", BLACK)
        self.mode = "standard"
        self.on_move = self.player1
        self.on_move_gui = gui.OnMove()

        self.white_stone_button = gui.ChooseColor(0)
        self.black_stone_button = gui.ChooseColor(1)
        self.ai_opponent_button = gui.ChooseOpponent(0)
        self.player_opponent_button = gui.ChooseOpponent(1)
        self.standard_mode_button = gui.ChooseMode(0)
        self.swap2_mode_button = gui.ChooseMode(1)


    def menu(self):
        self.on_move_gui.white(self.on_move.name)
        self.white_stone_button.white(True)
        self.black_stone_button.black()
        self.ai_opponent_button.AI(True)
        self.player_opponent_button.player()
        self.standard_mode_button.stanard(True)
        self.swap2_mode_button.swap2()
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.buttton_new_game.graphic.collidepoint(pos):
                        run = False
                        return self.player1, self.player2, self.on_move, self.mode
                    if self.white_stone_button.graphic.collidepoint(pos):
                        print("Clicked white")
                        self.on_move = self.player1
                        self.on_move_gui.white(self.player1.name)
                        self.white_stone_button.white(True)
                        self.black_stone_button.black()
                    if self.black_stone_button.graphic.collidepoint(pos):
                        print("Clicked black")
                        self.on_move_gui.black(self.player2.name)
                        self.white_stone_button.white(False)
                        self.black_stone_button.black(True)
                        self.on_move = self.player2
                    if self.ai_opponent_button.graphic.collidepoint(pos):
                        print("Clicked ai_opponent_button")
                        self.player2.name="AI"
                        if self.on_move == self.player2:
                            self.on_move_gui.black(self.player2.name)
                        self.ai_opponent_button.AI(True)
                        self.player_opponent_button.player(False)
                    if self.player_opponent_button.graphic.collidepoint(pos):
                        self.player2.set_name("Gracz2")
                        if self.on_move==self.player2:
                            self.on_move_gui.black(self.player2.name)
                        self.ai_opponent_button.AI(False)
                        self.player_opponent_button.player(True)
                        print("Clicked player_opponent_button")
                    if self.standard_mode_button.graphic.collidepoint(pos):
                        self.mode = "standard"
                        self.standard_mode_button.stanard(True)
                        self.swap2_mode_button.swap2()
                        print("Clicked standard_mode_button")
                    if self.swap2_mode_button.graphic.collidepoint(pos):
                        self.mode = "swap2"
                        self.standard_mode_button.stanard()
                        self.swap2_mode_button.swap2(True)
                        print("Clicked swap2_mode_button")
                    pygame.display.update()

                    print("Player 1:", self.player1.name)
                    print("Player 2:", self.player2.name)
                    print("On move:", self.on_move.name)
                    print("Mode:", self.mode)

    def ai_move(self):
        best_move = self.ai.play_best(self.played_moves)
        print(best_move[0], " x ", best_move[1])
        self.make_move(best_move[0], best_move[1])
        if self.arbiter.checkBoardState(self.move_number, self.on_move.name):
            self.run = False
        self.next_turn()
        pygame.display.update()

    def next_turn(self):
        if self.on_move == self.player1:
            self.on_move = self.player2
            if self.on_move.get_stone_color()==WHITE:
                self.on_move_gui.white(self.on_move.name)
            else:
                self.on_move_gui.black(self.on_move.name)
        elif self.on_move == self.player2:
            self.on_move = self.player1
            if self.on_move.get_stone_color() == WHITE:
                self.on_move_gui.white(self.on_move.name)
            else:
                self.on_move_gui.black(self.on_move.name)

    def make_move(self, i, j):
        print("Ruch numer:", self.move_number)
        if self.on_move.get_stone_color() == WHITE:
            self.board_gui[i][j].white_stone(i, j)
            self.board[i][j] = WHITE
        else:
            self.board_gui[i][j].black_stone(i, j)
            self.board[i][j] = BLACK
        self.move_number += 1
        self.played_moves.add((i, j))
        self.ai.add_neighbours_squares(i, j, 0, self.played_moves)

    def playgame(self):
        pass

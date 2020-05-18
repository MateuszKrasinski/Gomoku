import sys
import pygame
import gui
from check_board_state import CheckBoardState
from ai import AI

BOARDSIZE = 15


class Player():
    def __init__(self, name_="Gracz", stone_="white"):
        self.name = name_
        self.stone_color = stone_

    def get_stone_color(self):
        return str(self.stone_color)

    def stone_white(self):
        self.stone_color = "white"

    def stone_black(self):
        self.stone_color = "black"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Game:
    def __init__(self):
        self.run = True
        self.moveNumber = 0
        gui.Background()
        self.board = [["_" for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.b = [[gui.Square() for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.buttton_new_game = gui.Button(0, "New Game")
        self.buttton_menu = gui.Button(1, "Menu")
        self.arbiter = CheckBoardState(self.board)
        self.ai = AI(self.board, self.moveNumber)
        self.played_moves = set()
        self.player1 = Player("Gracz1", "white")
        self.player2 = Player("AI", "black")
        self.on_move = self.player1
        self.on_move_gui = gui.OnMove()
        self.on_move_gui.white(self.on_move.name)

        self.b1 = gui.ChooseColor(0)
        self.b2 = gui.ChooseColor(1)
        self.c1 = gui.ChooseOpponent(0)
        self.c2 = gui.ChooseOpponent(1)
        self.m1 = gui.ChooseMode(0)
        self.m2 = gui.ChooseMode(1)
        self.mode = "standard"

    def menu(self):
        self.b1.white()
        self.b2.black()
        self.c1.AI()
        self.c2.player()
        self.m1.stanard()
        self.m2.swap2()
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.buttton_new_game.graphic.collidepoint(pos):
                        run = False
                        return self.player1, self.player2, self.on_move, self.mode
                    if self.b1.rect.collidepoint(pos):
                        print("Clicked white")
                        self.on_move = self.player1
                    if self.b2.rect.collidepoint(pos):
                        print("Clicked black")
                        self.on_move = self.player2
                    if self.c1.graphic.collidepoint(pos):
                        print("Clicked c1")
                        self.player2.set_name("AI")
                    if self.c2.graphic.collidepoint(pos):
                        self.player2.set_name("Gracz2")
                        print("Clicked c2")
                    if self.m1.rect.collidepoint(pos):
                        self.mode = "standard"
                        print("Clicked m1")
                    if self.m2.rect.collidepoint(pos):
                        self.mode = "swap2"
                        print("Clicked m2")

                    print("Player 1:", self.player1.name)
                    print("Player 2:", self.player2.name)
                    print("On move:", self.on_move.name)
                    print("MOde:", self.mode)
    def ai_move(self):
        best_move = self.ai.play_best(self.played_moves)
        print(best_move[0]," x ",best_move[1])
        self.make_move(best_move[0], best_move[1])
        if self.arbiter.checkBoardState(self.moveNumber, self.on_move.name):
            self.run = False
        self.next_turn()
        pygame.display.update()

    def next_turn(self):
        if self.on_move == self.player1:
            self.on_move = self.player2
            self.on_move_gui.black(self.on_move.name)
        elif self.on_move == self.player2:
            self.on_move = self.player1
            self.on_move_gui.white(self.on_move.name)

    def make_move(self, i, j):
        print("Ruch numer:", self.moveNumber)
        if self.on_move.get_stone_color() == "white":
            self.b[i][j].whiteSquare(i, j)
            self.board[i][j] = "white"
        else:
            self.b[i][j].blackSquare(i, j)
            self.board[i][j] = "black"
        self.moveNumber += 1
        self.played_moves.add((i, j))
        self.ai.add_neighbours_squares(i, j, 0, self.played_moves)

    def playgame(self):
        pass

import pygame, sys
import GUI
from  CheckBoardState import CheckBoardState
from AI import AI
BOARDSIZE=15
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
        GUI.Background()
        self.board=[["_" for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.b = GUI.Board()
        self.buttonNewGame=GUI.Button(0, "New Game")
        self.buttonSettings=GUI.Button(1, "Menu")
        self.arbiter=CheckBoardState(self.board)
        self.ai=AI(self.board,self.moveNumber)
        self.playedMoves=set()
        self.player1=Player("Gracz1","white")
        self.player2=Player("AI","black")
        self.onMove = self.player1
        self.onMoveGUI = GUI.OnMove()
        self.onMoveGUI.white(self.onMove.name)

        self.b1 = GUI.ChooseColor(0)
        self.b2 = GUI.ChooseColor(1)
        self.c1 = GUI.ChooseOpponent(0)
        self.c2 = GUI.ChooseOpponent(1)
        self.m1 = GUI.ChooseMode(0)
        self.m2 = GUI.ChooseMode(1)
        self.mode="standard"
    def Menu(self):
        self.b1.white()
        self.b2.black()
        self.c1.AI()
        self.c2.player()
        self.m1.stanard()
        self.m2.swap2()
        pygame.display.update()
        run=True
        while(run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.buttonNewGame.graphic.collidepoint(pos):
                        run=False
                        return self.player1,self.player2,self.onMove,self.mode
                    if self.b1.rect.collidepoint(pos):
                        print("Clicked white")
                        self.onMove=self.player1
                    if self.b2.rect.collidepoint(pos):
                        print("Clicked black")
                        self.onMove=self.player2
                    if self.c1.graphic.collidepoint(pos):
                        print("Clicked c1")
                        self.player2.set_name("AI")
                    if self.c2.graphic.collidepoint(pos):
                        self.player2.set_name("Gracz2")
                        print("Clicked c2")
                    if self.m1.rect.collidepoint(pos):
                        self.mode="standard"
                        print("Clicked m1")
                    if self.m2.rect.collidepoint(pos):
                        self.mode="swap2"
                        print("Clicked m2")

                    print("Player 1:", self.player1.name)
                    print("Player 2:", self.player2.name)
                    print("On move:", self.onMove.name)
                    print("MOde:", self.mode)

    def nextTurn(self):
        if self.onMove==self.player1:
            self.onMove=self.player2
            self.onMoveGUI.black(self.onMove.name)
        elif self.onMove==self.player2:
            self.onMove=self.player1
            self.onMoveGUI.white(self.onMove.name)
    def makeMove(self, i, j):
        print("Ruch numer:",self.moveNumber)
        if self.onMove.get_stone_color() == "white":
            self.b.square[i][j].whiteSquare(i, j)
            self.board[i][j]="white"
        else:
            self.b.square[i][j].blackSquare(i, j)
            self.board[i][j]="black"
        self.moveNumber += 1
        self.playedMoves.add((i,j))
        self.ai.addNeighboursSquares(i, j, 0,self.playedMoves)




    def playgame(self):
        pass
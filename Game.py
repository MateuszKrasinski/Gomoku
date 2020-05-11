import pygame, sys
import board
from  CheckBoardState import CheckBoardState
from Globals import BOARDSIZE, screen
from AI import AI
from Player import Player


class Game:
    def __init__(self):
        self.run = True
        self.moveNumber = 0
        board.Background()
        self.b = board.Board()
        self.buttonNewGame=board.Button(0,"vs Player")
        self.buttonSettings=board.Button(1,"vs AI")
        self.arbiter=CheckBoardState(self.b)
        self.ai=AI(self.b,self.moveNumber)
        self.onMoveGUI=board.OnMove()
        self.onMoveGUI.white()
        self.playedMoves=set()
        self.player1=Player("Gracz1","white")
        self.player2=Player("Gracz2","black")
        self.onMove = self.player1

    def makeMove(self, i, j):
        print("Ruch numer:",self.moveNumber)
        if self.onMove.get_stone_color() == "white":
            self.b.square[i][j].whiteSquare(i, j)
            self.b.square[i][j].value = "white"
            self.onMoveGUI.black()
        else:
            self.b.square[i][j].blackSquare(i, j)
            self.b.square[i][j].value = "black"
            self.onMove = "white"
            self.onMoveGUI.white()
        if self.onMove==self.player1:
            self.onMove=self.player2
        else:
            self.onMove=self.player1
        self.moveNumber += 1
        self.playedMoves.add((i,j))
        self.ai.addNeighboursSquares(i, j, 0,self.playedMoves)


    def playgame(self):
        pass
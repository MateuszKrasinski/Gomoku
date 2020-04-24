import pygame
import Globals


class Square:
    margin = Globals.squareMargin
    width = Globals.squareWidth
    left = int(Globals.screenWidth / 2 - Globals.BOARDSIZE * (width / 2 + margin))
    up = int(Globals.screenHeight / 2 - Globals.BOARDSIZE * (width / 2 + margin))
    numberOfNeighboursWhite = 0
    numberOfNeighboursBlack = 0
    value = "_"
    graphic = pygame.draw.rect(Globals.screen, (0, 255, 255),
                               (width + margin + left, width + margin + up, width, width))

    def emptySquare(self, j, i):
        self.graphic = pygame.draw.rect(Globals.screen, (102, 51, 0),
                                        (i * self.width + i * self.margin + self.left,
                                         j * self.width + j * self.margin + self.up, self.width, self.width))

    def whiteSquare(self, j, i):
        self.graphic = pygame.draw.circle(Globals.screen, (255, 255, 255),
                                          (i * self.width + i * self.margin + self.left + self.width // 2,
                                           j * self.width + j * self.margin + self.up + self.width // 2),
                                          self.width // 2)

    def blackSquare(self, j, i):
        self.graphic = pygame.draw.circle(Globals.screen, (0, 0, 0),
                                          (i * self.width + i * self.margin + self.left + self.width // 2,
                                           j * self.width + j * self.margin + self.up + self.width // 2),
                                          self.width // 2)


class Board:
    def __init__(self):
        self.square = [[Square() for i in range(Globals.BOARDSIZE)] for j in range(Globals.BOARDSIZE)]

    def draw(self):
        for i in range(0, Globals.BOARDSIZE):
            for j in range(0, Globals.BOARDSIZE):
                self.square[i][j].emptySquare(i, j)

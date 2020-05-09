import pygame
from Globals import screen,screenHeight,screenWidth,BOARDSIZE,squareWidth,squareMargin
pygame.init()
pygame.display.set_caption('Gomoku')
font = pygame.font.Font("freesansbold.ttf", 26)
def messageButton(what, x, y):
    font = pygame.font.Font("freesansbold.ttf", 30)
    text = font.render(what, True, (0, 0, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
def message(what, x, y):
    font = pygame.font.Font("freesansbold.ttf", 26)
    text = font.render(what, True, (0, 128, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
def messageResult(what, x, y):
    font2 = pygame.font.Font("freesansbold.ttf", 60)
    text = font.render(what, True, (0, 128, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
def messageWin():
    messageResult("Wygrana", int(screenWidth / 2), int(screenHeight / 3 / 5))
    #self.run = False
    pygame.display.update()

def messageDraw():
    messageResult("Remis", int(screenWidth / 2), int(screenHeight / 1 / 5))
    #self.run = False
    pygame.display.update()
class Square:
    margin = squareMargin
    width = squareWidth
    left = int(screenWidth / 2 - BOARDSIZE * (width / 2 + margin))
    up = int(screenHeight / 2 - BOARDSIZE * (width / 2 + margin))
    numberOfNeighboursWhite = 0
    numberOfNeighboursBlack = 0
    value = "_"
    graphic = pygame.draw.rect(screen, (0, 255, 255),
                               (width + margin + left, width + margin + up, width, width))

    def emptySquare(self, j, i):
        self.graphic = pygame.draw.rect(screen, (102, 51, 0),
                                        (i * self.width + i * self.margin + self.left,
                                         j * self.width + j * self.margin + self.up, self.width, self.width))

    def whiteSquare(self, j, i):
        self.graphic = pygame.draw.circle(screen, (255, 255, 255),
                                          (i * self.width + i * self.margin + self.left + self.width // 2,
                                           j * self.width + j * self.margin + self.up + self.width // 2),
                                          self.width // 2)

    def blackSquare(self, j, i):
        self.graphic = pygame.draw.circle(screen, (0, 0, 0),
                                          (i * self.width + i * self.margin + self.left + self.width // 2,
                                           j * self.width + j * self.margin + self.up + self.width // 2),
                                          self.width // 2)
class Board:
    def __init__(self):
        self.onMove=OnMove()
        self.button = Button()
        self.square = [[Square() for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        self.margin = squareMargin
        self.width = squareWidth
        self.left = int(screenWidth / 2 - BOARDSIZE * (self.width / 2 + self.margin))
        self.up = int(screenHeight / 2 - BOARDSIZE * (self.width / 2 + self.margin))
    def draw(self):
        for i in range(BOARDSIZE):
            message("{}".format(i), self.left +15 + i * 33, self.up -30)
        for i in range(0, BOARDSIZE):
            for j in range(0, BOARDSIZE):
                self.square[i][j].emptySquare(i, j)
            message("{}".format(i),self.left-30,self.up+15+i*33)
            self.button.draw()
            self.onMove

class Button:
    def __init__(self):
        self.graphic=pygame.Rect(640,350,150,75)
    def draw(self):
        pygame.draw.rect(screen,(102, 51, 0),self.graphic)
        messageButton("Restart", self.graphic.center[0],self.graphic.center[1])
class OnMove:
    def __init__(self):
        self.graphic = pygame.draw.rect(screen, (102, 51, 0), (700, 200, 60, 60))
    def black(self):
        self.graphic=pygame.draw.circle(screen, (0, 0, 0), (700 + 30, 200 + 30), 30)
    def white(self):
        self.graphic=pygame.draw.circle(screen, (255, 255, 255), (700 + 30, 200 + 30), 30)



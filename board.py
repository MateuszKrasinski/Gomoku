import pygame
from Globals import screen,screenHeight,screenWidth,BOARDSIZE,squareWidth,squareMargin
pygame.init()
pygame.display.set_caption('Gomoku')
font = pygame.font.Font("freesansbold.ttf", 26)
boardWidth=(BOARDSIZE * (squareWidth + squareMargin)+2*squareMargin)
leftMargin=int(screenWidth - (BOARDSIZE * (squareWidth + squareMargin)))//4
topMargin= int(screenHeight - BOARDSIZE * (squareWidth + squareMargin))//2
rightMargin=screenWidth-boardWidth-leftMargin
def messageButton(what, x, y):
    font = pygame.font.SysFont("Arial",14,1)
    text = font.render(what, True, (0, 0, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
def message(what, x, y):
    font = pygame.font.SysFont("Arial",14,1)
    text = font.render(what, True, (0, 0, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
def messageResult(what, x, y):
    font = pygame.font.SysFont("Arial", 40, 1)
    text = font.render(what, True, (0, 0, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
def messageWin(name):
    rect=pygame.Rect(leftMargin,4,boardWidth,topMargin+6)
    border=pygame.Rect(leftMargin-3,1,boardWidth+6,topMargin+12)
    pygame.draw.rect(screen,(0, 0, 0),border)
    pygame.draw.rect(screen,(88, 61, 0),rect)
    messageResult(name+" WINS!", rect.center[0], rect.center[1])
    #self.run = False
    pygame.display.update()

def messageDraw():
    messageResult("Remis", int(screenWidth / 2), int(screenHeight / 1 / 5))
    #self.run = False
    pygame.display.update()
class Square:
    value = "_"
    rect=pygame.Rect(squareMargin + squareMargin + leftMargin, squareWidth + squareMargin + topMargin, squareWidth, squareWidth)
    graphic = pygame.draw.rect(screen, (0, 255, 255),rect)

    def emptySquare(self, j, i):
        pygame.draw.rect(screen, (0, 0, 0),
                         (i * squareWidth + i * squareMargin + leftMargin-2,
                          j * squareWidth + j * squareMargin + topMargin-2+15, squareWidth+4, squareWidth+4))
        self.graphic = pygame.draw.rect(screen, (133, 87, 35),
                                        (i * squareWidth + i * squareMargin + leftMargin,
                                         j * squareWidth + j * squareMargin+15 + topMargin, squareWidth, squareWidth))

    def whiteSquare(self, j, i):
        self.graphic = pygame.draw.circle(screen, (255, 255, 255),
                                          (i * squareWidth + i * squareMargin + leftMargin + squareWidth // 2,
                                           j * squareWidth + j * squareMargin+15 + topMargin + squareWidth // 2),
                                          squareWidth // 2)

    def blackSquare(self, j, i):
        self.graphic = pygame.draw.circle(screen, (0, 0, 0),
                                          (i * squareWidth + i * squareMargin + leftMargin + squareWidth // 2,
                                           j * squareWidth + j * squareMargin+15 + topMargin + squareWidth // 2),
                                          squareWidth // 2)
class Board:
    def __init__(self):
        self.onMove=OnMove()
        self.button = Button()
        self.square = [[Square() for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
    def draw(self):
        for i in range(0, BOARDSIZE):
            for j in range(0, BOARDSIZE):
                self.square[i][j].emptySquare(i, j)
            message("{}".format(i),leftMargin-squareWidth//3-2,topMargin+squareWidth//2+i*(squareWidth+squareMargin)+15)
        for i in range(BOARDSIZE):
            message("{}".format(i), leftMargin + squareWidth//2 + i * (squareWidth+squareMargin), boardWidth+topMargin+20)

class Button:
    def __init__(self,next=0,name="Button"):
        print(next*squareWidth)
        self.border=pygame.Rect(screenWidth - rightMargin + rightMargin // 20-2,screenHeight//3+(next*(squareWidth+2*squareMargin))-2,rightMargin*9//10+4,4//4*squareWidth+4)
        self.graphic=pygame.Rect(screenWidth - rightMargin + rightMargin // 20,screenHeight//3+(next*(squareWidth+2*squareMargin)),rightMargin*9//10,4//3*squareWidth)
        pygame.draw.rect(screen, (0, 0, 0), self.border)
        pygame.draw.rect(screen, (88, 61, 0), self.graphic)
        print("szerokosc:",rightMargin*9//10)
        print("Wysokosc:",squareWidth)
        messageButton(name, self.graphic.center[0], self.graphic.center[1])

class OnMove:
    def __init__(self):
        self.center=(boardWidth+(screenHeight-boardWidth)//2+screenHeight/2)
        self.graphic = pygame.Rect(screenWidth - rightMargin//4, screenHeight / 3.5, rightMargin * 1 // 10, rightMargin * 1 // 10)
        message("Turn:", screenWidth - rightMargin + rightMargin // 4,self.graphic.center[1])
        print(screenWidth - rightMargin + rightMargin,"Ss")
        pygame.draw.rect(screen, (129,108,91), self.graphic)
    def black(self):
        self.graphic=pygame.draw.circle(screen, (0, 0, 0),self.graphic.center,squareWidth/2.5)
    def white(self):
        self.graphic = pygame.draw.circle(screen, (255, 255, 255), self.graphic.center, squareWidth/2.5 )
        #self.graphic=pygame.draw.circle(screen, (255, 255, 255), (700 + 30, 200 + 30), 30)

class ChooseColor:
    def __init__(self):
        self.graphic = pygame.draw.rect(screen, (102, 51, 0), (550, 50, 30, 30))
        self.graphic=pygame.draw.circle(screen, (255, 255, 255), (550 + 15, 50 + 15), 15)
def startMenu():
    screen.fill((0, 0, 0))

class Background():
    def __init__(self):
        screen.fill((133, 87, 35))

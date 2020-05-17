import pygame

BOARDSIZE = 15
squareWidth = 30
squareMargin = 2
screenWidth = 600
screenHeight = 545
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.init()
pygame.display.set_caption('Gomoku')
font = pygame.font.Font("freesansbold.ttf", 26)
boardWidth = (BOARDSIZE * (squareWidth + squareMargin) + 2 * squareMargin)
leftMargin = int(screenWidth - (BOARDSIZE * (squareWidth + squareMargin))) // 4
topMargin = int(screenHeight - BOARDSIZE * (squareWidth + squareMargin)) // 2
rightMargin = screenWidth - boardWidth - leftMargin


def messageButton(what, x, y):
    font = pygame.font.SysFont("Arial", 14, 1)
    text = font.render(what, True, (0, 0, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def message(what, x, y):
    font = pygame.font.SysFont("Arial", 14, 1)
    text = font.render(what, True, (0, 0, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def messageResult(what, x, y):
    font = pygame.font.SysFont("Arial", 40, 1)
    text = font.render(what, True, (0, 0, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def messageWin(name):
    rect = pygame.Rect(leftMargin, 4, boardWidth, topMargin + 6)
    border = pygame.Rect(leftMargin - 3, 1, boardWidth + 6, topMargin + 12)
    pygame.draw.rect(screen, (0, 0, 0), border)
    pygame.draw.rect(screen, (88, 61, 0), rect)
    messageResult(name + " WINS!", rect.center[0], rect.center[1])
    pygame.display.update()


def messageDraw():
    messageResult("Remis", int(screenWidth / 2), int(screenHeight / 1 / 5))
    pygame.display.update()


class Square:
    rect = pygame.Rect(squareMargin + squareMargin + leftMargin,
                       squareWidth + squareMargin + topMargin, squareWidth,
                       squareWidth)
    graphic = pygame.draw.rect(screen, (0, 255, 255), rect)

    def emptySquare(self, j, i):
        pygame.draw.rect(screen, (0, 0, 0),
                         (i * squareWidth + i * squareMargin + leftMargin - 2,
                          j * squareWidth + j * squareMargin + topMargin - 2 + 15,
                          squareWidth + 4, squareWidth + 4))
        self.graphic = pygame.draw.rect(screen, (133, 87, 35),
                                        (
                                        i * squareWidth + i * squareMargin + leftMargin,
                                        j * squareWidth + j * squareMargin + 15 + topMargin,
                                        squareWidth, squareWidth))

    def whiteSquare(self, j, i):
        self.graphic = pygame.draw.circle(screen, (255, 255, 255),
                                          (
                                          i * squareWidth + i * squareMargin + leftMargin + squareWidth // 2,
                                          j * squareWidth + j * squareMargin + 15 + topMargin + squareWidth // 2),
                                          squareWidth // 2)

    def blackSquare(self, j, i):
        self.graphic = pygame.draw.circle(screen, (0, 0, 0),
                                          (
                                          i * squareWidth + i * squareMargin + leftMargin + squareWidth // 2,
                                          j * squareWidth + j * squareMargin + 15 + topMargin + squareWidth // 2),
                                          squareWidth // 2)


class Board:
    def __init__(self):
        self.square = [[Square() for i in range(BOARDSIZE)] for j in
                       range(BOARDSIZE)]

    def draw(self):
        for i in range(0, BOARDSIZE):
            for j in range(0, BOARDSIZE):
                self.square[i][j].emptySquare(i, j)
            message("{}".format(i), leftMargin - squareWidth // 3 - 2,
                    topMargin + squareWidth // 2 + i * (
                                squareWidth + squareMargin) + 15)
        for i in range(BOARDSIZE):
            message("{}".format(i), leftMargin + squareWidth // 2 + i * (
                        squareWidth + squareMargin),
                    boardWidth + topMargin + 20)


class OnMove():
    def __init__(self):
        self.center = (boardWidth + (
                    screenHeight - boardWidth) // 2 + screenHeight / 2)
        self.graphic = pygame.Rect(screenWidth - 70, screenHeight / 3.5,
                                   rightMargin * 1 // 10, rightMargin * 1 // 10)
        message("Turn:", self.graphic.center[0], self.graphic.center[1] - 20)
        pygame.draw.rect(screen, (0, 108, 91), self.graphic)
        self.graphic1 = pygame.Rect(screenWidth - rightMargin,
                                    screenHeight / 3.5, squareWidth * 2.8,
                                    squareWidth / 2)

    def black(self, name):
        pygame.draw.rect(screen, (133, 87, 35), self.graphic1)
        message(name, screenWidth - rightMargin + rightMargin // 4 + 5,
                self.graphic1.center[1])
        self.graphic = pygame.draw.circle(screen, (0, 0, 0), (
        self.graphic1.midright[0] - squareWidth / 2 - 2,
        self.graphic1.midright[1] - 2), squareWidth / 2.5)
        pygame.display.update()

    def white(self, name):
        pygame.draw.rect(screen, (133, 87, 35), self.graphic1)
        message(name, screenWidth - rightMargin + rightMargin // 4 + 5,
                self.graphic1.center[1])
        self.graphic = pygame.draw.circle(screen, (255, 255, 255), (
        self.graphic1.midright[0] - squareWidth / 2 - 2,
        self.graphic1.midright[1] - 2), squareWidth / 2.5)
        pygame.display.update()


class Button:
    def __init__(self, next=0, name="Button"):
        self.border = pygame.Rect(
            screenWidth - rightMargin + rightMargin // 20 - 2,
            screenHeight // 3 + (next * (squareWidth + 2 * squareMargin)) - 2,
            rightMargin * 9 // 10 + 4,
            4 // 4 * squareWidth + 4)
        self.graphic = pygame.Rect(
            screenWidth - rightMargin + rightMargin // 20,
            screenHeight // 3 + (next * (squareWidth + 2 * squareMargin)),
            rightMargin * 9 // 10,
            4 // 3 * squareWidth)
        pygame.draw.rect(screen, (0, 0, 0), self.border)
        pygame.draw.rect(screen, (88, 61, 0), self.graphic)
        messageButton(name, self.graphic.center[0], self.graphic.center[1])


class ChooseColor:
    def __init__(self, number):
        self.number = number
        self.rect = pygame.Rect(screenWidth / 4.5 + number * 30 - 20, 10, 30,
                                30)
        self.border = pygame.Rect(screenWidth / 4.5 + number * 30 - 2 - 20,
                                  10 - 2, 30 + 4, 30 + 4)

    def black(self):
        pygame.draw.rect(screen, (0, 0, 0), self.border)
        pygame.draw.rect(screen, (88, 61, 0), self.rect)
        pygame.draw.circle(screen, (0, 0, 0), (self.rect.center), 12)

    def white(self):
        message("Choose color:", leftMargin + 25, topMargin - 5)
        pygame.draw.rect(screen, (0, 0, 0), self.border)
        pygame.draw.rect(screen, (88, 61, 0), self.rect)
        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, 12)


class ChooseOpponent():
    def __init__(self, number):
        self.number = number
        self.graphic = pygame.Rect(screenWidth / 2 + number * 50 - 25, 10, 60,
                                   30)
        self.border = pygame.Rect(screenWidth / 2 + number * 50 - 25 - 2,
                                  10 - 2, 60 + 4, 30 + 4)

    def AI(self):
        pygame.draw.rect(screen, (0, 0, 0), self.border)
        pygame.draw.rect(screen, (88, 61, 0), self.graphic)
        message("Opponent:", screenWidth / 2 - 70, topMargin - 5)
        message("AI", self.graphic.center[0] - 5, self.graphic.center[1])

    def player(self):
        pygame.draw.rect(screen, (0, 0, 0), self.border)
        pygame.draw.rect(screen, (88, 61, 0), self.graphic)
        message("PLAYER", self.graphic.center[0], self.graphic.center[1])


class ChooseMode():
    def __init__(self, number):
        self.number = number
        self.rect = pygame.Rect(boardWidth - 30 + number * 70, 10, 70, 30)
        self.border = pygame.Rect(boardWidth - 30 + number * 70 - 2, 10 - 2,
                                  70 + 4, 30 + 4)

    def stanard(self):
        self.border = pygame.draw.rect(screen, (0, 0, 0), self.border)
        self.graphic = pygame.draw.rect(screen, (88, 61, 0), self.rect)
        message("Rules:", boardWidth - 60, topMargin - 5)
        message("standard", self.graphic.center[0], self.graphic.center[1])

    def swap2(self):
        self.border = pygame.draw.rect(screen, (0, 0, 0), self.border)
        self.graphic = pygame.draw.rect(screen, (88, 61, 0), self.rect)
        message("swap2", self.graphic.center[0], self.graphic.center[1])


class Background():
    def __init__(self):
        screen.fill((133, 87, 35))

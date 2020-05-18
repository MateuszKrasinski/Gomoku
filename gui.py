import pygame

BOARDSIZE = 15
SQUARE_WIDTH = 30
SQUARE_MARGIN = 2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 545
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()
pygame.display.set_caption('Gomoku')
font = pygame.font.Font("freesansbold.ttf", 26)
boardWidth = (BOARDSIZE * (SQUARE_WIDTH + SQUARE_MARGIN) + 2 * SQUARE_MARGIN)
LEFT_MARGIN = int(SCREEN_WIDTH - (BOARDSIZE * (SQUARE_WIDTH + SQUARE_MARGIN))) // 4
TOP_MARGIN = int(SCREEN_HEIGHT - BOARDSIZE * (SQUARE_WIDTH + SQUARE_MARGIN)) // 2
RIGHT_MARGIN = SCREEN_WIDTH - boardWidth - LEFT_MARGIN


def messageButton(what, x, y):
    font = pygame.font.SysFont("Arial", 14, 1)
    text = font.render(what, True, (0, 0, 0))
    SCREEN.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def message(what, x, y):
    font = pygame.font.SysFont("Arial", 14, 1)
    text = font.render(what, True, (0, 0, 0))
    SCREEN.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def messageResult(what, x, y):
    font = pygame.font.SysFont("Arial", 40, 1)
    text = font.render(what, True, (0, 0, 0))
    SCREEN.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def messageWin(name):
    rect = pygame.Rect(LEFT_MARGIN, 4, boardWidth, TOP_MARGIN + 6)
    border = pygame.Rect(LEFT_MARGIN - 3, 1, boardWidth + 6, TOP_MARGIN + 12)
    pygame.draw.rect(SCREEN, (0, 0, 0), border)
    pygame.draw.rect(SCREEN, (88, 61, 0), rect)
    messageResult(name + " WINS!", rect.center[0], rect.center[1])
    pygame.display.update()


def messageDraw():
    messageResult("Remis", int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 1 / 5))
    pygame.display.update()


class Square:
    rect = pygame.Rect(SQUARE_MARGIN + SQUARE_MARGIN + LEFT_MARGIN,
                       SQUARE_WIDTH + SQUARE_MARGIN + TOP_MARGIN, SQUARE_WIDTH,
                       SQUARE_WIDTH)
    graphic = pygame.draw.rect(SCREEN, (0, 255, 255), rect)

    def emptySquare(self, j, i):
        pygame.draw.rect(SCREEN, (0, 0, 0),
                         (i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN - 2,
                          j * SQUARE_WIDTH + j * SQUARE_MARGIN + TOP_MARGIN - 2 + 15,
                          SQUARE_WIDTH + 4, SQUARE_WIDTH + 4))
        self.graphic = pygame.draw.rect(SCREEN, (133, 87, 35),
                                        (
                                            i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN,
                                            j * SQUARE_WIDTH + j * SQUARE_MARGIN + 15 + TOP_MARGIN,
                                            SQUARE_WIDTH, SQUARE_WIDTH))

    def whiteSquare(self, j, i):
        self.graphic = pygame.draw.circle(SCREEN, (255, 255, 255),
                                          (
                                              i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN + SQUARE_WIDTH // 2,
                                              j * SQUARE_WIDTH + j * SQUARE_MARGIN + 15 + TOP_MARGIN + SQUARE_WIDTH // 2),
                                          SQUARE_WIDTH // 2)

    def blackSquare(self, j, i):
        self.graphic = pygame.draw.circle(SCREEN, (0, 0, 0),
                                          (
                                              i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN + SQUARE_WIDTH // 2,
                                              j * SQUARE_WIDTH + j * SQUARE_MARGIN + 15 + TOP_MARGIN + SQUARE_WIDTH // 2),
                                          SQUARE_WIDTH // 2)


def draw_board(square):
    for i in range(0, BOARDSIZE):
        for j in range(0, BOARDSIZE):
            square[i][j].emptySquare(i, j)
        message("{}".format(i), LEFT_MARGIN - SQUARE_WIDTH // 3 - 2,
                TOP_MARGIN + SQUARE_WIDTH // 2 + i * (
                        SQUARE_WIDTH + SQUARE_MARGIN) + 15)
    for i in range(BOARDSIZE):
        message("{}".format(i), LEFT_MARGIN + SQUARE_WIDTH // 2 + i * (
                SQUARE_WIDTH + SQUARE_MARGIN),
                boardWidth + TOP_MARGIN + 20)
    pygame.display.update()



class OnMove():
    def __init__(self):
        self.center = (boardWidth + (
                SCREEN_HEIGHT - boardWidth) // 2 + SCREEN_HEIGHT / 2)
        self.graphic = pygame.Rect(SCREEN_WIDTH - 70, SCREEN_HEIGHT / 3.5,
                                   RIGHT_MARGIN * 1 // 10, RIGHT_MARGIN * 1 // 10)
        message("Turn:", self.graphic.center[0], self.graphic.center[1] - 20)
        pygame.draw.rect(SCREEN, (0, 108, 91), self.graphic)
        self.graphic1 = pygame.Rect(SCREEN_WIDTH - RIGHT_MARGIN,
                                    SCREEN_HEIGHT / 3.5, SQUARE_WIDTH * 2.8,
                                    SQUARE_WIDTH / 2)

    def black(self, name):
        pygame.draw.rect(SCREEN, (133, 87, 35), self.graphic1)
        message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 5,
                self.graphic1.center[1])
        self.graphic = pygame.draw.circle(SCREEN, (0, 0, 0), (
            self.graphic1.midright[0] - SQUARE_WIDTH / 2 - 2,
            self.graphic1.midright[1] - 2), SQUARE_WIDTH / 2.5)
        pygame.display.update()

    def white(self, name):
        pygame.draw.rect(SCREEN, (133, 87, 35), self.graphic1)
        message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 5,
                self.graphic1.center[1])
        self.graphic = pygame.draw.circle(SCREEN, (255, 255, 255), (
            self.graphic1.midright[0] - SQUARE_WIDTH / 2 - 2,
            self.graphic1.midright[1] - 2), SQUARE_WIDTH / 2.5)
        pygame.display.update()


class Button:
    def __init__(self, next=0, name="Button"):
        self.border = pygame.Rect(
            SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 20 - 2,
            SCREEN_HEIGHT // 3 + (next * (SQUARE_WIDTH + 2 * SQUARE_MARGIN)) - 2,
            RIGHT_MARGIN * 9 // 10 + 4,
            4 // 4 * SQUARE_WIDTH + 4)
        self.graphic = pygame.Rect(
            SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 20,
            SCREEN_HEIGHT // 3 + (next * (SQUARE_WIDTH + 2 * SQUARE_MARGIN)),
            RIGHT_MARGIN * 9 // 10,
            4 // 3 * SQUARE_WIDTH)
        pygame.draw.rect(SCREEN, (0, 0, 0), self.border)
        pygame.draw.rect(SCREEN, (88, 61, 0), self.graphic)
        messageButton(name, self.graphic.center[0], self.graphic.center[1])


class ChooseColor:
    def __init__(self, number):
        self.number = number
        self.rect = pygame.Rect(SCREEN_WIDTH / 4.5 + number * 30 - 20, 10, 30,
                                30)
        self.border = pygame.Rect(SCREEN_WIDTH / 4.5 + number * 30 - 2 - 20,
                                  10 - 2, 30 + 4, 30 + 4)

    def black(self):
        pygame.draw.rect(SCREEN, (0, 0, 0), self.border)
        pygame.draw.rect(SCREEN, (88, 61, 0), self.rect)
        pygame.draw.circle(SCREEN, (0, 0, 0), (self.rect.center), 12)

    def white(self):
        message("Choose color:", LEFT_MARGIN + 25, TOP_MARGIN - 5)
        pygame.draw.rect(SCREEN, (0, 0, 0), self.border)
        pygame.draw.rect(SCREEN, (88, 61, 0), self.rect)
        pygame.draw.circle(SCREEN, (255, 255, 255), self.rect.center, 12)


class ChooseOpponent():
    def __init__(self, number):
        self.number = number
        self.graphic = pygame.Rect(SCREEN_WIDTH / 2 + number * 50 - 25, 10, 60,
                                   30)
        self.border = pygame.Rect(SCREEN_WIDTH / 2 + number * 50 - 25 - 2,
                                  10 - 2, 60 + 4, 30 + 4)

    def AI(self):
        pygame.draw.rect(SCREEN, (0, 0, 0), self.border)
        pygame.draw.rect(SCREEN, (88, 61, 0), self.graphic)
        message("Opponent:", SCREEN_WIDTH / 2 - 70, TOP_MARGIN - 5)
        message("AI", self.graphic.center[0] - 5, self.graphic.center[1])

    def player(self):
        pygame.draw.rect(SCREEN, (0, 0, 0), self.border)
        pygame.draw.rect(SCREEN, (88, 61, 0), self.graphic)
        message("PLAYER", self.graphic.center[0], self.graphic.center[1])


class ChooseMode():
    def __init__(self, number):
        self.number = number
        self.rect = pygame.Rect(boardWidth - 30 + number * 70, 10, 70, 30)
        self.border = pygame.Rect(boardWidth - 30 + number * 70 - 2, 10 - 2,
                                  70 + 4, 30 + 4)

    def stanard(self):
        self.border = pygame.draw.rect(SCREEN, (0, 0, 0), self.border)
        self.graphic = pygame.draw.rect(SCREEN, (88, 61, 0), self.rect)
        message("Rules:", boardWidth - 60, TOP_MARGIN - 5)
        message("standard", self.graphic.center[0], self.graphic.center[1])

    def swap2(self):
        self.border = pygame.draw.rect(SCREEN, (0, 0, 0), self.border)
        self.graphic = pygame.draw.rect(SCREEN, (88, 61, 0), self.rect)
        message("swap2", self.graphic.center[0], self.graphic.center[1])


class Background():
    def __init__(self):
        SCREEN.fill((133, 87, 35))

import pygame

# colors
SETTINGS_TOP_MARGIN = 10
BUTTON_COLOR = (88, 61, 0)
BOARD_COLOR = (133, 87, 35)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SELECTED_COLOR=(218,165,32)

BIG_FONT_SIZE = 40
FONT_SIZE = 14
BORDER = 2
BOARD_SIZE = 15
SQUARE_WIDTH = 30
CIRCLE_RADIUS = SQUARE_WIDTH // 2
SQUARE_MARGIN = 2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 545
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()
pygame.display.set_caption('Gomoku')
BOARD_WIDTH = int(BOARD_SIZE * (SQUARE_WIDTH + SQUARE_MARGIN) + 2 * SQUARE_MARGIN)
LEFT_MARGIN = int(SCREEN_WIDTH - (BOARD_SIZE * (SQUARE_WIDTH + SQUARE_MARGIN))) // 4
TOP_MARGIN = int(SCREEN_HEIGHT - BOARD_SIZE * (SQUARE_WIDTH + SQUARE_MARGIN)) // 2
RIGHT_MARGIN = int(SCREEN_WIDTH - BOARD_WIDTH - LEFT_MARGIN)
SETTINGS_MESSAGE_TOP_MARGIN = TOP_MARGIN - 5


def message(what, x, y, font_size):
    font = pygame.font.SysFont("Arial", font_size, 1)
    text = font.render(what, True, BLACK)
    SCREEN.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def messageWin(name):
    rect = pygame.Rect(LEFT_MARGIN, 4, BOARD_WIDTH, TOP_MARGIN + 6)
    border = pygame.Rect(LEFT_MARGIN - 3, 1, BOARD_WIDTH + 6, TOP_MARGIN + 12)
    pygame.draw.rect(SCREEN, BLACK, border)
    pygame.draw.rect(SCREEN, BUTTON_COLOR, rect)
    message(name + " WINS!", rect.center[0], rect.center[1], BIG_FONT_SIZE)
    pygame.display.update()


def messageDraw():
    message("Remis", int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 1 / 5),BIG_FONT_SIZE)
    pygame.display.update()


class Square:
    rect = pygame.Rect(SQUARE_MARGIN + SQUARE_MARGIN + LEFT_MARGIN,
                       SQUARE_WIDTH + SQUARE_MARGIN + TOP_MARGIN, SQUARE_WIDTH,
                       SQUARE_WIDTH)
    graphic = pygame.draw.rect(SCREEN, (0, 255, 255), rect)

    def empty_square(self, j, i):
        pygame.draw.rect(SCREEN, BLACK,
                         (i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN - BORDER,
                          j * SQUARE_WIDTH + j * SQUARE_MARGIN + TOP_MARGIN - BORDER + 15,
                          SQUARE_WIDTH + 2 * BORDER, SQUARE_WIDTH + 2 * BORDER))
        self.graphic = pygame.draw.rect(SCREEN, BOARD_COLOR,
                                        (
                                            i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN,
                                            j * SQUARE_WIDTH + j * SQUARE_MARGIN + SQUARE_WIDTH // 2
                                            + TOP_MARGIN, SQUARE_WIDTH, SQUARE_WIDTH))

    def white_stone(self, j, i):
        self.graphic = pygame.draw.circle(SCREEN, WHITE,
                                          (
                                              i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN +
                                              SQUARE_WIDTH // 2,
                                              j * SQUARE_WIDTH + j * SQUARE_MARGIN +
                                              SQUARE_WIDTH // 2 +
                                              TOP_MARGIN + SQUARE_WIDTH // 2),
                                          SQUARE_WIDTH // 2)

    def black_stone(self, j, i):
        self.graphic = pygame.draw.circle(SCREEN, BLACK,
                                          (
                                              i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN +
                                              SQUARE_WIDTH // 2,
                                              j * SQUARE_WIDTH + j * SQUARE_MARGIN +
                                              SQUARE_WIDTH // 2 +
                                              TOP_MARGIN + SQUARE_WIDTH // 2),
                                          SQUARE_WIDTH // 2)


def draw_board(square):
    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            square[i][j].empty_square(i, j)
        message("{}".format(i), LEFT_MARGIN - SQUARE_WIDTH // 3 - 2,
                TOP_MARGIN + SQUARE_WIDTH // 2 + i * (
                        SQUARE_WIDTH + SQUARE_MARGIN) + SQUARE_WIDTH // 2, FONT_SIZE)
    for i in range(BOARD_SIZE):
        message("{}".format(i), LEFT_MARGIN + SQUARE_WIDTH // 2 + i * (
                SQUARE_WIDTH + SQUARE_MARGIN),
                BOARD_WIDTH + TOP_MARGIN + 20, FONT_SIZE)
    pygame.display.update()


class OnMove():
    def __init__(self):
        self.graphic = pygame.Rect(SCREEN_WIDTH - 70, SCREEN_HEIGHT / 3.5,
                                   RIGHT_MARGIN * 1 // 10, RIGHT_MARGIN * 1 // 10)
        message("Turn:", self.graphic.center[0], self.graphic.center[1] - 20, FONT_SIZE)
        self.graphic1 = pygame.Rect(SCREEN_WIDTH - RIGHT_MARGIN,
                                    SCREEN_HEIGHT // 3.5, SQUARE_WIDTH * 2.8,
                                    SQUARE_WIDTH // 2)

    def black(self, name):
        pygame.draw.rect(SCREEN, BOARD_COLOR, self.graphic1)
        message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 5,
                self.graphic1.center[1], FONT_SIZE)
        self.graphic = pygame.draw.circle(SCREEN, BLACK, (
            int(self.graphic1.midright[0]) - SQUARE_WIDTH // 2 - 2,
            int(self.graphic1.midright[1]) - 2), SQUARE_WIDTH // 2.5)
        pygame.display.update()

    def white(self, name):
        pygame.draw.rect(SCREEN, BOARD_COLOR, self.graphic1)
        message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 5,
                self.graphic1.center[1], FONT_SIZE)
        self.graphic = pygame.draw.circle(SCREEN, WHITE, (
            int(self.graphic1.midright[0]) - SQUARE_WIDTH // 2 - 2,
            int(self.graphic1.midright[1] - 2)), SQUARE_WIDTH // 2.5)
        pygame.display.update()

    def change_message(self, name):
        pygame.draw.rect(SCREEN, BOARD_COLOR, (SCREEN_WIDTH - RIGHT_MARGIN,
                                               SCREEN_HEIGHT // 3.5, int(SQUARE_WIDTH * 1.7),
                                               SQUARE_WIDTH // 2))
        message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 5,
                self.graphic1.center[1], FONT_SIZE)
        pygame.display.update()


class Button:
    def __init__(self, next=0, name="Button"):
        self.button_width = RIGHT_MARGIN * 9 // 10
        self.button_height = SQUARE_WIDTH
        self.left_down_corner_x = SCREEN_WIDTH - RIGHT_MARGIN // 2 - self.button_width // 2
        self.left_down_corner_y = SCREEN_HEIGHT // 3 + (next * (SQUARE_WIDTH + 2 * SQUARE_MARGIN)) \
                                  - BORDER
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)
        pygame.draw.rect(SCREEN, BLACK, self.border)
        pygame.draw.rect(SCREEN, BUTTON_COLOR, self.graphic)
        message(name, self.graphic.center[0], self.graphic.center[1], FONT_SIZE)


class ChooseColor:
    def __init__(self, next):
        self.button_width = SQUARE_WIDTH
        self.button_height = SQUARE_WIDTH
        self.left_down_corner_x = SCREEN_WIDTH / 4.5 + next * (SQUARE_WIDTH+2*BORDER) - 20
        self.left_down_corner_y = SETTINGS_TOP_MARGIN
        self.next = next
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)

    def black(self,clicked=False):
        if clicked:
            pygame.draw.rect(SCREEN, SELECTED_COLOR, self.border)
        else:
            pygame.draw.rect(SCREEN, BLACK, self.border)
        pygame.draw.rect(SCREEN, BUTTON_COLOR, self.graphic)
        pygame.draw.circle(SCREEN, BLACK, self.graphic.center, CIRCLE_RADIUS - BORDER)

    def white(self,clicked=False):
        message("Choose color:", LEFT_MARGIN + 25, SETTINGS_MESSAGE_TOP_MARGIN, FONT_SIZE)
        if clicked:
            pygame.draw.rect(SCREEN, SELECTED_COLOR, self.border)
        else:
            pygame.draw.rect(SCREEN, BLACK, self.border)
        pygame.draw.rect(SCREEN, BUTTON_COLOR, self.graphic)
        pygame.draw.circle(SCREEN, WHITE, self.graphic.center, CIRCLE_RADIUS - BORDER)


class ChooseOpponent():
    def __init__(self, next=0):
        self.left_down_corner_x = SCREEN_WIDTH // 2 + next * 64 - 30
        self.left_down_corner_y = SETTINGS_TOP_MARGIN
        self.button_width = SQUARE_WIDTH * 2
        self.button_height = SQUARE_WIDTH
        self.next = next
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)

    def AI(self,clicked=False):
        if clicked:
            pygame.draw.rect(SCREEN, SELECTED_COLOR, self.border)
        else:
            pygame.draw.rect(SCREEN, BLACK, self.border)
        pygame.draw.rect(SCREEN, BUTTON_COLOR, self.graphic)
        message("AI", self.graphic.center[0] - 5, self.graphic.center[1], FONT_SIZE)
        message("Opponent:", self.left_down_corner_x - 45, SETTINGS_MESSAGE_TOP_MARGIN, FONT_SIZE)

    def player(self,clicked=False):
        if clicked:
            pygame.draw.rect(SCREEN, SELECTED_COLOR, self.border)
        else:
            pygame.draw.rect(SCREEN, BLACK, self.border)
        pygame.draw.rect(SCREEN, BUTTON_COLOR, self.graphic)
        message("PLAYER", self.graphic.center[0], self.graphic.center[1], FONT_SIZE)


class ChooseMode():
    def __init__(self, number):
        self.left_down_corner_x = BOARD_WIDTH - 30 + number * 74
        self.left_down_corner_y = SETTINGS_TOP_MARGIN
        self.button_width = 70
        self.button_height = 30
        self.number = number
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)

    def stanard(self,clicked=False):
        if clicked:
            pygame.draw.rect(SCREEN, SELECTED_COLOR, self.border)
        else:
            pygame.draw.rect(SCREEN, BLACK, self.border)
        self.graphic = pygame.draw.rect(SCREEN, BUTTON_COLOR, self.graphic)
        message("Rules:", BOARD_WIDTH - 56, SETTINGS_MESSAGE_TOP_MARGIN, FONT_SIZE)
        message("standard", self.graphic.center[0], self.graphic.center[1], FONT_SIZE)

    def swap2(self,clicked=False):
        if clicked:
            pygame.draw.rect(SCREEN, SELECTED_COLOR, self.border)
        else:
            pygame.draw.rect(SCREEN, BLACK, self.border)
        self.graphic = pygame.draw.rect(SCREEN, BUTTON_COLOR, self.graphic)
        message("swap2", self.graphic.center[0], self.graphic.center[1], FONT_SIZE)


class Background():
    def __init__(self):
        SCREEN.fill(BOARD_COLOR)

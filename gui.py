"""Module contains all needed classes and functions connected with graphic"""
from enum import Enum

import pygame

import constants


class Color(Enum):
    """Enum with colors used in this module"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SELECTED = (218, 165, 32)
    BOARD = (133, 87, 35)
    BUTTON = (88, 61, 0)


BIG_FONT_SIZE = 40
FONT_SIZE = 14
SETTINGS_TOP_MARGIN = 10
BORDER = 2
constants.BOARD_SIZE = 15
SQUARE_WIDTH = 30
STONE_RADIUS = SQUARE_WIDTH // 2
SQUARE_MARGIN = 2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 545
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BOARD_WIDTH = int(constants.BOARD_SIZE * (SQUARE_WIDTH + SQUARE_MARGIN) + 2 * SQUARE_MARGIN)
LEFT_MARGIN = int(SCREEN_WIDTH - (constants.BOARD_SIZE * (SQUARE_WIDTH + SQUARE_MARGIN))) // 4
TOP_MARGIN = int(SCREEN_HEIGHT - constants.BOARD_SIZE * (SQUARE_WIDTH + SQUARE_MARGIN)) // 2
RIGHT_MARGIN = int(SCREEN_WIDTH - BOARD_WIDTH - LEFT_MARGIN)
SETTINGS_MESSAGE_TOP_MARGIN = TOP_MARGIN - 5
BUTTON_CHOOSE_MODE_WIDTH = 70
MESSAGE_CHOOSE_COLOR_X = LEFT_MARGIN + 25
MESSAGE_RULES_X = BOARD_WIDTH - 58
MESSAGE_OPPONENT_X = 226
MESSAGE_NUMBERS_X = 30
MESSAGE_WIN_HEIGHT = 40
CHOOSE_COLOR_X = 112


class Gui:
    """Base class"""
    def __init__(self, screen):
        self.screen = screen
        print(self.screen)

    def message(self, what, x, y, font_size, color=Color.BLACK.value):
        """Functions shows text on the screen with given arguments."""
        font = pygame.font.SysFont("Arial", font_size, 1)
        text = font.render(what, True, color)
        self.screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    def message_win(self, name):
        """Function prints on top of the screen message player_name wins!"""
        rect = pygame.Rect(LEFT_MARGIN, 2 * BORDER, BOARD_WIDTH - 2 * BORDER,
                           MESSAGE_WIN_HEIGHT - 2 * BORDER)
        border = pygame.Rect(LEFT_MARGIN - BORDER, BORDER, BOARD_WIDTH, MESSAGE_WIN_HEIGHT)
        pygame.draw.rect(self.screen, Color.BLACK.value, border)
        pygame.draw.rect(self.screen, Color.BUTTON.value, rect)
        self.message(name + " WINS!", rect.center[0], rect.center[1], BIG_FONT_SIZE)
        pygame.display.update()

    def message_draw(self):
        """Function prints on top of the screen message DRAW!"""
        rect = pygame.Rect(LEFT_MARGIN, 2 * BORDER, BOARD_WIDTH - 2 * BORDER,
                           MESSAGE_WIN_HEIGHT - 2 * BORDER)
        border = pygame.Rect(LEFT_MARGIN - BORDER, BORDER, BOARD_WIDTH, MESSAGE_WIN_HEIGHT)
        pygame.draw.rect(self.screen, Color.BLACK.value, border)
        pygame.draw.rect(self.screen, Color.BUTTON.value, rect)
        self.message("DRAW!", rect.center[0], rect.center[1], BIG_FONT_SIZE)
        pygame.display.update()

    def draw_board(self, board):
        """Functions draws on the middle-screen empty board"""
        for i in range(0, constants.BOARD_SIZE):
            for j in range(0, constants.BOARD_SIZE):
                board[i][j].draw_empty_square(i, j)
            self.message("{}".format(i + 1), LEFT_MARGIN - SQUARE_WIDTH // 3 - BORDER, TOP_MARGIN +
                         SQUARE_WIDTH // 2 + i * (SQUARE_WIDTH + SQUARE_MARGIN) + SQUARE_WIDTH // 2,
                         FONT_SIZE)
        for i in range(constants.BOARD_SIZE):
            self.message("{}".format(i + 1), LEFT_MARGIN + SQUARE_WIDTH // BORDER + i *
                         (SQUARE_WIDTH + SQUARE_MARGIN), MESSAGE_NUMBERS_X, FONT_SIZE)
        pygame.display.update()

    def draw_background(self):
        """Function draws background of the game"""
        self.screen.fill(Color.BOARD.value)


class Square(Gui):
    """Class contains methods connect with graphic on one square of the board"""

    def __init__(self, screen):
        super(Square, self).__init__(screen)
        """Init graphic with basic values """
        self.graphic = pygame.Rect(SQUARE_MARGIN + SQUARE_MARGIN + LEFT_MARGIN,
                                   SQUARE_WIDTH + SQUARE_MARGIN + TOP_MARGIN, SQUARE_WIDTH,
                                   SQUARE_WIDTH)
        self.border = pygame.Rect(SQUARE_MARGIN + SQUARE_MARGIN + LEFT_MARGIN - BORDER,
                                  SQUARE_WIDTH + SQUARE_MARGIN + TOP_MARGIN - BORDER,
                                  SQUARE_WIDTH + 2 * BORDER,
                                  SQUARE_WIDTH + 2 * BORDER)

    def draw_empty_square(self, j, i):
        """Method draws empty square on i,j position in board"""
        self.border = pygame.draw.rect(self.screen, Color.BLACK.value,
                                       (
                                           i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN
                                           - BORDER,
                                           j * SQUARE_WIDTH + j * SQUARE_MARGIN + SQUARE_WIDTH // 2
                                           + TOP_MARGIN - BORDER, SQUARE_WIDTH + 2 * BORDER,
                                           SQUARE_WIDTH + 2 * BORDER))
        self.graphic = pygame.draw.rect(self.screen, Color.BOARD.value,
                                        (
                                            i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN,
                                            j * SQUARE_WIDTH + j * SQUARE_MARGIN + SQUARE_WIDTH // 2
                                            + TOP_MARGIN, SQUARE_WIDTH, SQUARE_WIDTH))

    def draw_white_stone(self, j, i, last_move=False):
        """Method draws white stone on square(j,i) if square is last move draws golden frame"""
        if last_move:
            self.border = pygame.draw.rect(self.screen, Color.SELECTED.value,
                                           (i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN
                                            - BORDER, j * SQUARE_WIDTH + j * SQUARE_MARGIN +
                                            SQUARE_WIDTH // 2 + TOP_MARGIN - BORDER, SQUARE_WIDTH
                                            + 2 * BORDER, SQUARE_WIDTH + 2 * BORDER))
            self.graphic = pygame.draw.rect(self.screen, Color.BOARD.value,
                                            (i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN,
                                             j * SQUARE_WIDTH + j * SQUARE_MARGIN + SQUARE_WIDTH
                                             // 2 + TOP_MARGIN, SQUARE_WIDTH, SQUARE_WIDTH))

        self.graphic = pygame.draw.circle(self.screen, Color.WHITE.value,
                                          (i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN +
                                           SQUARE_WIDTH // 2, j * SQUARE_WIDTH + j *
                                           SQUARE_MARGIN + SQUARE_WIDTH // 2 + TOP_MARGIN +
                                           SQUARE_WIDTH // 2), SQUARE_WIDTH // 2)

    def draw_black_stone(self, j, i, last_move=False):
        """Method draws black stone on square(j,i) if square is last move draws golden frame."""
        if last_move:
            self.border = pygame.draw.rect(self.screen, Color.SELECTED.value,
                                           (
                                               i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN
                                               - BORDER, j * SQUARE_WIDTH + j * SQUARE_MARGIN +
                                               SQUARE_WIDTH // 2 + TOP_MARGIN - BORDER, SQUARE_WIDTH
                                               + 2 * BORDER, SQUARE_WIDTH + 2 * BORDER))
            self.graphic = pygame.draw.rect(self.screen, Color.BOARD.value,
                                            (
                                                i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN,
                                                j * SQUARE_WIDTH + j * SQUARE_MARGIN + SQUARE_WIDTH
                                                // 2 + TOP_MARGIN, SQUARE_WIDTH, SQUARE_WIDTH))
        self.graphic = pygame.draw.circle(self.screen, Color.BLACK.value,
                                          (
                                              i * SQUARE_WIDTH + i * SQUARE_MARGIN + LEFT_MARGIN +
                                              SQUARE_WIDTH // 2,
                                              j * SQUARE_WIDTH + j * SQUARE_MARGIN +
                                              SQUARE_WIDTH // 2 +
                                              TOP_MARGIN + SQUARE_WIDTH // 2),
                                          SQUARE_WIDTH // 2)


class OnMove(Gui):
    """Class shows on right of the board text "Turn:" and "player's name" and stone graphic."""

    def __init__(self, screen):
        super(OnMove, self).__init__(screen)
        self.left_down_corner_x = SCREEN_WIDTH - 70
        self.left_down_corner_y = SCREEN_HEIGHT // 3.5
        self.button_width = RIGHT_MARGIN * 1 // 10
        self.button_height = RIGHT_MARGIN * 1 // 10
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)
        self.message("Turn:", self.graphic.center[0], self.graphic.center[1] - 20, FONT_SIZE)
        self.graphic_stone = pygame.Rect(SCREEN_WIDTH - RIGHT_MARGIN,
                                         SCREEN_HEIGHT // 3.5, SQUARE_WIDTH * 2.8,
                                         SQUARE_WIDTH // 2)

    def black(self, name):
        """Draws black stone as graphic on turn and name given in function."""
        pygame.draw.rect(self.screen, Color.BOARD.value, self.graphic_stone)
        self.message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 2 * BORDER,
                     self.graphic_stone.center[1], FONT_SIZE)
        self.graphic = pygame.draw.circle(self.screen, Color.BLACK.value, (
            int(self.graphic_stone.midright[0]) - SQUARE_WIDTH // 2 - BORDER,
            int(self.graphic_stone.midright[1]) - BORDER), int(SQUARE_WIDTH // 2.5))
        pygame.display.update()

    def white(self, name):
        """Draws black stone as graphic on turn and name given in function."""
        pygame.draw.rect(self.screen, Color.BOARD.value, self.graphic_stone)
        self.message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 2 * BORDER,
                     self.graphic_stone.center[1], FONT_SIZE)
        self.graphic = pygame.draw.circle(self.screen, Color.WHITE.value, (
            int(self.graphic_stone.midright[0]) - SQUARE_WIDTH // 2 - BORDER,
            int(self.graphic_stone.midright[1] - BORDER)), int(SQUARE_WIDTH // 2.5))
        pygame.display.update()

    def change_message(self, name):
        """Method changes player's name on turn."""
        pygame.draw.rect(self.screen, Color.BOARD.value, (SCREEN_WIDTH - RIGHT_MARGIN,
                                                          SCREEN_HEIGHT // 3.5,
                                                          int(SQUARE_WIDTH * 1.7),
                                                          SQUARE_WIDTH // 2))
        self.message(name, SCREEN_WIDTH - RIGHT_MARGIN + RIGHT_MARGIN // 4 + 2 * BORDER,
                     self.graphic_stone.center[1], FONT_SIZE)
        pygame.display.update()


class ButtonRightMenu(Gui):
    """Class creating right menu with button with given names."""

    def __init__(self, screen, next_=0, name="Button"):
        super(ButtonRightMenu, self).__init__(screen)
        """Init all buttons properties, "next" argument allows to create next button under last."""
        self.button_width = RIGHT_MARGIN * 9 // 10
        self.button_height = SQUARE_WIDTH
        self.left_down_corner_x = SCREEN_WIDTH - RIGHT_MARGIN // 2 - self.button_width // 2
        self.left_down_corner_y = SCREEN_HEIGHT // 3 + (next_ * (SQUARE_WIDTH + 2 *
                                                                 SQUARE_MARGIN)) - BORDER
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)
        pygame.draw.rect(self.screen, Color.BLACK.value, self.border)
        pygame.draw.rect(self.screen, Color.BUTTON.value, self.graphic)
        self.message(name, self.graphic.center[0], self.graphic.center[1], FONT_SIZE)


class ButtonChooseColor(Gui):
    """Class creates on left above board  text "Choose color:" buttons white and black stone."""

    def __init__(self, screen, next_=0):
        super(ButtonChooseColor, self).__init__(screen)
        """Init with all button properties, "next" allows creating buttons next to each other."""
        self.button_width = SQUARE_WIDTH
        self.button_height = SQUARE_WIDTH
        self.left_down_corner_x = CHOOSE_COLOR_X + next_ * (SQUARE_WIDTH + BORDER * BORDER)
        self.left_down_corner_y = SETTINGS_TOP_MARGIN
        self.next = next_
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)

    def black(self, selected=False):
        """Method draws black stone if button is selected drawing golden frame. """
        if selected:
            pygame.draw.rect(self.screen, Color.SELECTED.value, self.border)
        else:
            pygame.draw.rect(self.screen, Color.BLACK.value, self.border)
        pygame.draw.rect(self.screen, Color.BUTTON.value, self.graphic)
        pygame.draw.circle(self.screen, Color.BLACK.value, self.graphic.center,
                           STONE_RADIUS - BORDER)

    def white(self, selected=False):
        """Method draws white stone if button is selected drawing golden frame. """
        self.message("Choose color:", MESSAGE_CHOOSE_COLOR_X, SETTINGS_MESSAGE_TOP_MARGIN,
                     FONT_SIZE)
        if selected:
            pygame.draw.rect(self.screen, Color.SELECTED.value, self.border)
        else:
            pygame.draw.rect(self.screen, Color.BLACK.value, self.border)
        pygame.draw.rect(self.screen, Color.BUTTON.value, self.graphic)
        pygame.draw.circle(self.screen, Color.WHITE.value, self.graphic.center,
                           STONE_RADIUS - BORDER)

    def hide(self):
        """Methods covers all buttons after choosing colors during game in swap2 mode."""
        pygame.draw.rect(self.screen, Color.BOARD.value, (0, self.left_down_corner_y - BORDER,
                                                          BOARD_WIDTH,
                                                          self.button_height + 2 * BORDER))
        for i in range(constants.BOARD_SIZE):
            self.message("{}".format(i + 1), LEFT_MARGIN + SQUARE_WIDTH // BORDER + i *
                         (SQUARE_WIDTH + SQUARE_MARGIN), MESSAGE_NUMBERS_X, FONT_SIZE)


class ButtonChooseOpponent(Gui):
    """Class creates on middle above board text "Opponent:" and buttons "Ai" and Player"."""

    def __init__(self, screen, next_=0):
        super(ButtonChooseOpponent, self).__init__(screen)
        """Init with all button properties, "next" allows creating buttons next to each other."""
        self.left_down_corner_x = SCREEN_WIDTH // 2 + next_ * (SQUARE_WIDTH * 2 + 2 * BORDER) \
                                  - SQUARE_WIDTH
        self.left_down_corner_y = SETTINGS_TOP_MARGIN
        self.button_width = SQUARE_WIDTH * 2
        self.button_height = SQUARE_WIDTH
        self.next = next_
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)

    def AI(self, selected=False):
        """Method draws text "Opponent:"and button "AI" if button is selected draws golden frame."""
        if selected:
            pygame.draw.rect(self.screen, Color.SELECTED.value, self.border)
        else:
            pygame.draw.rect(self.screen, Color.BLACK.value, self.border)
        pygame.draw.rect(self.screen, Color.BUTTON.value, self.graphic)
        self.message("AI", self.graphic.center[0], self.graphic.center[1], FONT_SIZE)
        self.message("Opponent:", MESSAGE_OPPONENT_X, SETTINGS_MESSAGE_TOP_MARGIN, FONT_SIZE)

    def player(self, selected=False):
        """Method draws button "Player" if button is selected draws golden frame."""
        if selected:
            pygame.draw.rect(self.screen, Color.SELECTED.value, self.border)
        else:
            pygame.draw.rect(self.screen, Color.BLACK.value, self.border)
        pygame.draw.rect(self.screen, Color.BUTTON.value, self.graphic)
        self.message("PLAYER", self.graphic.center[0], self.graphic.center[1], FONT_SIZE)


class ButtonChooseMode(Gui):
    """Class creates on right above board text"Mode: ",buttons with names "standard" and "swap2"."""

    def __init__(self, screen, number):
        super(ButtonChooseMode, self).__init__(screen)
        self.left_down_corner_x = BOARD_WIDTH - SQUARE_WIDTH + number * (BUTTON_CHOOSE_MODE_WIDTH +
                                                                         2 * BORDER)
        self.left_down_corner_y = SETTINGS_TOP_MARGIN
        self.button_width = BUTTON_CHOOSE_MODE_WIDTH
        self.button_height = SQUARE_WIDTH
        self.number = number
        self.border = pygame.Rect(
            self.left_down_corner_x - BORDER, self.left_down_corner_y - BORDER,
            self.button_width + 2 * BORDER,
            self.button_height + 2 * BORDER)
        self.graphic = pygame.Rect(
            self.left_down_corner_x, self.left_down_corner_y, self.button_width, self.button_height)

    def standard(self, selected=False):
        """Method draws "Rules:"a nd button "standard" if button is selected draws golden frame."""
        if selected:
            pygame.draw.rect(self.screen, Color.SELECTED.value, self.border)
        else:
            pygame.draw.rect(self.screen, Color.BLACK.value, self.border)
        self.graphic = pygame.draw.rect(self.screen, Color.BUTTON.value, self.graphic)
        self.message("Rules:", MESSAGE_RULES_X, SETTINGS_MESSAGE_TOP_MARGIN, FONT_SIZE)
        self.message("standard", self.graphic.center[0], self.graphic.center[1], FONT_SIZE)

    def swap2(self, selected=False):
        """Method draws "swap2:"a nd button "standard" if button is selected draws golden frame."""
        if selected:
            pygame.draw.rect(self.screen, Color.SELECTED.value, self.border)
        else:
            pygame.draw.rect(self.screen, Color.BLACK.value, self.border)
        self.graphic = pygame.draw.rect(self.screen, Color.BUTTON.value, self.graphic)
        self.message("swap2", self.graphic.center[0], self.graphic.center[1], FONT_SIZE)

"""Main module controlling changing of game modes"""
import collections

import pygame

import game
import standard
import swap2
import constants

GameSettings = collections.namedtuple("GameSettings", "player1 player2 player_on_move game_mode")
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 545
WINDOW_CAPTION = 'Gomoku'


def main():
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_CAPTION)
    while True:

        gra = game.Game(screen)
        settings = gra.menu()
        if settings:
            if settings.game_mode == constants.STANDARD:
                while True:
                    if not standard.Standard(screen, settings.player1, settings.player2,
                                             settings.player_on_move).playgame() == constants.RESTART:
                        break
            elif settings.game_mode == constants.SWAP2:
                while True:
                    if not swap2.Swap2(screen, settings.player1, settings.player2,
                                       settings.player_on_move).playgame() == constants.RESTART:
                        break

        pygame.display.update()


if __name__ == '__main__':
    main()

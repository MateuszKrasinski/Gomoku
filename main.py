"""Main module controlling changing of game modes"""
import collections

import pygame

import game
import standard
import swap2
import constants

GameSettings = collections.namedtuple("GameSettings", "player1 player2 player_on_move game_mode")


def main():
    while True:

        gra = game.Game()
        settings = gra.menu()
        if settings:
            if settings.game_mode == constants.STANDARD:
                while True:
                    if not standard.Standard(settings.player1, settings.player2,
                                             settings.player_on_move).playgame() == constants.RESTART:
                        break
            elif settings[3] == constants.SWAP2:
                while True:
                    if not swap2.Swap2(settings.player1, settings.player2,
                                       settings.player_on_move).playgame() == constants.RESTART:
                        break

        pygame.display.update()


if __name__ == '__main__':
    main()

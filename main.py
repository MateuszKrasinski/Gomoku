"""Main module controlling changing of game modes"""
import collections

import pygame

import game
import standard
import swap2
import constants

GameSettings = collections.namedtuple("GameSettings", "player1 player2 game_mode")


def main():
    while True:

        gra = game.Game()
        game_settings = gra.menu()
        if game_settings:
            if game_settings[3] == constants.STANDARD:
                while True:
                    if not standard.Standard(game_settings[0], game_settings[1],
                                             game_settings[2]).playgame() == constants.RESTART:
                        break
            elif game_settings[3] == constants.SWAP2:
                while True:
                    if not swap2.Swap2(game_settings[0], game_settings[1],
                                       game_settings[2]).playgame() == constants.RESTART:
                        break

        pygame.display.update()


if __name__ == '__main__':
    main()

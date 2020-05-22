"""Main module controlling changing of game modes"""
import collections

import pygame

import game
import standard
import swap2

RESTART = "Restart"
MENU = "Menu"
SWAP2 = "swap2"
STANDARD = "standard"
GameSettings = collections.namedtuple("GameSettings", "player1,player2 game_mode")
while True:

    gra = game.Game()
    GameSettings = gra.menu()
    if GameSettings:
        if GameSettings[3] == STANDARD:
            while True:
                if standard.Standard(GameSettings[0], GameSettings[1],
                                     GameSettings[2]).playgame() == RESTART:
                    continue
                break
        elif GameSettings[3] == SWAP2:
            while True:
                if swap2.Swap2(GameSettings[0], GameSettings[1],
                               GameSettings[2]).playgame() == RESTART:
                    continue
                break

    pygame.display.update()
if __name__ == '__main__':
    main()

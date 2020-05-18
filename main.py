import time
import sys

import swap2, standard
import pygame

import game

while (True):

    gra = game.Game()
    result = gra.menu()
    if result:
        if result[3] == "standard":
            gra = standard.Standard(result[0], result[1], result[2])
            gra = True
            while gra:
                gra = standard.Standard(result[0], result[1], result[2])
                gra = gra.playgame()
                if gra == "Restart":
                    pass
                if gra == "Menu":
                    break
        elif result[3] == "swap2":
            gra = True
            while gra:
                gra = swap2.Swap2(result[0], result[1], result[2])
                gra = gra.playgame()
                if gra == "Restart":
                    pass
                if gra == "Menu":
                    break

    pygame.display.update()

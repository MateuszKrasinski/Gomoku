from Game import Game
import time,sys
import swap2,standard
import pygame
from Player import Player
from Globals import screen
while(True):


    game=Game()
    result = game.Menu()
    if result:
        if result[3]=="standard":
            game=standard.Standard(result[0],result[1],result[2])
            game = True
            while game:
                game = standard.Standard(result[0], result[1], result[2])
                game = game.playgame()
                if game == "Restart":
                    pass
                if game == "Menu":
                    break
        elif result[3]=="swap2":
            game=True
            while game:
                game=swap2.Swap2(result[0],result[1],result[2])
                game=game.playgame()
                if game=="Restart":
                    pass
                if game=="Menu":
                    break


    pygame.display.update()


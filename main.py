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
        print("Player 1:", result[0].name)
        print("Player 2:", result[1].name)
        print("Na ruchu:", result[2].name)
        print("Game rules:",result[3])
        if result[3]=="standard":
            game=standard.Standard(result[0],result[1],result[2])
        elif result[3]=="swap2":
            game=swap2.Swap2(result[0],result[1],result[2])
        game.playgame()

    pygame.display.update()


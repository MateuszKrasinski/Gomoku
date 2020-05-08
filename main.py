from Game import Game
import time,sys
import pygame
StartGame=True
while(True):
    game = Game()
    if game.playgame():
        continue
    else:
        time.sleep(5)
        sys.exit(0)

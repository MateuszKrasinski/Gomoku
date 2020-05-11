from Game import Game
import time,sys
import swap2,standard
import pygame
from Globals import screen
StartGame=True
mode1=True
mode2=False
while(True):
    if mode1:
        game=standard.Standard()
    else:
        game=swap2.swap2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if game.buttonNewGame.graphic.collidepoint()==pos:
                mode1=True
                continue
            elif game.buttonSettings.graphic.collidepoint()==pos:
                mod1=False
                continue
    if game.playgame():
        continue
    else:
        time.sleep(5)
        sys.exit(0)

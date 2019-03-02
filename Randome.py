import pygame
import sys
from pygame.locals import *

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = ( 55,0,0)

size = (800,800)
screen = pygame.display.set_mode(size)
screen.fill(RED)
pygame.display.update()
pygame.display.set_caption('The Acrid Dragon Flys')


# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop

import pygame #always need to create a game
import random #to get randome numbers or locations or etc..
import sys #import the game system


pygame.init() # new to initalize the game

(width, height) = (800, 800) # dimensions of the screen
screen = pygame.display.set_mode((width, height)) # fucntion to display screen
pygame.display.flip() # call pygame to display screen

running = True # to open screen and to close
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

import pygame
from imageSpaceBackground import Star, SpaceBackground
from character import player
import os

#from testCharacter import player
pygame.init()

(winX, winY) = (600, 700)

running = True

screen = pygame.display.set_mode((winX, winY))
clock = pygame.time.Clock()

bg = SpaceBackground(screen, 1, 0)

p1= player(300,410,64,64)

while running:

    clock.tick(120)

    screen.fill((24,24,24))

    p1.draw(screen)

    bg.updateItems()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys= pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        
        if p1.x<=winX-p1.width-p1.vel and (keys[pygame.K_d] or p1.keys[pygame.K_RIGHT]):
            p1.moveRight()
            print ("R")

        if p1.x>=10 and (keys[pygame.K_a] or p1.keys[pygame.K_LEFT]):
            p1.moveLeft()
            print ("L")

        if p1.x>=10 and (keys[pygame.K_w] or p1.keys[pygame.K_UP]):
            p1.moveUp()
            print ("U")

        if p1.x>=10 and (keys[pygame.K_s] or p1.keys[pygame.K_DOWN]):
            p1.moveDown()
            print ("D")

    pygame.display.flip()


pygame.quit()
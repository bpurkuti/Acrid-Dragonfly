#import libraries and Objects from different files
import pygame
import os
#ScoreBoard tracks and presents Score in the GameScreen
from scoreBoard import ScoreBoard
#The Background for the game, consisting of stars and asteroids
from imageSpaceBackground import Star, SpaceBackground
#Character/player class
from character import player

#initialize game
pygame.init()

#Window Size
(winX, winY) = (800, 600)

#Create the window with aboce specs
screen = pygame.display.set_mode((winX, winY))
#clock used for fps
clock = pygame.time.Clock()

#initialzing the Objects
scoreB = ScoreBoard(100, 100)
score = 0
scoreB.setScore(score)

bg = SpaceBackground(screen, 2, 0)

p1= player(300,410,64,64)

running = True
while running:
    #FPS
    clock.tick(50)

    screen.fill((24,24,24))

    #drawing ScoreBoard
    score = score + 1
    scoreB.setScore(score)
    scoreB.draw(screen)
    bg.updateItems()

    #drawing player
    p1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys= pygame.key.get_pressed()
        #Escape to exit
        if keys[pygame.K_ESCAPE]:
            running = False
        #PlayerMovements + Boundaries: Right, Left, Up, and Down
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
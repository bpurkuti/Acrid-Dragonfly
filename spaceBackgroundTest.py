#import libraries and Objects from different files
import pygame
import os
#ScoreBoard tracks and presents Score in the GameScreen
from scoreBoard import ScoreBoard
#The Background for the game, consisting of stars and asteroids
from imageSpaceBackground import Star, SpaceBackground
#Character/player class
from character import player
from Projectiles import projectile

white=(250,250,250)
#initialize game
pygame.init()

#Window Size
(winX, winY) = (800, 600)

#Create the window with aboce specs
screen = pygame.display.set_mode((winX, winY))
#clock used for fps
clock = pygame.time.Clock()

#initialzing the Objects
scoreB = ScoreBoard(0,0)
score = 0
scoreB.setScore(score)
bg = SpaceBackground(screen, 2, 0)
p1= player(300, 410, 64, 64)
b1= projectile(5, 8, 6,(250,250,250), -1)
bullets=[]

running = True
while running:
    #FPS
    clock.tick(100)

    screen.fill((24,24,24))

    #drawing ScoreBoard
    score = score + 1
    scoreB.setScore(score)
    scoreB.draw(screen)
    bg.updateItems()

    #drawing player
    p1.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
   
    #testing stuff with bullets
    for bullet in bullets:
        if bullet.x <500 and bullet.x >0:
            bullet.x+=bullet.vel
        else:
            bullet.pop(bullets.index(bullet))
    
    keys= pygame.key.get_pressed()

    #Drawing bullets
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            #x,y,radius,color,facing
            bullets.append(b1) #1 is for direction
    #Escape to exit
    if keys[pygame.K_ESCAPE]:
        running = False
    #PlayerMovements + Boundaries: Right, Left, Up, and Down
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
        if p1.x<=winX - p1.width - p1.vel:
            p1.moveRight()
            print ("R")

    elif (keys[pygame.K_a] or keys[pygame.K_LEFT]):
        if p1.x>=p1.vel:   
            p1.moveLeft()
            print ("L")

    elif (keys[pygame.K_w] or keys[pygame.K_UP]):
        if p1.y>=p1.vel:
            p1.moveUp()
            print ("U")

    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]):
        if p1.y<=winY - p1.height - p1.vel:
            p1.moveDown()
            print ("D")
    else:
        print ("still")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        

    pygame.display.flip()


pygame.quit()
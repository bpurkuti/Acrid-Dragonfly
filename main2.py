#import libraries and Objects from different files
import pygame
import os
#ScoreBoard tracks and presents Score in the GameScreen
from screens.scoreBoard import ScoreBoard
#The Background for the game, consisting of stars and asteroids
from screens.spaceBackground import Star, SpaceBackground
from screens.startScreen import StartScreen
from screens.finishScreen import FinishScreen
#Character/player class
from character import player


#initialize game
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('music/BackSound.mp3')
pygame.mixer.music.set_volume(0.5) # volume of the son
pygame.mixer.music.play(-1)

#Window Size
(winX, winY) = (1200, 800)


#Create the window with aboce specs
screen = pygame.display.set_mode((winX, winY))
#clock used for fps
clock = pygame.time.Clock()

#initialzing the Objects
scoreB = ScoreBoard(20, 20, 40)
score = 0
scoreB.setScore(score)

bg = SpaceBackground(screen, 1, 0)

p1= player(300,410,64,64)

running = True
runGame = False
def beginGame():
    global runGame
    runGame = True
def quitGame():
    global running
    running = False

ss = StartScreen(screen, beginGame)

while running:
    #FPS
    clock.tick(30)

    screen.fill((24,24,24))

    bg.updateItems()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if(event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN):
            position = pygame.mouse.get_pos()
            ss.handleClick(position, event.type)

    keys = pygame.key.get_pressed()

    #Escape to exit
    if keys[pygame.K_ESCAPE]:
        if(runGame):
            runGame = False
            ss = FinishScreen(screen, score, beginGame, quitGame)
            score = 0
        else:
            pass

    if(runGame):
        #drawing ScoreBoard
        score = score + 1
        scoreB.setScore(score)
        scoreB.draw(screen)

        #drawing player
        p1.draw(screen)

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

    else:
        ss.draw()

    pygame.display.flip()


pygame.quit()

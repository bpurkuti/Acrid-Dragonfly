import pygame
from screens import SpaceBackground
from gameState import *

#initialize game
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('music/BackSound.mp3')
pygame.mixer.music.set_volume(0.2) # volume of the son
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode(WIN_SIZE)

# 0 start, 1 active, 2 end
GAME_STATE = 0

def setGS1():
    global GAME_STATE
    GAME_STATE = 1

def setGS2():
    global GAME_STATE
    GAME_STATE = 2

mainRunning = True

def STOPGAME():
    global mainRunning
    mainRunning = False

SB = ScoreBoard(0, 0, 30)
SCORE = 0
SB.setScore(SCORE)
BGS = SpaceBackground(screen, 1, 10)
SS = StartScreen(screen, setGS1)

clock = pygame.time.Clock()

mainRunning = True
while mainRunning:

    screen.fill((0, 0, 0))

    if(GAME_STATE == 0):
        gameScreens.start(setGS1, clock, BGS, screen)
    elif(GAME_STATE == 1):
        runGame(screen, BGS, setGS2, clock)
    elif(GAME_STATE == 2):
        pass
    else:
        STOPGAME()


    keys= pygame.key.get_pressed()

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

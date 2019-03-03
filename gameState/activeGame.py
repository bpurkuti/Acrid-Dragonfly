from gameState.loadSkins import *
from entities import *
from logic import *
import random, math

WIN_SIZE = (1200, 800)
WIN_HITBOX = RectangleHB((0,0), (1200, 0), (1200, 800), (0, 800))

MID = (WIN_SIZE[0] // 2, WIN_SIZE[1] // 2)
PLAYER_SETTINGS = [
    PLAYER_SKINS[0],
    10, PLAYER_SKINS[1][0], False,
    MID[0], MID[1], 10, 0, 1,
    100,
    PROJECTILE_SKINS[0][1], PROJECTILE_SKINS[1][1], PROJECTILE_SKINS[2][1],
    20, 50, 5
]

running = True
def stopGame():
    global running
    running = False

PLAYER_SETTINGS.append(stopGame)

def runGame(screen, BGS, topEH, clock):
    
    player = Player(*PLAYER_SETTINGS)
    projectilesE = []
    projectilesM = []
    enemies = []

    while running:

        clock.tick(30)

        screen.fill(0, 0, 0)
        BGS.updateItems

        mpos = pygame.mouse.get_pos()
        mdisp = (mpos[0] - player.movement.x, mpos[1] - player.movement.y)
        newRotation = math.degrees(math.atan(disp[1] / disp[0]))
        player.updateRotation(newRotation)

        keys = pygame.key.get_pressed()

        #Escape to exit
        if keys[pygame.K_ESCAPE]:
            stopGame()

        moveProfile = (0,0,0,0)
    
        #PlayerMovements + Boundaries: Right, Left, Up, and Down
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            moveProfile[1] = 1
            print ("R")

        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            moveProfile[3] = 1
            print ("L")

        elif (keys[pygame.K_w] or keys[pygame.K_UP]):
            moveProfile[0] = 1
            print ("U")

        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            moveProfile[2] = 1
            print ("D")

        direction = (moveProfile[1] - moveProfile[3], moveProfile[0] - moveProfile[2])
        direction = -math.atan(moveProfile[1] / moveProfile[0])
        direction = (math.cos(direction), math.sin(direction))

        player.updateAcceleration(direction)
        player.updateMovement()
        if(player.getHitbox().didHit(WIN_HITBOX)):
            velT = player.movement.vel
            player.movement.vel = (-velT[0], -velT[1])
            player.movement.acc = -player.movement.acc
        
        for p in projectilesE:
            p.updateMovement()
        for p in projectilesM:
            p.updateMovement()
        for e in enemies:
            e.updateMovement()

        
        










        player.draw(screen)
        for p in projectilesE:
            p.draw(screen)
        for p in projectilesM:
            p.draw(screen)
        for e in enemies:
            e.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopGame()




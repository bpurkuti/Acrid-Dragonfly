import pygame
import os
#initializing
pygame.init()

#loading player sprites
rightSprite = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R2.png')]
leftSprite = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('R2.png')]
upSprite= [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('R2.png')]
downSprite= [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('R2.png')]
stillFrame=pygame.image.load('standing.png')

clock=pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        #man=player(300,410,64,64)
    def draw(self,win):
        if self.left:
            win.blit(moveLeft[self.walkCount//3], (self.x,self.y)) #integer divison
        elif self.right:
            win.blit(moveRight[self.walkCount//3], (self.x,self.y))
        elif self.up:
            win.blit(moveRight[self.walkCount//3], (self.x,self.y))
        elif self.down:
            win.blit(moveRight[self.walkCount//3], (self.x,self.y))
        else:
            win.blit(stillFrame, (self.x,self.y))

    def 

    #check for events
    #gets all the events like mouse and stuff
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run= False

    #Do these stuff when any key is pressed down
        if event.type== pygame.KEYDOWN:

    #Exit out when the ESCAPE is pressed down
            if event.key==pygame.K_ESCAPE:
                run= False

    #Player Movement
    
    #holding keys
    keys= pygame.key.get_pressed()
    #moving left
    if man.x>=10 and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
        man.x-=man.vel
        man.left=True
        man.right=False
        print ('',man.x,man.y)
    #moving right
    elif man.x<=winX-man.width and (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
        man.x+=man.vel 
        man.left=False
        man.right=True
        print ('',man.x,man.y)
    else:
        man.right=False
        man.left=False
        man.walkCount=0

    #implementing Jump
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump=True
            man.right=False
            man.left=False
    else: #use quadratic func fr jump
        #go up
        if man.jumpCount>=-10:
            neg=1
            #falling down
            if man.jumpCount<0:
                neg=-1
            man.y-=man.jumpCount **2*0.5*neg
            man.jumpCount-=1

        else:
            man.isJump=False
            man.jumpCount=10
    redrawGameWindow()
pygame.quit()

        

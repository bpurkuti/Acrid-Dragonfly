import pygame
import pygame.gfxdraw
import os

#loading player sprites
rightSprite = [pygame.image.load('Game Sprites/right1.png'), pygame.image.load('Game Sprites/right2.png'), pygame.image.load('Game Sprites/right3.png'),pygame.image.load('Game Sprites/right2.png'),pygame.image.load('Game Sprites/right1.png')]
leftSprite = [pygame.image.load('Game Sprites/left1.png'), pygame.image.load('Game Sprites/left2.png'), pygame.image.load('Game Sprites/left3.png'),pygame.image.load('Game Sprites/left2.png'),pygame.image.load('Game Sprites/left1.png')]
upSprite= [pygame.image.load('Game Sprites/up1.png'), pygame.image.load('Game Sprites/up2.png'), pygame.image.load('Game Sprites/up3.png'),pygame.image.load('Game Sprites/up2.png'),pygame.image.load('Game Sprites/up1.png')]
downSprite= [pygame.image.load('Game Sprites/down1.png'), pygame.image.load('Game Sprites/down2.png'), pygame.image.load('Game Sprites/down3.png'),pygame.image.load('Game Sprites/down2.png'),pygame.image.load('Game Sprites/down1.png')]
stillFrame=pygame.image.load('up1.png')

clock=pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.keys= pygame.key.get_pressed()

        #man=player(300,410,64,64)
    def draw(self,win):
        if self.left:
            win.blit(leftSprite[1], (self.x,self.y)) #integer divison
            

        elif self.right:
            win.blit(rightSprite[1], (self.x,self.y)) 

        elif self.up:
            win.blit(upSprite[4], (self.x,self.y))
            
        elif self.down:
            win.blit(downSprite[1], (self.x,self.y))
            
        else:
            win.blit(stillFrame, (self.x,self.y))
            self.left = False
            self.right = False
            self.up = False
            self.down = False

    def moveRight(self):
            self.x+=self.vel
            self.right=True
            self.left = False
            self.up = False
            self.down = False
            print ('',self.x,self.y)

    def moveLeft(self):
            self.x-=self.vel
            self.left=True
            self.right = False
            self.up = False
            self.down = False
            print ('',self.x,self.y)
    
    def moveUp(self):
            self.y-=self.vel
            self.up=True
            self.left = False
            self.right = False
            self.down = False
            print ('',self.x,self.y)

    def moveDown(self):
            self.y+=self.vel
            self.down=True
            self.left = False
            self.right = False
            self.up = False
            print ('',self.x,self.y)

        

import pygame
import pygame.gfxdraw
import os

#loading player sprites
rightSprite = [pygame.image.load('gameSprites/right1.png'), pygame.image.load('gameSprites/right2.png'), pygame.image.load('gameSprites/right3.png'),pygame.image.load('gameSprites/right2.png'),pygame.image.load('gameSprites/right1.png')]
leftSprite = [pygame.image.load('gameSprites/left1.png'), pygame.image.load('gameSprites/left2.png'), pygame.image.load('gameSprites/left3.png'),pygame.image.load('gameSprites/left2.png'),pygame.image.load('gameSprites/left1.png')]
upSprite= [pygame.image.load('gameSprites/up1.png'), pygame.image.load('gameSprites/up2.png'), pygame.image.load('gameSprites/up3.png'),pygame.image.load('gameSprites/up2.png'),pygame.image.load('gameSprites/up1.png')]
downSprite= [pygame.image.load('gameSprites/down1.png'), pygame.image.load('gameSprites/down2.png'), pygame.image.load('gameSprites/down3.png'),pygame.image.load('gameSprites/down2.png'),pygame.image.load('gameSprites/down1.png')]
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
        self.spriteLoop = 0
        self.fire=False

        #man=player(300,410,64,64)
    def draw(self,win):

        self.spriteLoop = (self.spriteLoop + 1) % 5
        
        if self.left:
            win.blit(leftSprite[self.spriteLoop], (self.x,self.y)) #integer divison
            

        if self.right:
            win.blit(rightSprite[self.spriteLoop], (self.x,self.y)) 

        if self.up:
            win.blit(upSprite[self.spriteLoop], (self.x,self.y))
            
        if self.down:
            win.blit(downSprite[self.spriteLoop], (self.x,self.y))
            
        if self.left==False and self.right==False and self.up==False and self.down==False:
            win.blit(upSprite[self.spriteLoop], (self.x,self.y))
            self.left = False
            self.right = False
            self.up = False
            self.down = False

    def moveLeft(self):
            self.x-=self.vel
            self.left=True
            self.right = False
            self.up = False
            self.down = False
            print ('',self.x,self.y)

    def moveRight(self):
            self.x+=self.vel
            self.right=True
            self.left = False
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
    


import pygame
import pygame.gfxdraw
import os

#loading player sprites
rightSprite = [pygame.image.load('up1.png'), pygame.image.load('up1.png'), pygame.image.load('up1.png')]
leftSprite = [pygame.image.load('up1.png'), pygame.image.load('up1.png'), pygame.image.load('up1.png')]
upSprite= [pygame.image.load('up1.png'), pygame.image.load('up1.png'), pygame.image.load('up1.png')]
downSprite= [pygame.image.load('up1.png'), pygame.image.load('up1.png'), pygame.image.load('up1.png')]
stillFrame=pygame.image.load('up1.png')

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
        self.keys= pygame.key.get_pressed()

        #man=player(300,410,64,64)
    def draw(self,win):
        if self.left:
            #win.blit(leftSprite[3], (self.x,self.y)) #integer divison
            pygame.gfxdraw.box(win, pygame.Rect(self.x,self.y,self.width,self.height), (250,0,0))
            

        elif self.right:
            #win.blit(rightSprite[3], (self.x,self.y))
            pygame.gfxdraw.box(win, pygame.Rect(self.x,self.y,self.width,self.height), (0,250,0))
            

        elif self.up:
           # win.blit(upSprite[3], (self.x,self.y))
            pygame.gfxdraw.box(win, pygame.Rect(self.x,self.y,self.width,self.height), (1,7,7))
            
        elif self.down:
            #win.blit(downSprite[3], (self.x,self.y))
            pygame.gfxdraw.box(win, pygame.Rect(self.x,self.y,self.width,self.height), (170,80,32))
            
        else:
            #win.blit(stillFrame, (self.x,self.y))
            pygame.gfxdraw.box(win, pygame.Rect(self.x,self.y,self.width,self.height), (250,0,250))
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

        

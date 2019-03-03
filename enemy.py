import pygame
import random
import pygame.gfxdraw
import os

clock=pygame.time.Clock()

class Enemy1(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.keys= pygame.key.get_pressed()

   def draw(self,win):



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

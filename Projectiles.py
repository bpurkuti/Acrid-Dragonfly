import pygame
import os
class projectile(object):
    def __init__(self,x,y,width,height,radius,color,facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
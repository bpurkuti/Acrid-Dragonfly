import pygame
import math

class Movement(object):

    def __init__(self, x, y, vel, acc):
        self.x = x
        self.y = y
        self.vel = vel
        self.acc = acc

    def updatePosition(self):
        self.vel = (self.vel[0] + self.acc[0], self.vel[1] + self.acc[1])
        self.x = self.x + self.vel[0]
        self.y = self.y + self.vel[1]

    def forceVelocity(self, newVel):
        self.vel = newVel

    def updateAcceleration(self, newAcc):
        self.acc = newAcc

    

    
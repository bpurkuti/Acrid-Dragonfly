import pygame
from logic.movement import Movement
from logic.hitbox import CircleHB, RectangleHB
from logic.collision import rotate_around_point_highperf
from logic.accelerationProfile import AccelerationProfile

class Entity(object):

    def __init__(self, skin, size, hType, x, y, vel, acc, accelerationProfile, rotation):
        # type = rectangle (true), circle (false)
        self.skin = skin
        self.movement = Movement(x, y, vel, acc)
        self.rotation = rotation
        self.hType = hType
        self.accelProfile = AccelerationProfile(self.movement, accelerationProfile)

        self.maxL = max(size[0], size[1])

    def updateMovement(self):
        self.movement.updatePosition()

    def updateRotation(self, newRotation):
        self.rotation = newRotation

    def updateAcceleration(self, accelParams):
        self.accelProfile.updateAcceleration(accelParams)

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.skin, self.rotation)
        if(self.hType):
            #circle
            screen.blit(rotated, self.movement.x - self.size[0] // 2, self.movement.y - self.size[0] // 2)
        else:
            #rectangle
            skinW = rotated.get_width()
            skinH = rotated.get_height()
            screen.blit(rotated, self.movement.x - skinW // 2, self.movement.y - skinH // 2)

    def isInside(self, size):
        # size = (screen width, screen height)
        return self.movement.x + self.maxL > 0 and self.movement.x - self.maxL < size[0] and self.movement.y + self.maxL > 0 and self.movement.y - self.maxL < size[1] 

    def getHitbox(self):

        if(self.hType):
            return CircleHB(self.movement.x, self.movement.y, self.size[0])
        else:
            xOff = self.size[0] // 2
            yOff = self.size[1] // 2
            p1 = (self.movement.x - xOff, self.movement.y - yOff)
            p2 = (self.movement.x + xOff, self.movement.y - yOff)
            p3 = (self.movement.x - xOff, self.movement.y + yOff)
            p4 = (self.movement.x + xOff, self.movement.y + yOff)
            p1 = rotate_around_point_highperf(p1, self.rotation, self.movement.x, self.movement.y)
            p2 = rotate_around_point_highperf(p2, self.rotation, self.movement.x, self.movement.y)
            p3 = rotate_around_point_highperf(p3, self.rotation, self.movement.x, self.movement.y)
            p4 = rotate_around_point_highperf(p4, self.rotation, self.movement.x, self.movement.y)
            return RectangleHB(p1, p2, p3, p4)


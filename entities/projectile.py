import pygame
import math
from entities.entity import Entity
from logic.accelerationProfile import ZeroProfile
from logic.collision import normalize

class Projectile(Entity):

    def __init__(self, skin, size, hType, x, y, vel, acc, damage):
        rotation = math.degrees(math.atan(vel[1] / vel[0]))
        super(skin, size, hType, x, y, vel, acc, ZeroProfile(), rotation)
        self.damage = damage

    def entityHitCheck(self, entityHB, entityEffectEH):
        hitQ = self.didHit(entityHB)
        if(hitQ):
            entityEffectEH(self.damage)
            return True
        else:
            return False

    

    
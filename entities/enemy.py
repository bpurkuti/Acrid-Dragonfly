import pygame
from entities.entity import Entity
from entities.gun import Gun
import math

class Enemy(Entity):

    def __init__(self, skin, size, hType, x, y, vel, acc, accelerationProfile, health, projectileSkin, projectileSize, speed, damage, fireRate, dieEH, hitPlayerEH):
        rotation = math.degrees(math.atan(vel[1] / vel[0]))
        super(skin, size, hType, x, y, vel, acc, accelerationProfile, rotation)
        self.gun = Gun(self, projectileSkin, projectileSize, hType, fireRate)
        self.speed = speed
        self.damage = damage
        self.health = health
        self.dieEH = dieEH

    def updateRotation(self):
        self.rotation = math.degrees(math.atan(self.vel[1] / self.vel[0]))

    def takeDamage(self, damage):
        self.health = self.health - damage
        if(self.health <= 0):
            self.dieEH()
            return True
        else:
            return False

    def fireProjectile(self):
        return self.gun.fireProjectile(self.speed, self.damage)

    
import pygame
from entities.entity import Entity
from logic.accelerationProfile import BasicProfile
from entities.playerSkinLoop import PlayerSkinLoop
from entities.gun import Gun

class Player(Entity):

    def __init__(self, skins, skinDelay, size, hType, x, y, vel, acc, rotation, maxAcc, decreAcc, health, projectileSkin, projectileSize, pj_hType, speed, damage, fireRate, gameOverEH):
        super(skins[0], size, hType, x, y, vel, acc, BasicProfile(maxAcc, decreAcc))
        self.gun = Gun(self, projectileSkin, projectileSize, pj_hType, damage, fireRate)
        self.skinLoop = PlayerSkinLoop(skins, skinDelay)
        self.health = health
        self.gameOverEH = gameOverEH
        self.score = 0

    def takeDamage(self, damage):
        self.health = self.health - damage
        if(self.health <= 0):
            self.gameOverEH(self.score)

    def draw(self, screen):
        self.skinLoop.tick()
        self.skin = self.skinLoop.getCurrentSkin()
        super.draw(screen)
    
    def fireProjectile(self):
        return self.gun.fireProjectile(self.speed, self.damage)
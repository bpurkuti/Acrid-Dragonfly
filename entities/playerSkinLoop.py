import pygame

class PlayerSkinLoop(object):

    def __init__(self, skins, delay):
        self.skins = skins
        self.delay = delay
        self.tickCount = 0
        self.spriteIndex = 0
        self.spritesLength = len(skins)

    def tick(self):
        self.tickCount = (self.tickCount + 1) % self.delay
        if(self.tickCount == 0):
            self.spriteIndex = (self.spriteIndex + 1) % self.spritesLength

    def getCurrentSkin(self):
        return self.skins[self.spriteIndex]


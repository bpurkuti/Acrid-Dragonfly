import pygame

class ScoreBoard(object):

    def __init__(self, x, y, fontSize):
        self.x = x
        self.y = y
        self.score = 0

        self.font = pygame.font.SysFont('arial', fontSize)
        self.fontColor = (0,0,0)
        self.outlineColor = (255,255,255)

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def draw(self, screen):
        text = self.font.render('Score: ' + str(self.score), 1, self.fontColor)
        textW = self.font.render('Score: ' + str(self.score), 1, self.outlineColor)
        for i in range(-1,2):
            for j in range(-1,2):
                screen.blit(textW, (self.x + i, self.y + j))
                
        screen.blit(text, (self.x, self.y))
import pygame
import pygame.gfxdraw
import random

class Item(object):

    def __init__(self, x, y, length, vel, color):
        self.x = x
        self.y = y
        self.vel = vel
        self.length = length
        self.color = color

    def move(self):
        self.y = self.y + self.vel

class Asteroid(Item):

    def draw(self, screen):
        pygame.gfxdraw.box(screen, pygame.Rect(self.x,self.y,self.length,self.length), self.color)

class Star(Item):
    
    def draw(self, screen):
        x1 = self.x
        y1 = self.y + self.length
        x2 = self.x + self.length // 2
        y2 = self.y
        x3 = self.x + self.length
        y3 = self.y + self.length
        pygame.gfxdraw.filled_trigon(screen, x1, y1, x2, y2, x3, y3, self.color)



class SpaceBackground(object):

    def __init__(self, scale, screen):

        self.scale = scale
        self.screen = screen

        # screen width, height, and lists for holding asteroid and stars
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.asteroids = []
        self.stars = []

        # ------------ INNER SETTINGS ------------

        # maximum count for items
        self.asteroidCount = 30
        self.starCount = 30

        # size range of items
        self.asteroidBound = (30, 60)
        self.starBound = (70, 100)

        # velocity range of items
        self.velAsteroidBound = (15, 30)
        self.velStarBound = (5, 15)

        # opacity range of items
        self.opAsteroidBound = (50, 80)
        self.opStarBound = (30, 40)

        # items colors, asteroid only has one, star can be random one in list
        self.colorAsteroid = (255, 255, 255)
        self.colorStar = ((255, 0, 0), (0, 255, 0), (255, 102, 0), (255, 255, 0))

        # limit respawn of items
        self.asteroidAddWait = 10
        self.starAddWait = 20

        # beginning draw
        self.beginLimit = 50
        
        # ------------ INNER SETTINGS END ------------

        # scaling

        self.asteroidBound = (int(self.asteroidBound[0] * scale), int(self.asteroidBound[1] * scale))
        self.starBound = (int(self.starBound[0] * scale), int(self.starBound[1] * scale))
        self.velAsteroidBound = (int(self.velAsteroidBound[0] * scale), int(self.velAsteroidBound[1] * scale))
        self.velStarBound = (int(self.velStarBound[0] * scale), int(self.velStarBound[1] * scale))

        self.asteroidWait = 0
        self.starWait = 0
    
        self.limitCounter = 0
        self.canDraw = False

    # delete items outside of window
    def checkItems(self):

        iOff = 0
        for i in range(0, len(self.stars)):
            star = self.stars[i - iOff]
            if(star.y + star.length > self.height):
                del self.stars[i - iOff]
                iOff = iOff + 1

        jOff = 0
        for j in range(0, len(self.asteroids)):
            asteroid = self.asteroids[j - jOff]
            if(asteroid.y + asteroid.length > self.height):
                del self.asteroids[j - jOff]
                jOff = jOff + 1 

    # handling respawn of items
    def addItems(self):

        self.starWait = (self.starWait + 1) % self.starAddWait
        self.asteroidWait = (self.asteroidWait + 1) % self.asteroidAddWait

        if len(self.asteroids) < self.asteroidCount and self.asteroidWait == 0:
            
            aLength = random.randint(self.asteroidBound[0], self.asteroidBound[1])
            aVel = random.randint(self.velAsteroidBound[0], self.velAsteroidBound[1])
            aOp = self.opAsteroidBound[0] + (self.opAsteroidBound[1] - self.opAsteroidBound[0]) * (self.velAsteroidBound[1] - aVel) // int(self.velAsteroidBound[1] - self.velAsteroidBound[0])

            aX = random.randint(0, self.width - aLength)
            aY = 0 - aLength
            aColor = (self.colorAsteroid[0], self.colorAsteroid[1], self.colorAsteroid[2], aOp)

            aI = Asteroid(aX, aY, aLength, aVel, aColor)
            self.asteroids.append(aI)

        if len(self.stars) < self.starCount and self.starWait == 0:
            
            sLength = random.randint(self.starBound[0], self.starBound[1])
            sVel = random.randint(self.velStarBound[0], self.velStarBound[1])
            sOp = self.opStarBound[0] + (self.opStarBound[1] - self.opStarBound[0]) * (self.velStarBound[1] - sVel) // int(self.velStarBound[1] - self.velStarBound[0])

            sX = random.randint(0, self.width - sLength)
            sY = 0 - sLength
            sColor = self.colorStar[random.randint(0, len(self.colorStar) - 1)]
            sColor = (sColor[0], sColor[1], sColor[2], sOp)

            sI = Star(sX, sY, sLength, sVel, sColor)
            self.stars.append(sI)

    # move items by velocity
    def moveItems(self):

        for asteroid in self.asteroids:
            asteroid.move()

        for star in self.stars:
            star.move()

    # drawing items onto screen
    def draw(self):

        for asteroid in self.asteroids:
            asteroid.draw(self.screen)
            #a = asteroid
            #print(a.x,a.y,a.length,a.color,a.vel)
        for star in self.stars:
            star.draw(self.screen)
            #s = star
            #print(s.x,s.y,s.length,s.color,s.vel)

        #print(len(self.stars))

        #if(len(self.stars) == 30):
            #for s in self.stars:
                #print(s.x,s.y,s.length,s.color,s.vel)
            #sys.exit()

    # update items
    def updateItems(self):

        if(not self.canDraw):
            if(self.limitCounter > self.beginLimit):
                self.canDraw = True
            else:
                self.limitCounter = self.limitCounter + 1

        self.moveItems()
        self.checkItems()
        self.addItems()
        if(self.canDraw):
            self.draw()
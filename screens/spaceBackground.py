import pygame
import pygame.gfxdraw
import random
import pygameUtils

ASSETS = {
    'images': {
        'stars': {},
        'asteroids': {}
    }
}
ASSETS['images']['stars']['raw'] = [pygame.image.load('bg/star_blue.bmp'), pygame.image.load('bg/star_red.bmp')]
ASSETS['images']['stars']['sizes'] = ((12, 12), (16, 16), (20, 20))
ASSETS['images']['stars']['trans'] = []

ASSETS['images']['asteroids']['raw'] = [pygame.image.load('bg/asteroid.bmp'), pygame.image.load('bg/asteroid2.png'), pygame.image.load('bg/asteroid3.png')]
ASSETS['images']['asteroids']['sizes'] = ((16, 16), (24, 24), (32, 32), (40, 40), (48, 48))
ASSETS['images']['asteroids']['trans'] = []

for raw_image in ASSETS['images']['stars']['raw']:
    for size in ASSETS['images']['stars']['sizes']:
        transformed = {'image': pygame.transform.scale(raw_image, size), 'size': size}
        ASSETS['images']['stars']['trans'].append(transformed)

for raw_image in ASSETS['images']['asteroids']['raw']:
    for size in ASSETS['images']['asteroids']['sizes']:
        transformed = {'image': pygame.transform.scale(raw_image, size), 'size': size}
        ASSETS['images']['asteroids']['trans'].append(transformed)



class Item(object):

    def __init__(self, x, y, length, vel, image, alpha):
        self.x = x
        self.y = y
        self.vel = vel
        self.length = length
        self.image = image
        self.alpha = alpha

    def move(self):
        self.y = self.y + self.vel

class Asteroid(Item):

    def draw(self, screen):
        pygameUtils.blit_alpha(screen, self.image, (self.x, self.y), self.alpha)

class Star(Item):
    
    def draw(self, screen):
        pygameUtils.blit_alpha(screen, self.image, (self.x, self.y), self.alpha)



class SpaceBackground(object):

    def __init__(self, screen, scale, beginLimit):

        self.scale = scale
        self.screen = screen

        # screen width, height, and lists for holding asteroid and stars
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.asteroids = []
        self.stars = []

        self.SCALED_ASSETS = ASSETS
        
        for i in range(0, len(self.SCALED_ASSETS['images']['stars']['trans'])):
            image = self.SCALED_ASSETS['images']['stars']['trans'][i]
            size = (image['size'][0] * self.scale, image['size'][0] * self.scale)
            size = (int(size[0]), int(size[1]))
            image = pygame.transform.scale(image['image'], size)
            image = pygame.transform.rotate(image, random.randint(0, 359))
            self.SCALED_ASSETS['images']['stars']['trans'][i] = {'image': image, 'size': size}
        for i in range(0, len(self.SCALED_ASSETS['images']['asteroids']['trans'])):
            image = self.SCALED_ASSETS['images']['asteroids']['trans'][i]
            size = (image['size'][0] * self.scale, image['size'][0] * self.scale)
            size = (int(size[0]), int(size[1]))
            image = pygame.transform.scale(image['image'], size)
            image = pygame.transform.rotate(image, random.randint(0, 359))
            self.SCALED_ASSETS['images']['asteroids']['trans'][i] = {'image': image, 'size': size}

        # ------------ INNER SETTINGS ------------

        # maximum count for items
        self.asteroidCount = 30
        self.starCount = 30

        # velocity range of items
        self.velAsteroidBound = (6, 9)
        self.velStarBound = (3, 6)

        # opacity range of items
        self.opAsteroidBound = (100, 120)
        self.opStarBound = (200, 255)

        # limit respawn of items
        self.asteroidAddWait = 10
        self.starAddWait = 20

        # beginning draw
        self.beginLimit = beginLimit
        
        # ------------ INNER SETTINGS END ------------

        # scaling
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
            if(star.y > self.height):
                del self.stars[i - iOff]
                iOff = iOff + 1

        jOff = 0
        for j in range(0, len(self.asteroids)):
            asteroid = self.asteroids[j - jOff]
            if(asteroid.y > self.height):
                del self.asteroids[j - jOff]
                jOff = jOff + 1 

    # handling respawn of items
    def addItems(self):

        self.starWait = (self.starWait + 1) % self.starAddWait
        self.asteroidWait = (self.asteroidWait + 1) % self.asteroidAddWait

        if len(self.asteroids) < self.asteroidCount and self.asteroidWait == 0:
            
            aImage = self.SCALED_ASSETS['images']['asteroids']['trans'][ random.randint(0, len(self.SCALED_ASSETS['images']['asteroids']['trans'])-1) ]
            aLength = aImage['size'][0]
            aVel = random.randint(self.velAsteroidBound[0], self.velAsteroidBound[1])
            aOp = self.opAsteroidBound[0] + (self.opAsteroidBound[1] - self.opAsteroidBound[0]) * (self.velAsteroidBound[1] - aVel) // int(self.velAsteroidBound[1] - self.velAsteroidBound[0])

            aX = random.randint(0, self.width - aLength)
            aY = 0 - aLength

            aI = Asteroid(aX, aY, aLength, aVel, aImage['image'], aOp)
            self.asteroids.append(aI)

        if len(self.stars) < self.starCount and self.starWait == 0:
            
            sImage = self.SCALED_ASSETS['images']['stars']['trans'][ random.randint(0, len(self.SCALED_ASSETS['images']['stars']['trans']) - 1) ]
            sLength = sImage['size'][0]
            sVel = random.randint(self.velStarBound[0], self.velStarBound[1])
            sOp = self.opStarBound[0] + (self.opStarBound[1] - self.opStarBound[0]) * (self.velStarBound[1] - sVel) // int(self.velStarBound[1] - self.velStarBound[0])

            sX = random.randint(0, self.width - sLength)
            sY = 0 - sLength

            sI = Star(sX, sY, sLength, sVel, sImage['image'], sOp)
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
import pygame
import math

class CircleImageButton(object):

    def __init__(self, length, imageUp, imageDown, onClick):

        self.length = length
        self.imageUp = pygame.transform.scale(imageUp, (self.length, self.length))
        self.imageDown = pygame.transform.scale(imageDown, (self.length, self.length))
        self.onClick = onClick
        self.buttonState = False

    def onMouseDown(self):
        self.buttonState = True

    def onMouseUp(self):
        self.onClick()

    def checkClick(self, position, eventType, buttonOffset):
        # should be called upon MOUSE_UP

        x = position[0]
        y = position[1]
        xOff = buttonOffset[0]
        yOff = buttonOffset[1]
        xMid = xOff + self.length // 2
        yMid = yOff + self.length // 2
        xDis = abs(xMid - x)
        yDis = abs(yMid - y)
        dis = int(math.sqrt(xDis * xDis + yDis * yDis))

        print(x,y,xOff,yOff,xMid,yMid,xDis,yDis,dis)

        if(eventType == pygame.MOUSEBUTTONUP):
            self.buttonState = False
            
        if(dis < self.length // 2):
            if(eventType == pygame.MOUSEBUTTONUP):
                self.onMouseUp()
            elif(eventType == pygame.MOUSEBUTTONDOWN):
                self.onMouseDown()

    def draw(self, screen, offset):
        image = self.imageUp
        if(self.buttonState):
            image=self.imageDown
        screen.blit(image, offset)
import pygame
from screens.circleButton import CircleImageButton

BUTTON_IMAGES = (
    pygame.image.load('screens/buttons/greenUp.png'),
    pygame.image.load('screens/buttons/greenDown.png')
)

class StartScreen(object):

    def __init__(self, screen, playEV):
        self.playEV = playEV
        self.screen = screen

        self.width = screen.get_width()
        self.height = screen.get_height()

        self.scaleCalculations()

    def handleClick(self, position, eventType):
        self.playButton.checkClick(position, eventType, self.buttonOffset)

    def scaleCalculations(self):

        minSize = min(self.width, self.height)
        buttonSize = minSize // 3

        self.buttonOffset = (
            self.width // 2 - buttonSize // 2,
            7 * self.height // 10 - buttonSize // 2
        )

        self.playButton = CircleImageButton(buttonSize, BUTTON_IMAGES[0], BUTTON_IMAGES[1], self.playEV)

        self.logo = pygame.image.load('screens/logo.png')
        logoW = self.logo.get_width()
        logoH = self.logo.get_height()
        logoScaleF = 0.75 * self.width / logoW

        logoW = int(logoW * logoScaleF)
        logoH = int(logoH * logoScaleF)
        self.logo = pygame.transform.scale(self.logo, (logoW, logoH))

        self.logoOffset = (
            self.width // 2 - logoW // 2,
            self.height // 4 - logoH // 2
        )

    def draw(self):
        self.screen.blit(self.logo, self.logoOffset)
        self.playButton.draw(self.screen, self.buttonOffset)



    
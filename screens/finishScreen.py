import pygame
from screens.circleButton import CircleImageButton

BUTTON_IMAGES = (
    pygame.image.load('screens/buttons/greenUp.png'),
    pygame.image.load('screens/buttons/greenDown.png'),
    pygame.image.load('screens/buttons/redUp.png'),
    pygame.image.load('screens/buttons/redDown.png')
)

class FinishScreen(object):

    def __init__(self, screen, score, playAgainEV, quitEV):
        self.score = score
        self.playAgainEV = playAgainEV
        self.quitEV = quitEV
        self.screen = screen

        self.width = screen.get_width()
        self.height = screen.get_height()

        self.fontColor = (255, 255, 255)

        self.scaleCalculations()

    def handleClick(self, position, eventType):
        self.playAgainButton.checkClick(position, eventType, self.buttonOffsets[0])
        self.quitButton.checkClick(position, eventType, self.buttonOffsets[1])

    def registerFont(self):

        font = pygame.font.SysFont('arial', 1024, 1)
        txt = font.render('Score: ' + str(self.score), 1, self.fontColor)
        return txt

    def scaleCalculations(self):

        minSize = min(self.width, self.height)
        buttonSize = minSize // 5

        fourthsW = (self.width // 4, 2 * self.width // 4, 3 * self.width // 4)
        fourthsH = (self.height // 4, 2 * self.height // 4, 3 * self.height // 4)

        self.buttonOffsets = (
            (fourthsW[0] - buttonSize // 2, fourthsH[2] - buttonSize // 2),
            (fourthsW[2] - buttonSize // 2, fourthsH[2] - buttonSize // 2)
        )

        self.playAgainButton = CircleImageButton(buttonSize, BUTTON_IMAGES[0], BUTTON_IMAGES[1], self.playAgainEV)
        self.quitButton = CircleImageButton(buttonSize, BUTTON_IMAGES[2], BUTTON_IMAGES[3], self.quitEV)

        self.txt = self.registerFont()

        txtW = self.txt.get_width()
        txtH = self.txt.get_height()
        txtScaleF = 0.3 * self.width / txtW

        txtW = int(txtW * txtScaleF)
        txtH = int(txtH * txtScaleF)
        self.txt = pygame.transform.scale(self.txt, (txtW, txtH))

        self.txtOffset = (
            self.width // 2 - txtW // 2,
            fourthsH[1] - txtH // 2
        )

        self.logo = pygame.image.load('screens/logo.png')
        logoW = self.logo.get_width()
        logoH = self.logo.get_height()
        logoScaleF = 0.6 * self.width / logoW

        logoW = int(logoW * logoScaleF)
        logoH = int(logoH * logoScaleF)
        self.logo = pygame.transform.scale(self.logo, (logoW, logoH))

        self.logoOffset = (
            self.width // 2 - logoW // 2,
            fourthsH[0] - logoH // 2
        )


    def draw(self):
        self.screen.blit(self.logo, self.logoOffset)
        self.screen.blit(self.txt, self.txtOffset)
        self.playAgainButton.draw(self.screen, self.buttonOffsets[0])
        self.quitButton.draw(self.screen, self.buttonOffsets[1])



    
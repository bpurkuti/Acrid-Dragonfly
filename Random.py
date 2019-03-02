import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption('Jaime Game')

gameExit = False

lead_x = 300
lead_y = 600
lead_x_change = 0

clock = pygame.time.Clock()


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    lead_x += lead_x_change
    gameDisplay.fill(red)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,50,50])
    pygame.display.update()

    clock.tick(30)


pygame.quit()
quit()

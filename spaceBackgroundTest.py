import pygame
from spaceBackground import Star, SpaceBackground
#from testCharacter import player
pygame.init()

WIN_SPEC = (600, 700)

running = True

screen = pygame.display.set_mode(WIN_SPEC)
clock = pygame.time.Clock()

ast = Star(50, 50, 25, 3, (255, 255, 255, 30))
#p1= player(300,410,64,64)
bg = SpaceBackground(0.5, screen)

while running:

    clock.tick(60)

    screen.fill((24,24,24))

    ast.draw(screen)
    bg.updateItems()
   # p1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys= pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()


pygame.quit()
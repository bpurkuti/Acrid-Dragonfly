import pygame
from spaceBackground import Star, SpaceBackground

pygame.init()

WIN_SPEC = (1200, 800)

running = True

screen = pygame.display.set_mode(WIN_SPEC)
clock = pygame.time.Clock()

ast = Star(50, 50, 25, 3, (255, 255, 255, 30))

bg = SpaceBackground(0.75, screen)

while running:

    clock.tick(1000)

    screen.fill((24,24,24))

    ast.draw(screen)
    bg.updateItems()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
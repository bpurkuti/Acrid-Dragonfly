import pygame
from scoreBoard import ScoreBoard
from imageSpaceBackground import Star, SpaceBackground

pygame.init()

WIN_SPEC = (1200, 800)

running = True

screen = pygame.display.set_mode(WIN_SPEC)
clock = pygame.time.Clock()

scoreB = ScoreBoard(100, 100)
score = 0
scoreB.setScore(score)

bg = SpaceBackground(screen, 1, 0)

while running:

    clock.tick(60)

    screen.fill((24,24,24))

    score = score + 1
    scoreB.setScore(score)
    scoreB.draw(screen)
    bg.updateItems()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
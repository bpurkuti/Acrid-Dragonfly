import pygame
from screens import SpaceBackground, FinishScreen, ScoreBoard, StartScreen

pygame.init()

pygame.mixer.init()
<<<<<<< Updated upstream
pygame.mixer.music.load('Space2.mp3')
pygame.mixer.music.set_volume(0.2) # volume of the son
=======
pygame.mixer.music.load('music/Space2.mp3')
pygame.mixer.music.set_volume(0.2)
>>>>>>> Stashed changes
pygame.mixer.music.play(-1)

WIN_SPEC = (800, 600)

running = True

screen = pygame.display.set_mode(WIN_SPEC)
clock = pygame.time.Clock()

scoreB = ScoreBoard(25, 25, 36)
score = 0
scoreB.setScore(score)

bg = SpaceBackground(screen, 1, 0)

def logClick():
    print('clicked')

def quit():
    global running
    running = False



sn = StartScreen(screen, logClick)
fn = FinishScreen(screen, 10000000000000, logClick, quit)

while running:
<<<<<<< Updated upstream
    #FPS
    clock.tick(60)
=======

    clock.tick(30)
>>>>>>> Stashed changes

    screen.fill((24,24,24))

    score = score + 1
    scoreB.setScore(score)
    scoreB.draw(screen)
    bg.updateItems()
    #fn.draw()
    sn.draw()
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN):
            position = pygame.mouse.get_pos()
            #fn.handleClick(position, event.type)
            sn.handleClick(position, event.type)
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
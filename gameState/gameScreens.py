import pygame
from screens import *

running = True
def leave():
    global running
    running = False

def start(changeGM, clock, BSG, screen):
    global running
    SS = StartScreen(screen, leave)
    while running:
        
        print(running)
        clock.tick(30)
        screen.fill((0,0,0))

        BSG.updateItems()
        SS.draw()

        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN):
                position = pygame.mouse.get_pos()
                SS.handleClick(position, event.type)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave()

    changeGM()

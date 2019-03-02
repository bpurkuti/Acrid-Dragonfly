import pygame, sys
pygame.init()

win = pygame.display.set_mode((800,600))

pygame.display.set_caption("The Game")


walkRight = pygame.image.load('test.png')
walkLeft = pygame.image.load('test.png')
bg = pygame.image.load('sky.jpg')
char = pygame.image.load('test.png')

clock = pygame.time.Clock()

x = 50
y = 50
width = 16
height = 16
vel = 15
left = False
right = False
walkCount = 0

def redrawGameWindow():
        global walkCount

        win.blit(bg, (0,0)
                 
        if walkCount + 1 >= 1 :
                walkCount = 0
        if left:
                win.blit(walkLeft{walkCount//3])
                walkCount += 1
        elif right:
                win.blit(walkRight{walkCount//3])
                walkCount += 1
        else:
                win,blit(char, (x,y)
                 
        pygame.display.update()



#the game stuff
run = True
while run:
        clock.tick(30)
        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        keys = pygame.key.get_pressed()
        

        if keys  [pygame.K_LEFT] and x > vel:
                x -= vel
                 left = True
                 right = False
        elif keys  [pygame.K_RIGHT] and x < 800 - width - vel:
                x += vel
                 right = True
                 left = False
        else:
                 right = False
                 left = False
                 walkCount = 0
        if keys  [pygame.K_UP] and y > vel:
                y -= vel
        if keys  [pygame.K_DOWN] and y < 600 - height - vel:
                y += vel
                 # end of loop
        redrawGameWindow()
        
pygame.quit()

import pygame
import random
import sys
import time
import pyglet
from os import path
import string

## initialize pygame and create window
pygame.mixer.init()
pygame.init()

Sound = path.join(path.dirname(__file__), 'assets') # foler for sound
Pictures = path.join(path.dirname(__file__), 'sounds') # folder for images

WIDTH = 1000
HEIGHT = 800

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
darkBlue = (0,0,128)
BACKGROUND_COLOR = (155,205,155)
gray = (128,128,128)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

SPEED = 10
game_over = False
score = 0

# Play background music
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.set_volume(0.5) # volume of the son
pygame.mixer.music.play(-1) #loop the song

space = pygame.image.load('space.png')
#here we add if the scale is not K_RIGHT


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Acrid Dragon Flys')
clock = pygame.time.Clock()


myFont = pygame.font.SysFont("arial", 35)

def set_level(score, SPEED): # Speed of the game
	if score < 15:
		SPEED = 15
	elif score < 25:
		SPEED = 20
	elif score < 60:
		SPEED = 30
	elif score < 100:
			SPEED = 40
	elif score < 150:
			SPEED = 60
	elif score < 200:
			SPEED = 80
	else:
		SPEED = 90
	return SPEED
	# SPEED = score/5 + 1

def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			score += 1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_ESCAPE:
				pygame.quit() # event to exit game
			if event.key == pygame.K_LEFT: # move left
				x -= player_size
			elif event.key == pygame.K_RIGHT: # move right
				x += player_size
			elif event.key == pygame.K_UP: # move up
				y -= player_size
			elif event.key == pygame.K_DOWN: # move down
				y += player_size

			player_pos = [x,y]

	screen.fill(BACKGROUND_COLOR)

	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)

	text = "My Score: " + str(score)
	label = myFont.render(text, 1, darkBlue)
	screen.blit(label, (WIDTH-150, HEIGHT-30))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.ellipse(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)

	pygame.display.update()

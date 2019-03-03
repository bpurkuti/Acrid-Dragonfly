import pygame

spritePath = 'entities/sprites/enemy/'
ENEMIES = (
    (pygame.image.load(spritePath + 'skin1.png'), pygame.image.load(spritePath + 'skin2.png'), pygame.image.load(spritePath + 'skin1.png'), pygame.image.load(spritePath + 'skin3.png')),
    [0,1,2,3],
    (False, False, False, False)
)
for i in range(0, len(ENEMIES[0])):
    image = ENEMIES[0][i]
    ENEMIES[1][i] = (
        image.get_width(),
        image.get_height()
    )

spritePath = 'entities/sprites/projectiles/'
PROJECTILES = (
    (pygame.image.load(spritePath + 'fireball.png'), pygame.image.load(spritePath + 'missile.png'), pygame.image.load(spritePath + 'rocket.png')),
    [0,1,2],
    (True, False, False)
)
for i in range(0, len(PROJECTILES[0])):
    image = PROJECTILES[0][i]
    PROJECTILES[1][i] = (
        image.get_width(),
        image.get_height()
    )

spritePath = 'entities/sprites/player/'
PLAYERSKINS = (
    (pygame.image.load(spritePath + 'player1.png'), pygame.image.load(spritePath + 'player2.png'), pygame.image.load(spritePath + 'player3.png')),
    [0,1,2,3],
    (False, False, False, False)
)
for i in range(0, len(PLAYERSKINS[0])):
    image = PLAYERSKINS[0][i]
    PLAYERSKINS[1][i] = (
        image.get_width(),
        image.get_height()
    )

ENEMY_SKINS = ENEMIES
PROJECTILE_SKINS = PROJECTILES
PLAYER_SKINS = PLAYERSKINS
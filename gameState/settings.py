from gameState.loadSkins import *
from entities import *
import random

WIN_SIZE = (1200, 800)

MID = (WIN_SIZE[0] // 2, WIN_SIZE[1] // 2)
PLAYER_SETTINGS = [
    PLAYER_SKINS[0],
    10, PLAYER_SKINS[1][0], False,
    MID[0], MID[1], (5,5), 0, 0, 30, 1,
    100,
    PROJECTILE_SKINS[0][1], PROJECTILE_SKINS[1][1], PROJECTILE_SKINS[2][1],
    20, 50, 5
]


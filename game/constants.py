from enum import Enum
from pathlib import Path

import pygame

# Game constants
GAME_TITLE = "Snake game"
TILE_SIZE = 16
DISPLAY_WIDTH, DISPLAY_HEIGHT = 480, 480
FPS = 60
SNAKE_SPEED = 500
MAX_FRUIT_COUNT = 2
HORIZONTAL_BAR_HEIGHT = 25

# Colors
MAIN_SNAKE_COLOR = (255, 208, 0)
SECONDARY_SNAKE_COLOR = (189, 155, 4)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (0, 255, 0)
DARK_GREEN_COLOR = (0, 170, 0)

# Pathes
ASSETS_FOLDER_PATH = Path("assets")
IMAGES_FOLDER_PATH = Path(ASSETS_FOLDER_PATH, "images")
FRUITS_FOLDER_PATH = Path(IMAGES_FOLDER_PATH, "fruits")
SAVE_FILE_PATH = Path("save.pickle")
FONT_FOLDER_PATH = Path(ASSETS_FOLDER_PATH, "fonts")
FONT_FILE_PATH = Path(FONT_FOLDER_PATH, "PixeloidSansBold.ttf")


class Directions(Enum):
    IDLE = pygame.math.Vector2(0, 0)
    UP = pygame.math.Vector2(0, -1)
    DOWN = pygame.math.Vector2(0, 1)
    RIGHT = pygame.math.Vector2(1, 0)
    LEFT = pygame.math.Vector2(-1, 0)

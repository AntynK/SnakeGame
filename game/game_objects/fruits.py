import random
from pathlib import Path

import pygame

from game.constants import TILE_SIZE, FRUITS_FOLDER_PATH


class Fruit(pygame.sprite.Sprite):
    VALUE: int
    """This number will be added when snake eats fruit."""
    NAME = ""
    """Name of fruit image file."""

    def __init__(self, game_area: pygame.rect.Rect) -> None:
        """Base Fruit class.

        Arg:
            game_area: Area on which fruit can appear.
        """

        super().__init__()
        self.game_area = game_area
        self.image: pygame.surface.Surface = pygame.image.load(
            Path(FRUITS_FOLDER_PATH, f"{self.NAME}.png")
        ).convert_alpha()
        self.new_pos()

    def new_pos(self) -> None:
        """Change position of fruit."""

        self.rect: pygame.rect.Rect = pygame.rect.Rect(
            random.randrange(
                self.game_area.x + TILE_SIZE, self.game_area.width - TILE_SIZE
            ),
            random.randrange(
                self.game_area.y + TILE_SIZE, self.game_area.height - TILE_SIZE
            ),
            TILE_SIZE,
            TILE_SIZE,
        )

    def draw(self, display: pygame.surface.Surface):
        display.blit(self.image, self.rect)


class Apple(Fruit):
    """Inherited from Fruit class."""

    VALUE = 10
    NAME = "apple"


class Cherry(Fruit):
    """Inherited from Fruit class."""

    VALUE = 15
    NAME = "cherry"

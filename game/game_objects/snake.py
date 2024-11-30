from collections import deque
from pathlib import Path

import pygame

from game.game_objects.particles import TextParticle
from game.constants import (
    Directions,
    TILE_SIZE,
    MAIN_SNAKE_COLOR,
    SECONDARY_SNAKE_COLOR,
    SNAKE_SPEED,
    IMAGES_FOLDER_PATH,
)
from game.score import Score


class Snake(pygame.sprite.Sprite):
    def __init__(self, game, game_area: pygame.rect.Rect) -> None:
        """Snake class.

        Args:
            game: An instance of main game class.
            game_area: Area on which player plays, if player goes outside this area then game over.
        """

        super().__init__()
        self.direction: Directions = Directions.IDLE
        self.game_area = game_area

        self.pos = pygame.math.Vector2(game_area.width // 2, game_area.height // 2)
        self.body: deque[pygame.rect.Rect] = deque()
        self.body.append(pygame.rect.Rect(self.pos, (TILE_SIZE, TILE_SIZE)))
        self.rect: pygame.rect.Rect = pygame.rect.Rect(self.pos, (TILE_SIZE, TILE_SIZE))

        self.game = game
        """An instance of main game class."""
        self.score: Score = game.score
        self.collided = False
        self.image: pygame.surface.Surface = pygame.image.load(
            Path(IMAGES_FOLDER_PATH, "snake_head.png")
        )

    def update(self, fruits: pygame.sprite.Group, delta_time: float) -> None:
        """Update snake position and check collisions."""

        self.pos += self.direction.value * SNAKE_SPEED * delta_time
        self.rect.x, self.rect.y = self.pos.x, self.pos.y  # type: ignore
        self.check_collision()
        if self.collided:
            return

        self.body.appendleft(
            pygame.rect.Rect(self.pos, (TILE_SIZE, TILE_SIZE)),
        )

        if fruit := pygame.sprite.spritecollide(self, fruits, True):
            score = fruit[0].VALUE  # type: ignore
            self.score.add(score)
            TextParticle(self.game, self.pos.x, self.pos.y, 50, f"+{score}")  # type: ignore
        else:
            self.body.pop()

    def check_collision(self):
        """Check collision.

        Check if player goes outside game area or snake head collides with snake body.
        """

        if (
            self.pos.x > self.game_area.width + self.game_area.x / 1.5
            or self.pos.x < 0 + self.game_area.x / 1.5
        ):
            self.collided = True
        elif (
            self.pos.y > self.game_area.height + self.game_area.y / 1.5
            or self.pos.y < 0 + self.game_area.y / 1.5
        ):
            self.collided = True

        for index, rect in enumerate(self.body):
            if index != 0 and rect.collidepoint(
                *(self.pos + self.direction.value * TILE_SIZE)
            ):
                self.collided = True

    def draw(self, display: pygame.surface.Surface):
        for index, rect in enumerate(reversed(self.body)):
            if index == len(self.body) - 1:
                display.blit(self.image, rect)
                continue
            color = MAIN_SNAKE_COLOR if index % 2 == 1 else SECONDARY_SNAKE_COLOR
            pygame.draw.rect(display, color, rect)

    def set_direction(self, direction: Directions):
        """Change direction.

        Arg:
            direction: New snake direction.
        Raises:
            TypeError: If direction is not Directions type.
        """

        if not isinstance(direction, Directions):
            raise TypeError(f"Arg direction can be Directions, not {type(direction)}.")
        self.direction = direction

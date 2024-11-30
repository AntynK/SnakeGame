import random
from pathlib import Path

import pygame

from game.states.state import State
from game.states.pause import Pause
from game.states.game_over import GameOver
from game.ui import Text
from game.game_objects.snake import Snake
from game.game_objects.fruits import Apple, Cherry
from game.constants import (
    Directions,
    WHITE_COLOR,
    GREEN_COLOR,
    DARK_GREEN_COLOR,
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    MAX_FRUIT_COUNT,
    HORIZONTAL_BAR_HEIGHT,
    IMAGES_FOLDER_PATH,
    FRUITS_FOLDER_PATH,
)


class Game(State):
    def __init__(self, game) -> None:
        """Game state class.

        Inherited from State class.

        Arg:
            game: An instance of main game class.
        """

        super().__init__(game)
        self.game_area = pygame.rect.Rect(
            HORIZONTAL_BAR_HEIGHT,
            HORIZONTAL_BAR_HEIGHT,
            DISPLAY_WIDTH - HORIZONTAL_BAR_HEIGHT * 2,
            DISPLAY_HEIGHT - HORIZONTAL_BAR_HEIGHT * 2,
        )
        self.trophy_image = pygame.image.load(
            Path(IMAGES_FOLDER_PATH, "trophy.png")
        ).convert_alpha()
        self.apple_image = pygame.image.load(
            Path(FRUITS_FOLDER_PATH, "apple.png")
        ).convert_alpha()

        self.current_score_text = Text(70, 5, "0", font_size=15, font_color=WHITE_COLOR)
        self.record_score_text = Text(170, 5, "0", font_size=15, font_color=WHITE_COLOR)

        self.load()

    def event_handler(self, event: pygame.event.Event):
        """Handle events of current state.

        Override parent's method.

        This method is called from main game loop when event is received.
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Pause(self.game).enter_state()

            if event.key == pygame.K_UP and self.snake.direction is not Directions.DOWN:
                self.snake.set_direction(Directions.UP)
            elif (
                event.key == pygame.K_DOWN and self.snake.direction is not Directions.UP
            ):
                self.snake.set_direction(Directions.DOWN)
            elif (
                event.key == pygame.K_LEFT
                and self.snake.direction is not Directions.RIGHT
            ):
                self.snake.set_direction(Directions.LEFT)
            elif (
                event.key == pygame.K_RIGHT
                and self.snake.direction is not Directions.LEFT
            ):
                self.snake.set_direction(Directions.RIGHT)

    def update(self, delta_time: float):
        """Update current state.

        Override parent's method.

        This method is called from main loop game before draw method.

        Arg:
            delta_time: The time difference(in milliseconds) between the previous frame that was drawn and the current frame.
        """

        if len(self.fruits) < MAX_FRUIT_COUNT:
            self.fruits.add(random.choice([Apple, Cherry])(self.game_area))

        self.snake.update(self.fruits, delta_time)
        self.current_score_text.update_text(str(self.game.score.get_current()))
        self.record_score_text.update_text(str(self.game.score.get_record()))
        if self.snake.collided:
            self.game.score.save()
            GameOver(self.game).enter_state()

    def load(self):
        """Load state.

        Override parent's method.

        This method is called when state becomes active.
        """

        self.snake = Snake(self.game, self.game_area)
        self.fruits = pygame.sprite.Group()

        self.game.score.reset()

    def draw_score(self, display: pygame.surface.Surface):
        """Draw current score, record score and icons for them."""

        self.current_score_text.draw(display)
        display.blit(
            self.apple_image,
            (self.current_score_text.x - 32, self.current_score_text.y),
        )
        self.record_score_text.draw(display)
        display.blit(
            self.trophy_image, (self.record_score_text.x - 32, self.record_score_text.y)
        )

    def draw(self, display: pygame.surface.Surface):
        """Draw current state.

        Override parent's method.

        This method is called from main loop game after update method.
        """

        pygame.draw.rect(
            display, DARK_GREEN_COLOR, (0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        )
        pygame.draw.rect(display, GREEN_COLOR, self.game_area)
        self.draw_score(display)

        self.fruits.draw(display)

        self.snake.draw(display)

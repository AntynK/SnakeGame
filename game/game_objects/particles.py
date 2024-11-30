import pygame

from game.ui import Text
from game.constants import WHITE_COLOR


class Particle(pygame.sprite.Sprite):
    def __init__(self, game, x: int, y: int, duration: float) -> None:
        """Base particle class.

        Args:
            game: An instance of main game class.
            x,y: Position of particles.
            duration: Duration of particles.
        """

        super().__init__()
        self.particles: pygame.sprite.Group = game.particles
        self.particles.add(self)
        self.x, self.y = x, y
        self.rect: pygame.rect.Rect = pygame.rect.Rect(self.x, self.y, 1, 1)
        self.duration = duration

    def update(self, delta_time: float):
        """Update particles and delete them when duration time pass."""

        self.duration -= 100 * delta_time
        if self.duration <= 0:
            self.particles.remove(self)


class TextParticle(Particle):
    def __init__(
        self,
        game,
        x: int,
        y: int,
        duration: float,
        text: str,
        font_size: int = 10,
        font_color: tuple[int, int, int] = WHITE_COLOR,
    ) -> None:
        """TextParticle class.

        Args:
            game: An instance of main game class.
            x, y: Position of button.
            text: Text of the button.
            font_size: Text font size.
            font_color: Text color.
        """

        super().__init__(game, x, y, duration)
        self.text = Text(x, y, text, font_size, font_color)
        self.image: pygame.surface.Surface = self.text.pre_rendered_text

    def update(self, delta_time: float):
        """Update particles and fade text.

        Extends parent's method.
        """

        super().update(delta_time)
        self.rect.y -= 5 * delta_time  # type: ignore

        self.image.set_alpha(self.image.get_alpha() - 5)  # type: ignore

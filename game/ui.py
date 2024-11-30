from typing import Callable, Optional, Union

import pygame

from game.constants import BLACK_COLOR, WHITE_COLOR, FONT_FILE_PATH


class Text:
    def __init__(
        self,
        x: int,
        y: int,
        text: str,
        font_size: int = 20,
        font_color: tuple[int, int, int] = BLACK_COLOR,
    ) -> None:
        """Text class.

        Args:
            x, y: Position of button.
            text: Text of the button.
            font_size: Text font size.
            font_color: Text color.
        """

        self.x, self.y = x, y
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.pre_render()

    def pre_render(self):
        """Pre-render text and align text with coordinates."""

        font = pygame.font.Font(FONT_FILE_PATH, self.font_size)
        self.pre_rendered_text = font.render(self.text, True, self.font_color)
        self.rect = self.pre_rendered_text.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update_text(self, new_text: str):
        """Update text and pre-render it."""

        self.text = new_text
        self.pre_render()

    def draw(self, display: pygame.surface.Surface):
        display.blit(self.pre_rendered_text, self.rect)


class Button:
    def __init__(
        self,
        x: int,
        y: int,
        text: str,
        font_size: int = 20,
        font_color: tuple[int, int, int] = BLACK_COLOR,
        callback: Optional[Callable] = None,
    ) -> None:
        """Button class.

        Args:
            x, y: Position of button.
            text: Text of the button.
            font_size: Text font size.
            font_color: Text color.
            callback: When user clicks button 'callback' will be called.
        Raises:
            TypeError: If callback is not callable.
        """

        self.text = Text(x, y, text, font_size, font_color)
        self.x, self.y = x, y
        self.was_cursor_outside = False
        self.pre_render()
        self.callback: Union[Callable, None] = callback

        if self.callback is not None:
            if callable(callback):
                self.callback = callback
            else:
                raise TypeError("Argument 'callback' must be callable.")

    def pre_render(self):
        """Pre-render text and align button's position with text coordinates."""

        width, height = self.text.rect.width, self.text.rect.height
        self.rect = pygame.rect.Rect(self.x - 2, self.y, width + 2, height)
        self.outline_rect = pygame.rect.Rect(
            self.x - 4, self.y - 2, width + 6, height + 4
        )

    def draw(self, display: pygame.surface.Surface) -> bool:
        """Draw text on display.

        If user clicks on button it will return True or call callback.
        """

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(display, BLACK_COLOR, self.outline_rect, width=5)
            if pygame.mouse.get_pressed()[0] and self.was_cursor_outside:
                self.was_cursor_outside = False
                if self.callback is None:
                    return True
                self.callback()
        else:
            self.was_cursor_outside = True

        pygame.draw.rect(display, WHITE_COLOR, self.rect)
        display.blit(self.text.pre_rendered_text, (self.x, self.y))
        return False

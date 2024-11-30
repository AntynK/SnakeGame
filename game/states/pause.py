import pygame

from game.states.state import State
from game.ui import Text, Button
from game.constants import WHITE_COLOR


class Pause(State):
    def __init__(self, game) -> None:
        """Pause state class.

        Inherited from State class.

        Arg:
            game: An instance of main game class.
        """

        super().__init__(game)
        self.title_text = Text(
            150, 100, "Game paused", font_size=30, font_color=WHITE_COLOR
        )
        self.load()

    def event_handler(self, event: pygame.event.Event):
        """Handle events of current state.

        Override parent's method.

        This method is called from main game loop when event is received.
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.exit_state(False)
            elif event.key == pygame.K_ESCAPE:
                self.exit_state()
                self.exit_state()

    def load(self):
        """Load state.

        Override parent's method.

        This method is called when state becomes active.
        """

        self.resume_button = Button(200, 150, "Resume")
        self.exit_button = Button(200, 180, "Exit")

    def draw(self, display: pygame.surface.Surface):
        """Draw current state.

        Override parent's method.

        This method is called from main loop game after update method.
        """

        self.prev_state.draw(display)
        self.title_text.draw(display)

        if self.resume_button.draw(display):
            self.exit_state()
        if self.exit_button.draw(display):
            self.exit_state()
            self.exit_state()

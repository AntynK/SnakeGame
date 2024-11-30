import pygame

from game.states.state import State
from game.states.game import Game
from game.ui import Text, Button
from game.constants import WHITE_COLOR


class Title(State):
    def __init__(self, game) -> None:
        """Title state.

        Inherited from State class.

        Arg:
            game: An instance of main game class.
        """

        super().__init__(game)
        self.title_text = Text(
            150, 50, "Snake game", font_size=30, font_color=WHITE_COLOR
        )
        self.load()

    def load(self):
        """Load state.

        Override parent's method.

        This method is called when state becomes active.
        """

        self.start_button = Button(200, 150, "Start")
        self.exit_button = Button(200, 180, "Exit")

    def event_handler(self, event: pygame.event.Event):
        """Handle events of current state.

        Override parent's method.

        This method is called from main game loop when event is received.
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Game(self.game).enter_state()
            if event.key == pygame.K_ESCAPE:
                self.exit_state()

    def draw(self, display: pygame.surface.Surface):
        """Draw current state.

        Override parent's method.

        This method is called from main loop game after update method.
        """

        display.fill((0, 170, 0))
        self.title_text.draw(display)

        if self.exit_button.draw(display):
            self.exit_state()
        if self.start_button.draw(display):
            Game(self.game).enter_state()

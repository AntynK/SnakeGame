from typing import Any
from collections import deque

import pygame


class State:
    def __init__(self, game) -> None:
        """Base state class.

        Arg:
            game: An instance of main game class.
        """

        self.game = game
        """An instance of main game class."""

        self.state_stack: deque = game.state_stack
        self.prev_state: Any = None

    def load(self):
        """Load state.

        Does nothing, so you can override it. This method is called when state becomes active.
        """

        pass

    def event_handler(self, event: pygame.event.Event):
        """Handle events of current state.

        Does nothing, so you can override it. This method is called from main loop game when event is received.
        """

        pass

    def update(self, delta_time: float):
        """Update current state.

        Does nothing, so you can override it. This method is called from main loop game before draw method.

        Arg:
            delta_time: The time difference(in milliseconds) between the previous frame that was drawn and the current frame.
        """

        pass

    def draw(self, display: pygame.surface.Surface):
        """Draw current state.

        Does nothing, so you can override it. This method is called from main loop game after update method.
        """

        pass

    def enter_state(self):
        """Add state to state stack."""

        if len(self.state_stack) > 1:
            self.prev_state = self.state_stack[-1]
        self.state_stack.append(self)

    def exit_state(self, load_next_state: bool = True):
        """Pop state from state stack.

        If there is only one state in the state stack and this method is called, the game will be stopped.

        Arg:
            load_next_state: If True then next state load() method will be called. Defaults to True.
        """

        if len(self.state_stack) == 1:
            self.game.playing = False
        else:
            self.state_stack.pop()
            if load_next_state:
                self.state_stack[-1].load()

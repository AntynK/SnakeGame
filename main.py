import sys
from collections import deque

import pygame

from game.score import Score
from game.states.title import Title
from game.constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, FPS, GAME_TITLE


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.score = Score()

        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = True
        self.state_stack = deque()
        self.state_stack.append(Title(self))
        self.particles = pygame.sprite.Group()
        self.delta_time = 0

    def run(self):
        while self.playing:
            pygame.display.set_caption(GAME_TITLE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                self.state_stack[-1].event_handler(event)

            self.update()

            self.draw()

            pygame.display.update()
            self.delta_time = self.clock.tick(FPS) / 1000
        sys.exit()

    def update(self):
        """Update current state and particles."""

        self.state_stack[-1].update(self.delta_time)
        self.particles.update(self.delta_time)

    def draw(self):
        """Draw current state and particles."""

        self.state_stack[-1].draw(self.display)
        self.particles.draw(self.display)


if __name__ == "__main__":
    game = Game()
    game.run()

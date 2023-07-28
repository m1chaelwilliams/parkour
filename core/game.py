import pygame
from globals import *
from utils import *
from states import *
import sys

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        # *** special window config ***
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load(ICON).convert())
    def start(self):
        # start event polling
        EventHandler.init()

        self.states: dict[GameState, BaseState] = {
            GameState.MENU:Menu(self),
            GameState.WORLD:World(self)
        }
        self.active_state: GameState = GameState.MENU

        # game loop
        while self.IsOpen():
            self.update()
            self.draw()
        self.close()
    def update(self):
        EventHandler.poll_events()

        # --- updating logic ---
        self.states[self.active_state].update()

        self.clock.tick(FPS)
    def draw(self):

        # --- drawing logic ---
        self.states[self.active_state].draw()

        # update display
        pygame.display.update()
    def IsOpen(self) -> bool:
        for e in EventHandler.events:
            if e.type == pygame.QUIT:
                return False
        return True
    def close(self):
        self.states[self.active_state].close()
        pygame.quit()
        sys.exit()
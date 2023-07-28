import pygame

class BaseState:
    def __init__(self, app) -> None:
        self.app = app
        self.screen: pygame.Surface = app.screen
    def update(self):
        pass
    def draw(self):
        pass
    def close(self):
        pass
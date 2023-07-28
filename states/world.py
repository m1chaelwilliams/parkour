import pygame
from states.basestate import BaseState

class World(BaseState):
    def __init__(self, app) -> None:
        super().__init__(app)
    def draw(self):
        self.screen.fill('lightblue')
import pygame
from states.basestate import BaseState
from font.font import Font
from font.textbox import TextBox, BoundTextBox
from globals import *

class Menu(BaseState):
    def __init__(self, app) -> None:
        super().__init__(app)

        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.-,:+'!?0123456789"
        characters = [char for char in characters]
        self.font = Font('assets/fonts/custom_font.png', TILESIZE, characters)

        self.textbox = BoundTextBox("Hi, this is a group of scripts to speed up game dev! - Sphere", 
                               self.font, 
                               self.screen, 
                               pygame.Rect(0, 0, 600, 400),
                               (10, 10))
    def draw(self):
        self.screen.fill('red')

        self.textbox.run()
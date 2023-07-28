import pygame
from font.font import Font

class TextBox:
    def __init__(self, text: str, font: Font, display: pygame.Surface, position: tuple = (0,0), speed: int = 3) -> None:
        self.display = display
        self.font = font
        self.text = text
        self.speed = speed
        self.counter = 0
        self.text_range = 1
        self.char_count = len(text)
        self.position = position

        self.running = True
    def reset(self):
        self.counter = 0
        self.text_range = 1
        self.running = True
    def complete(self):
        self.text_range = self.char_count
    def run(self):
        self.counter += 1
        if self.counter > self.speed and self.text_range < self.char_count:
            self.counter = 0
            self.text_range += 1
        self.font.draw_paragraph(self.text[0:self.text_range], self.display, self.position)
        if self.text_range >= self.char_count:
            self.running = False

class BoundTextBox(TextBox):
    def __init__(self, text: str, font: Font, display: pygame.Surface, bounds: pygame.Rect, position: tuple = (0, 0), speed: int = 3) -> None:
        super().__init__(text, font, display, position, speed)
        self.rect = bounds
    def run(self):
        pygame.draw.rect(self.display, "black", self.rect)
        self.counter += 1
        if self.counter > self.speed and self.text_range < self.char_count:
            self.counter = 0
            self.text_range += 1
        self.font.draw_paragraph_within_bounds(self.text[0:self.text_range], self.display, self.position, self.rect)
        if self.text_range >= self.char_count:
            self.running = False
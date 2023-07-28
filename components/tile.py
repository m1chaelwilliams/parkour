import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups: list[pygame.sprite.Group], image: pygame.Surface, position: tuple):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
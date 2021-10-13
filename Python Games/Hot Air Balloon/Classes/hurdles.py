import pygame
from pygame.color import THECOLORS


class Hurdle(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load("Utils/Images/hurdle.png")
        self.image.set_colorkey(THECOLORS['white'])
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
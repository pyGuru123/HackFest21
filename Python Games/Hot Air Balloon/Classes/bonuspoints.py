import pygame
from pygame.color import THECOLORS


class Bonus(pygame.sprite.Sprite):
    """
    This is a bonus sprite for the game. Hitting on this sprite with balloon will give extra points.
    """

    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load("Utils/Images/bonus.png").convert()
        self.image.set_colorkey(THECOLORS['white'])
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
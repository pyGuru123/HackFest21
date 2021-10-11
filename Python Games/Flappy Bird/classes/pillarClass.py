from constants import WHITE, WINDOW_WIDTH
import pygame

class Pillar(pygame.sprite.Sprite):
    """
    This class renders the pillars (default uses Images/brick.png), and interactions are defined in update() from playstate.py
    """

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Images/brick.png")
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH + self.rect.width

        self.mask = pygame.mask.from_surface(self.image)
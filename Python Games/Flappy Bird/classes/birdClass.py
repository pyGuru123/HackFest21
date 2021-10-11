import pygame

from constants import *

class Bird(pygame.sprite.Sprite):
    """
    This class initializes the mechanics of the bird

    Parameters:
    pygame.sprite: This sprite is initialized in playstate.py and by default, draws from Images\bird1.png and bird2.png
    
    """
    def __init__(self):
        super().__init__()

        self.size = 40
        self.x = 200
        self.y = WINDOW_HEIGHT // 2 - self.size // 2
        self.color = BLUE

        self.image1 = pygame.image.load("Images\\bird1.png").convert()
        self.image2 = pygame.image.load("Images\\bird2.png").convert()
        # self.image1 = pygame.image.load("C:\\Users\\Rishikesh Kumar\\Dropbox\\My PC (LAPTOP-KP31EEKV)\\Desktop\Games\\flappyBird\\Images\\bird1.png").convert()
        # self.image2 = pygame.image.load("C:\\Users\\Rishikesh Kumar\\Dropbox\\My PC (LAPTOP-KP31EEKV)\\Desktop\Games\\flappyBird\\Images\\bird2.png").convert()
        self.image1.set_colorkey(WHITE)
        self.image2.set_colorkey(WHITE)

        self.flap = False

        if (self.flap) : self.image = self.image2
        else : self.image = self.image1

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)

        self.image = pygame.transform.scale(self.image, (50, 50))
    
    def make_flap(self):
        """
        By default this is false until called by update() in playstate.py, when the user inputs Spacebar kay
        """
        
        if self.flap : self.image = self.image2
        else : self.image = self.image1

        self.mask = pygame.mask.from_surface(self.image)
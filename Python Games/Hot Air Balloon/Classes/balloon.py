import pygame
from pygame.color import THECOLORS

class Balloon(pygame.sprite.Sprite):
    """
    This is our balloon class. Players will control this balloon with left and right arrow keys and save from getting touched to hurdles.
    """
    
    def __init__(self) -> None:
        super().__init__()
        
        self.image1 = pygame.image.load("Utils/Images/straight.png").convert()
        self.image2 = pygame.image.load("Utils/Images/left.png").convert()
        self.image3 = pygame.image.load("Utils/Images/right.png").convert()

        self.image = self.image1
        self.image.set_colorkey(THECOLORS['white'])
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
    
    def change(self, orient=None):
        if orient == "left": 
            self.image = self.image2
        elif orient == 'right':
            self.image = self.image3
        else : 
            self.image = self.image1


        self.image.set_colorkey(THECOLORS['white'])
import pygame

from GameConstants.constants import *

class Bubble():

    def __init__(self, width, height, color):
        super().__init__()

        self.width = width
        self.height = height
        self.color = color
        self.x = 0
        self.y = 0

        self.direction = 0
        self.speed = 0

    def render(self):
        global SCREEN


        # if (self.show) :
        pygame.draw.rect(SCREEN, self.color, [self.x, self.y, self.width, self.height])
    
    def update(self):

        self.x += self.speed * self.direction
import pygame
from GameConstants.constants import *

class Ball():

    def __init__(self, color):

        self.center = (0, 0)
        self. r = 5
        self.color = color
        self.speed = 0
        self.direction = [1, -1]
    
    def collides(self, obj):

        x,y = self.center

        if (x + self.r < obj.x - 5 or
            x - self.r > obj.x + obj.width + 5 or
            y + self.r < obj.y - 5 or
            y - self.r > obj.y + obj.height + 5) : return False
        
        return True
    
    def bounce(self, obj):

        x, y = self.center

        if x + self.r >= obj.x and x - self.r <= obj.x + obj.width : self.direction[1] *= -1
        if y + self.r >= obj.y and y - self.r <= obj.y + obj.height : self.direction[0] *= -1

        

    def render(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.r)
    
    def update(self):

        if self.center[0] <= self.r : self.direction[0] = 1
        if self.center[0] >= WINDOW_WIDTH - self.r : self.direction[0] = -1
        if self.center[1] - self.r <= 0 : self.direction[1] = 1

        x = self.center[0] + self.speed * self.direction[0]
        y = self.center[1] + self.speed * self.direction[1]

        self.center = (x, y)
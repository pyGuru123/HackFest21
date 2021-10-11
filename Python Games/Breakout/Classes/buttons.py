import pygame

from GameConstants.constants import *

BLACK = (0,0,0)

class Button:
    def __init__(self, x=0, y=0, text="Button",color=(255, 255, 255), color2=GRAY):  

        self.x = x
        self.y = y
        self.width = 100
        self.height = 50
        self.color = color
        self.text = text
        self.hover_color = color2
        self.temp = self.color
        
    def render(self):
        global SCREEN
        font = pygame.font.SysFont("Comic sans MS", 25)
        t = font.render(self.text, True, BLACK, self.color)
        textRect = t.get_rect()
        textRect.center = (self.x + self.width/2, self.y+self.height/2)
        if (textRect[2] > self.width) : self.width = textRect[2] + 20
        button = pygame.draw.rect(SCREEN, self.color, [self.x, self.y, self.width, self.height])
        SCREEN.blit(t, textRect)

    def update(self):
        
        if (self.hover()) : self.color = self.hover_color
        else : self.color = self.temp

        self.render()

    def hover(self):
        mouse = pygame.mouse.get_pos()

        return (mouse[0] >= self.x and mouse[0] <= self.x + self.width) and (mouse[1] >= self.y and mouse[1] <= self.y + self.height)

    def clicked(self):
        mouse = pygame.mouse.get_pressed()
        return (self.hover() and mouse[0])
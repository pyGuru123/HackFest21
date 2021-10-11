import pygame

from constants import *

class Button:

    def __init__(self, x=0, y=0, width=120, height=40, color2=BGC, color1=WHITE, text="Button"): 
        """
        By default, this renders a 3x1 button with parameters called from constants.py
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.text = text

        self.button = pygame.draw.rect(SCREEN, self.color2, [self.x, self.y, self.width, self.height])

    def render(self) :

        font = pygame.font.SysFont("Comic sans MS", int(0.70*self.height))
        txt = font.render(self.text, True, self.color1, self.color2)
        textRect = txt.get_rect()
        textRect.center = (self.x + self.width // 2, self.y + self.height // 2)

        self.button = pygame.draw.rect(SCREEN, self.color2, [self.x, self.y, self.width, self.height])
        SCREEN.blit(txt, textRect)

    def update(self) :
        self.render()

    def hover(self) :
        x,y = pygame.mouse.get_pos()

        return (x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height)

    def clicked(self) :
        a, b, c = pygame.mouse.get_pressed()

        return (self.hover and a)
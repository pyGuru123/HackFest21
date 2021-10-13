import pygame
from pygame.color import THECOLORS
from pygame.cursors import arrow, broken_x, diamond, sizer_x_strings, thickarrow_strings, tri_left, tri_right, ball
from Utils.functions import *

class Button:
    """
    This is a class which will render buttons on the screen.

    """

    def __init__(self, x=0, y=0, width=120, height=30, background=(0,0,0), color=(255, 255, 255), text="Button", screen=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background = background
        self.color = color
        self.text = text
        self.screen = screen

        self.box = pygame.Surface((self.width, self.height))
        self.box.fill(self.background)
        self.box_rect = self.box.get_rect()
        self.box_rect.center = (self.x, self.y)

    def render(self): 

        Write(screen=self.box, fontsize=int(0.70*self.height), text=self.text, color=self.color, background=self.background, center=True, x=self.width//2, y=self.height//2)
        self.screen.blit(self.box, self.box_rect)

    def update(self) : 

        # thickarrow_strings = [               #sized 24x24
        #     "XX                      ",
        #     "XX X                     ",
        #     "XXXX                    ",
        #     "XX.XX                   ",
        #     "XX..XX                  ",
        #     "XX...XX                 ",
        #     "XX....XX                ",
        #     "XX.....XX               ",
        #     "XX......XX              ",
        #     "XX.......XX             ",
        #     "XX........XX            ",
        #     "XX........XX X           ",
        #     "XX......XXXXX           ",
        #     "XX.XX X..XX              ",
        #     "XXXX XX..XX             ",
        #     "XX   XX..XX             ",
        #     "     XX..XX             ",
        #     "      XX..XX            ",
        #     "      XX..XX            ",
        #     "       XXXX             ",
        #     "       XX               ",
        #     "                        ",
        #     "                        ",
        #     "                        "]
            
        if self.hover() : pygame.mouse.set_cursor(pygame.cursors.tri_left)
        else : pygame.mouse.set_cursor(pygame.cursors.arrow)
        self.render()

    
    def hover(self) -> bool:
        x,y = pygame.mouse.get_pos()
        return (x >= self.box_rect.x and y >= self.box_rect.y and x <= self.box_rect.x + self.width and y <= self.box_rect.y + self.height)
    
    def clicked(self) -> bool:
        a, b, c = pygame.mouse.get_pressed()

        return a and self.hover()
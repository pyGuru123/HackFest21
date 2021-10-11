import pygame
from GameConstants.constants import *
from Functions.textfunctions import *

class Themeboard:

    def __init__(self, x=0, y=0, b_c=WHITE, s_c=WHITE, bl_c=WHITE, t_c=WHITE, count=0):

        self.count = count
        self.x = x
        self.y = y
        self.background_color = b_c
        self.slider_color = s_c
        self.ball_color = bl_c
        self.tile_color = t_c

        self.board_size = 60
        self.slider_dim = (40, 10)
        self.ball_radius = 5
        self.tile_size = 15

    def hover(self):
        mouse = pygame.mouse.get_pos()

        return (mouse[0] >= self.x and mouse[0] <= self.x + self.board_size) and (mouse[1] >= self.y and mouse[1] <= self.y + self.board_size)
    
    def render(self):
        global count_themeboard
        back = pygame.draw.rect(SCREEN, self.background_color, [self.x, self.y, self.board_size, self.board_size])
        print_text(str(self.count), WHITE, back.left-16, back.top, 16, False)
        s = pygame.draw.rect(SCREEN, self.slider_color, [back.center[0] - self.slider_dim[0] / 2, back.bottom - self.slider_dim[1], self.slider_dim[0], self.slider_dim[1]])
        b = pygame.draw.circle(SCREEN, self.ball_color, (s.center[0], s.top - self.ball_radius), self.ball_radius)
        t = pygame.draw.rect(SCREEN, self.tile_color, [back.center[0], back.top + 5, self.tile_size, self.tile_size])

    def clicked(self):
        mouse = pygame.mouse.get_pressed()
        return (self.hover() and mouse[0])
    
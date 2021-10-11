import pygame
from GameConstants.constants import *
from levels import *


#============= Text =====================#
def print_text(t, color, x,y, font_size, center=True):
    font = pygame.font.SysFont("Comic sans MS", font_size)
    text = font.render(t, True, color, BLACK)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    if center : SCREEN.blit(text, (textRect[0] - textRect[2] / 2, textRect[1] - textRect[3] / 2))
    else : SCREEN.blit(text, textRect)
#============= Text =====================#

def show_bubbles(level):
    if (level == 0) : return test()
    if (level == 1) : return level1()
    if (level == 2) : return level2()
    if (level == 3) : return level3()
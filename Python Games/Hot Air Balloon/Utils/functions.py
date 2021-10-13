import pygame

def Write(fnt="Comic sans MS", fontsize=24, text="Namastey!", color=(255, 255, 255), background=None, screen=None, x=0, y=0, center=False):
    """
    This funtion will write the text on the screen. 
    It takes as arguments:
        font
        fontsize
        text
        color
        background
        screen
        x
        y
        center -> This is check is the font is to be centered
    """


    f = pygame.font.Font("Utils/fonts/Roboto-Bold.ttf", fontsize)
    t = f.render(text, True, color, background)
    textRect = t.get_rect()
    if center : textRect.center = (x, y)
    screen.blit(t, textRect)
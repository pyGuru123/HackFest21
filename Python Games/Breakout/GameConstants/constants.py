import pygame

#================= COLORS ====================#
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 200)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
RED = (255, 0, 0)
DARKRED = (200, 0, 0)
CHOCOLATY = (210, 105, 30)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
LIGHTBLUE = (173, 216, 230)
DARKCYAN = (0, 139, 139)
#================= COLORS ===================#

#=============== GAME WINDOW =============#
LOGO = pygame.image.load("Images/logo.png")
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 750
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Breakout")
pygame.display.set_icon(LOGO)
clock = pygame.time.Clock()
#=============== GAME WINDOW =============#


#=============== SCORE WINDOW =============#
score_height = 50
score_color = BLACK
#=============== SCORE WINDOW =============#
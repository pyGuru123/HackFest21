import pygame

from statemachine import StateMachine

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# C      R  G  B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (0, 0, 255)
GREEN = (0, 255, 0)
RED =   (255, 0, 0)
BGC =   (76, 49, 49)

gStateMachine = StateMachine()

SCORE = 0
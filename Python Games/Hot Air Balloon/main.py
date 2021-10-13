from States.gameoverstate import GameOver
from States.playstate import Play
from States.countdownstate import Countdown
import pygame
from Classes.statemachine import StateMachine
from States.startstate import Start
import sys
from pygame.constants import QUIT
from pygame.color import THECOLORS

# This method is called to get started
pygame.init()

# variables for the width and height for our window (that is game screen)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750

# Making the screen and setting its caption
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hot Air Balloon")

# Game over variable game loop runs while it is false
GAME_OVER = False

# making a clock to used tick function
clock = pygame.time.Clock()

# Different game states
STATES = {
    "start" : Start(),
    'countdown' : Countdown(),
    "play" : Play(),
    "over" : GameOver()
}

# State changing machine
gstatemachine = StateMachine(STATES)

# changing first state to start
gstatemachine.change("start", 
                            screen = SCREEN,
                            wwidth = WINDOW_WIDTH,
                            wheight = WINDOW_HEIGHT,
                            gstatemachine=gstatemachine)

# Our game loop runs 60 times in a second
while not GAME_OVER:

    # event handling
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            GAME_OVER = True

    # filling the screen updating the current state and updating the screen
    SCREEN.fill(THECOLORS["black"])
    gstatemachine.update(events)
    pygame.display.update()

    # calling tick functinality
    clock.tick(60)
    

pygame.quit()
sys.exit()
import pygame

from GameConstants.constants import *
from GameConstants.variables import *
from statemachine import StateMachine
from States.TitleScreen import Title
from States.PlayScreen import Play
from States.WinScreen import Win
from States.GameOver import Over

pygame.init()

STATES = {
    "TitleScreen" : Title(),
    "play" : Play(),
    "win" : Win(),
    "over" : Over()
}

GAME_STATE_VARIABLES.states = STATES
GAME_STATE_VARIABLES.change("TitleScreen")

while not GAME_OVER:

    pressed_key = None
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            GAME_OVER = True
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT: pressed_key = "left"
            elif event.key == pygame.K_RIGHT : pressed_key = "right"
            else : pressed_key = event.unicode
        
        if event.type == pygame.KEYUP:

            pressed_key = "released"

    SCREEN.fill(BLACK)
    GAME_STATE_VARIABLES.update(pressed_key)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
quit()
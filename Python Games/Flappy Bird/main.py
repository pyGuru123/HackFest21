import pygame

from constants import *

from States.playstate import Play
from States.startstate import Start
from States.countdownstate import Countdown
from States.gameoverstate import GameOver

pygame.init()

STATES = {
    "start" : Start(),
    "play" : Play(),
    "countdown" : Countdown(),
    "gameover" : GameOver(),
}

gStateMachine.states = STATES
gStateMachine.change("start")

GAME_OVER = False

while not GAME_OVER:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            GAME_OVER = True
        
    SCREEN.fill(BGC)
    gStateMachine.update(events)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
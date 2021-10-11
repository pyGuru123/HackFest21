import pygame

from States.Baseclass import Base
from Functions.textfunctions import *
from GameConstants.constants import *
from GameConstants.variables import *
from Classes.buttons import Button


startbtn = Button(x = WINDOW_WIDTH // 2 - 200, y = WINDOW_HEIGHT // 2 + 200, text="Play Again", color=GREEN, color2 = DARKGREEN)
endbtn = Button(x = WINDOW_WIDTH // 2 + 100, y = WINDOW_HEIGHT // 2 + 200, text="Quit", color=RED, color2 = DARKRED)


class Over(Base):

    def __init__(self):
        super().__init__()

    def render(self):

        global startbtn, settingsbtn, endbtn, SCORE, HIGH_SCORE

        print_text("Game Over!", RED, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 72)
        
        startbtn.render()
        endbtn.render()

    def update(self, params):

        global startbtn, settingsbtn, endbtn, GAME_STATE_VARIABLES

        startbtn.update()
        endbtn.update()

        if startbtn.clicked() : GAME_STATE_VARIABLES.change("play")
        if endbtn.clicked() : 
            pygame.quit()
            quit()
        
        self.render()
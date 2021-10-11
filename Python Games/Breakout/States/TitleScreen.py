import pygame

from States.Baseclass import Base

from Functions.textfunctions import *

from GameConstants.constants import *
from GameConstants.variables import *

from Classes.buttons import Button


startbtn = Button(x = WINDOW_WIDTH // 2 - 200, y = WINDOW_HEIGHT // 2 + 200, text="Start", color=GREEN, color2 = DARKGREEN)
settingsbtn = Button(x = WINDOW_WIDTH // 2 - 50, y = WINDOW_HEIGHT // 2 + 200, text="Settings", color=BLUE, color2 = DARKBLUE)
endbtn = Button(x = WINDOW_WIDTH // 2 + 100, y = WINDOW_HEIGHT // 2 + 200, text="Quit", color=RED, color2 = DARKRED)


class Title(Base):

    def __init__(self):
        super().__init__()

        self.x = 100
        self.y = 100
        self.NAME = ""

    def render(self):

        global startbtn, settingsbtn, endbtn

        # (t, color, x,y, font_size, center=True)
        print_text(f"Enter your Name: {self.NAME}", GREEN, WINDOW_WIDTH//2, WINDOW_HEIGHT // 2 - 100, 24)
        print_text("Breakout", LIGHTBLUE, WINDOW_WIDTH//2, WINDOW_HEIGHT//2, 72)

        # Button(x, y, text, screen, color, hcolor)
        startbtn.render()
        endbtn.render()

    
    def update(self, params):

        global startbtn, settingsbtn, endbtn
        
        if params == '\x08' : self.NAME = self.NAME[:-1]
        elif (params != None and params != '\r' and 
            params != "released" and params != "left" and params != "right") : self.NAME += params

        startbtn.update()
        endbtn.update()

        if startbtn.clicked() : GAME_STATE_VARIABLES.change("play")
        if endbtn.clicked() : 
            pygame.quit()
            quit()

        self.render()

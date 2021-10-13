import pygame
from Classes.buttons import Button
from Utils.functions import Write
from States.basestate import Base
from pygame.color import THECOLORS

class Start(Base):
    """
    This is the first state of our game. This is the screen when player enters the game

    Inherits Base state
    """

    def __init__(self) -> None:
        super().__init__()

        self.startbtn = None
        self.background = pygame.image.load("Utils/Images/start_background.png")
        self.rect = self.background.get_rect()
    
    def render(self):
        self.screen.blit(self.background, self.rect)
        Write(text="Hot Air Balloon", screen=self.screen, x=self.wwidth//2, y=self.wheight//2, center=True, fontsize=64, color=THECOLORS['goldenrod'])
        self.startbtn = Button(x=self.wwidth//2, y=self.wheight//2+100, background=THECOLORS["darkred"], color=THECOLORS['goldenrod'], text="Start", screen=self.screen)
        self.startbtn.render()
        

    
    def update(self, params):

        self.render()

        if self.startbtn.clicked() : self.gstatemachine.change('countdown', screen=self.screen, width=self.wwidth, height=self.wheight, statemachine=self.gstatemachine)

        self.startbtn.update()
    
    def enter(self, **params):
        self.screen = params["screen"]
        self.wwidth = params['wwidth']
        self.wheight = params['wheight']
        self.gstatemachine = params['gstatemachine']

        self.__init__()
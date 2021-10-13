from Utils.functions import Write
import pygame
from pygame.color import THECOLORS
from States.basestate import Base
from Classes.buttons import Button

class GameOver(Base):
    """
    This state is shown when the game is over. That is the balloon is somehow exploded. 
    """

    def __init__(self) -> None:
        super().__init__()

    def render(self):
        
        Write(fontsize=72, text="Game Over!", color=THECOLORS['darkred'], screen=self.screen, x=self.wwidth//2, y=self.wheight//2, center=True)
        Write(fontsize=24, text=f"Score : {self.score}", color=THECOLORS['goldenrod'], screen=self.screen, x=self.wwidth//2, y=self.wheight//2 + 100, center=True)
        self.playagainbtn.render()

    def update(self, params):

        if self.playagainbtn.clicked() :
            self.gstatemachine.change('countdown', screen=self.screen, width=self.wwidth, height=self.wheight, statemachine=self.gstatemachine)
        self.playagainbtn.update()
        self.render()
    
    def enter(self, **params):
        self.screen = params['screen']
        self.wwidth = params['width']
        self.wheight = params['height']
        self.score = params['score']
        self.gstatemachine = params['gstatemachine']

        self.playagainbtn = Button(color=THECOLORS['goldenrod'], screen=self.screen, x=self.wwidth//2, y=self.wheight//2 + 200, background=THECOLORS['darkred'], text="Try Again")
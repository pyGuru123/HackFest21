import pygame

from States.basestate import Base
from classes.buttonClass import Button
from constants import *

class GameOver(Base):

    """
    This is a game over state that takes the argument from the base state to display Game Over message, total score, and presents the New Game option
    
    Parameters:
    Base: This is the base state
    """
    def __init__(self):
        super().__init__()

        self.biggerFont = pygame.font.SysFont("Comic sans MS", 100)
        self.smallerFont = pygame.font.SysFont("Comic sans MS", 36)
        self.startbtn = Button(text="Start Again", color2=BLUE)
        self.startbtn.x = WINDOW_WIDTH // 2 - self.startbtn.width // 2
        self.startbtn.y = WINDOW_HEIGHT // 2 + 200

        self.score = 0

    def render(self):
        message = self.biggerFont.render("Game Over!", True, RED, BGC)
        mRect = message.get_rect()
        mRect.center = (WINDOW_WIDTH //2 , WINDOW_HEIGHT // 2)
        SCREEN.blit(message, mRect)
        score = self.smallerFont.render(f"Score : {self.score}", True, GREEN, BGC)
        mRect = score.get_rect()
        mRect.center = (WINDOW_WIDTH //2 , WINDOW_HEIGHT // 2 + 100)
        SCREEN.blit(score, mRect)
        self.startbtn.render()

    def update(self, params):

        if self.startbtn.clicked() :
            gStateMachine.change("countdown")

        self.render()
    
    def enter(self, **params):
        
        self.score = params['SCORE']
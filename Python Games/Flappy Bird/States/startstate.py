import pygame

from States.basestate import Base

from classes.buttonClass import Button
from constants import *

class Start(Base):
    """
    This class state appears when 'python main.py' is invoked

    Parameters:
    Base: This is the base state
    """

    def __init__(self):

        super().__init__()

        self.startButton = Button(text="Start", color2=BLUE)
        self.startButton.x = WINDOW_WIDTH // 2 - self.startButton.width//2
        self.startButton.y = WINDOW_HEIGHT // 2 + 100

    
    def render(self) : 
        """
        Renders the screen
        """
        font = pygame.font.SysFont("Comic sans MS", 72)
        text = font.render("Flappy Bird", True, (255, 255, 255), BGC)
        textRect = text.get_rect()

        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        SCREEN.blit(text, textRect)
        self.startButton.render()

    def update(self, params):

        if self.startButton.clicked() : gStateMachine.change("countdown")

        self.render()
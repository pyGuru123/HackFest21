import pygame

from pygame.transform import scale

from States.basestate import Base

from constants import *

class Countdown(Base):    

    """
    This game state is called when User presses 'start' and lasts for 4(3) seconds and then moves to playstate

    Parameters:
    Base: This is the base state
    """
    def __init__(self):
        super().__init__()

        self.largeFont = pygame.font.SysFont("Comic sans MS", 100)
        self.MediumFont = pygame.font.SysFont("Comic sans MS", 36)
        self.count = 4
    
    def render(self):
        """
        Renders the countdown screen
        """
        count = self.largeFont.render(str(int(self.count)), True, WHITE, BGC)
        countRect = count.get_rect()
        countRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT // 2 - 100)

        txt = self.MediumFont.render("Press space to play", True, BLUE, BGC)
        textRect = txt.get_rect()
        textRect.center = (WINDOW_WIDTH //2 , WINDOW_HEIGHT // 2 + 100)
        SCREEN.blit(count, countRect)
        SCREEN.blit(txt, textRect)

        txt = self.MediumFont.render("Press p to toggle pause", True, BLUE, BGC)
        textRect = txt.get_rect()
        textRect.center = (WINDOW_WIDTH //2 , WINDOW_HEIGHT // 2 + 200)
        SCREEN.blit(txt, textRect)

        if self.count <= 1 : gStateMachine.change("play")

    def update(self, params):
        """
        Updates the number on countdown screen every 100 milliseconds
        """
        self.count -= 0.1
        pygame.time.wait(100)
        self.render()
    
    def enter(self, **params):
        self.count = 4
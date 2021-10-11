from random import randint

from pygame.constants import WINDOWHIDDEN
from classes.pillarClass import Pillar
from constants import BGC, SCORE, SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, gStateMachine
from classes.birdClass import Bird
import pygame

from States.basestate import Base

class Play(Base):

    """
    This class contains the functions necessary for the FlappyBird game mechanics
    """
    def __init__(self):
        """
        Initializing the mechanics of the game
        """
        super().__init__()

        self.pillar_sprite = pygame.sprite.Group()
        self.all_sprite = pygame.sprite.Group()
        self.bird = Bird()
        self.all_sprite.add(self.bird)
        self.speed = 0
        self.g = 0.5

        pillar1, pillar2 = Pillar(), Pillar()
        pillar1.rect.y = randint(-150, 0)
        pillar2.rect.y = WINDOW_HEIGHT // 2 + (pillar1.rect.bottom - randint(0, 100))
        self.all_sprite.add(pillar1)
        self.pillar_sprite.add(pillar1)
        self.all_sprite.add(pillar2)
        self.pillar_sprite.add(pillar2)

        self.last = pillar1
        self.current = pillar1
        self.count = False

        self.time_passed = 0

        self.paused = False


    def render(self) :
        self.all_sprite.draw(SCREEN)
        font = pygame.font.SysFont("Comic sans MS", 24)
        text = font.render(f"Score : {SCORE}", True, (255, 255, 255))
        textRect = text.get_rect()

        textRect.x= 10
        textRect.y = 10

        SCREEN.blit(text, textRect)

    def update(self, params) :
        """
        Checks for all possible events and handles user interactions such as Spacebar input, pause ('p' key input by default), and pillar collision
        """

        self.render()

        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.speed = -8
                    self.bird.flap = True
                    self.bird.make_flap()
                if event.key == pygame.K_p:
                    self.paused = not self.paused

        if self.paused :
            font = pygame.font.SysFont("Comic sans MS", 100)
            text = font.render("paused", True, (255, 255, 255), BGC)
            textRect = text.get_rect()

            textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

            SCREEN.blit(text, textRect)
            return

        global SCORE

        if (self.last.rect.x <= WINDOW_WIDTH - 300):
            pillar1, pillar2 = Pillar(), Pillar()
            pillar1.rect.y = randint(-150, 0)
            pillar2.rect.y = WINDOW_HEIGHT // 2 + (pillar1.rect.bottom - randint(100, 150))
            self.all_sprite.add(pillar1)
            self.pillar_sprite.add(pillar1)
            self.all_sprite.add(pillar2)
            self.pillar_sprite.add(pillar2)
            self.last = pillar1
        
        for pillar in self.pillar_sprite:
            if (self.bird.rect.x + self.bird.rect.width > pillar.rect.x and 
                self.bird.rect.x < pillar.rect.x + pillar.rect.width) : 
                self.count = True
                self.current = pillar
            if self.current.rect.x + self.current.rect.width < self.bird.rect.x and self.count:
                SCORE += 1
                self.count = False
            if pillar.rect.x < - pillar.rect.width: 
                pillar.kill()

        self.speed += self.g
        self.bird.rect.y += self.speed

        if (self.bird.rect.y + self.bird.rect.height >= WINDOW_HEIGHT or
            self.bird.rect.y <= 0) :
            pygame.time.wait(500)
            gStateMachine.change("gameover", SCORE=SCORE)

        for pillar in self.pillar_sprite:
            pillar.rect.x -= 3
            if pygame.sprite.collide_mask(self.bird, pillar) :
                pygame.time.wait(500)
                gStateMachine.change("gameover", SCORE=SCORE)

        self.time_passed += 1
        if (self.time_passed >= 30):
            self.bird.flap = False
            self.bird.make_flap()
            self.time_passed = 0

    
    def enter(self, **params):
        global SCORE
        self.all_sprite.empty()
        self.pillar_sprite.empty()
        self.bird = Bird()
        SCORE = 0

        self.__init__()
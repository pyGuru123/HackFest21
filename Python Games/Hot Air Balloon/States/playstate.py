from Classes.bonuspoints import Bonus
from Classes.hurdles import Hurdle
from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN, KEYUP, K_p
from pygame.color import THECOLORS
from Classes.balloon import Balloon
from Utils.functions import Write
import pygame
from States.basestate import Base
from random import *

class Play(Base):
    """
    This is play state, the actual playground of our game.
    """

    def __init__(self) -> None:

        # calls init funtion for base class
        super().__init__()

        # These are for speed of balloon
        self.speedY = 2
        self.speedX = 0

        # These are for hurdles
        self.hurdle_speed = 5
        self.countDeleted = 0
        self.score = 0

        # These are for bonus
        self.bonusScore = 5
        self.current_bonus = None
        self.bonus = 0

        # creating different sprite group
        self.bonusgroup = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.hurdles = pygame.sprite.Group()

        # Storing variable to keep track of making the bonus
        self.create_bonus = 180

        # loading background image for our game
        self.background1 = pygame.image.load("Utils/Images/background.png")
        self.background1 = pygame.transform.scale(self.background1, (500, 750))
        self.brect1 = self.background1.get_rect()
        self.background2 = self.background1
        self.brect2 = self.background2.get_rect()
        self.brect2.y = -self.brect2.height
        self.background_speed = 3

        # Number of hurdles are increased after this score
        self.hurdle_count = 1

        # Lives handline
        self.lives = 3
        self.lost_lives = 0
        self.lives_image = pygame.image.load("Utils/Images/lives.png")
        self.lost_lives_image = pygame.image.load("Utils/Images/lost_lives.png")

        # adding paused functionality
        self.paused = False


    def render(self) -> None :

        #displaying the background image
        self.screen.blit(self.background1, self.brect1)
        self.screen.blit(self.background2, self.brect2)

        # Display score on the screen
        Write(text=f"Score : {self.score}", fontsize=25, screen=self.screen, color=THECOLORS['goldenrod'])

        # displaying the the lives
        for i in range(self.lives):
            lives = self.lives_image
            if self.lives - self.lost_lives < i+1: lives = self.lost_lives_image
            rect = lives.get_rect()
            rect.center = (self.wwidth - 15*(i+1) - 25*i, 15)
            self.screen.blit(lives, rect)

        # Display all the sprite on the screen
        self.all_sprites.draw(self.screen)


    def update(self, params) -> None:

        # calling render function again
        self.render()

        # This is event handling section events are passed from main.py
        for event in params:

            # If any button is pressed
            if event.type == KEYDOWN:

                # pause function
                if event.key == K_p:
                    self.paused = not self.paused

                # Controlling the balloon if right or left arrow key is pressed
                if event.key == K_LEFT:
                    self.balloon.change("left")
                    self.speedX = -5
                if event.key == K_RIGHT:
                    self.balloon.change("right")
                    self.speedX = 5
            
            # If the pressed key is released
            if event.type == KEYUP:
                self.balloon.change()
                self.speedX = 0
        
        # if the game is paused
        if self.paused : 
            Write(text="Paused", fontsize=72, color=THECOLORS["darkred"], screen=self.screen, x=self.wwidth//2, y=self.wheight//2, center=True)
            Write(text="Press p to continue", color=THECOLORS["goldenrod"], screen=self.screen, x=self.wwidth//2, y=self.wheight//2 + 100, center=True)
            return

        #moving background
        self.brect1.y = self.brect1.y + self.background_speed if self.brect1.y < self.wheight else - self.brect1.height + self.background_speed
        self.brect2.y = self.brect2.y + self.background_speed if self.brect2.y < self.wheight else - self.brect2.height + self.background_speed

        # decreasing create bonus on each update
        self.create_bonus -= 1

        # creates bonus when create bonus is 0
        if self.create_bonus == 0:
            self.add_bonus()
            self.create_bonus = 180

        # for bonus
        for bonus in self.bonusgroup:

            # for moving the bonus same speed as hurdles
            bonus.rect.y += self.hurdle_speed

            #checks if the balloon collided with any bonus and increases score accordingly
            if pygame.sprite.collide_mask(self.balloon, bonus):
                self.bonus += self.bonusScore
                bonus.kill()

        # if the current hurdle is more than 200 away from the 0 vertically a new hurdle is created
        if self.current_hurdle.rect.y > 200 :
            for i in range(self.hurdle_count):
                self.add_hurlde()

        # variable to store the number of hurdles passed
        passedCount = 0

        # Hurdles
        for hurdle in self.hurdles:

            # checking if any hurdle collided with the balloon
            if pygame.sprite.collide_mask(self.balloon, hurdle):
                self.lost_lives += 1
                if (self.lost_lives == self.lives) :
                    self.speedY = 0
                    self.hurdle_speed = 0
                    self.gstatemachine.change("over", screen=self.screen, width=self.wwidth, height=self.wheight, score=self.score, gstatemachine=self.gstatemachine)
                self.respawn()
                # Write(text=f"{self.lives - self.lost_lives} lives remaining", color=THECOLORS["goldenrod"], screen=self.screen, x=self.wwidth//2, y=self.wheight//2, center=True)
                pygame.time.wait(1000)

            # moving the hurdle
            hurdle.rect.y += self.hurdle_speed

            # incresing the passedcount and hurdle speed if the hurdle has passed the balloon
            if hurdle.rect.y > self.balloon.rect.y + self.balloon.rect.height:
                passedCount += 1
                self.hurdle_speed += 0.001

            # Killin the hurdle if it has gone below the bottom
            if hurdle.rect.y >= self.wheight :
                self.countDeleted += 1
                hurdle.kill()

        # Updating our score  
        self.score = self.countDeleted + passedCount + self.bonus
        
        # creating an extra hurdle when score reaches 100
        if self.score >= 100 : self.hurdle_count = 2

        # preventing the balloon from getting too far left or too right of the screen
        if self.balloon.rect.y > self.wwidth // 2 + 100: self.balloon.rect.y -= self.speedY
        if self.balloon.rect.left >= 0 and self.balloon.rect.right <= self.wwidth : self.balloon.rect.x += self.speedX
        if self.balloon.rect.left <= 0 : self.balloon.rect.left = 2
        if self.balloon.rect.right >= self.wwidth : self.balloon.rect.right = self.wwidth - 2

        # updating the balloon class
        self.balloon.update()

    def enter(self, **params):

        # calling init function
        self.__init__()

        # taking variables passed during changing the state
        self.screen = params['screen']
        self.wwidth = params['width']
        self.wheight = params['height']
        self.gstatemachine = params['statemachine']

        # creating the balloon
        self.balloon = Balloon()
        self.balloon.rect.center = (self.wwidth // 2, self.wheight - 50)
        self.all_sprites.add(self.balloon)

        # creating first hurdle
        self.add_hurlde()

    def add_hurlde(self) -> None:
        """
        This function will add the hurdles on screen. It reduces some code and makes game code more readable.

        usage:
            self.add_hurlde()
        """
        self.current_hurdle = Hurdle()
        self.current_hurdle.rect.center = (randrange(self.current_hurdle.rect.width, self.wwidth - self.current_hurdle.rect.width), 0)
        self.all_sprites.add(self.current_hurdle)
        self.hurdles.add(self.current_hurdle)
    
    def add_bonus(self) -> None:
        """
        This function will add the Bonuses on screen. It reduces some code and makes game code more readable.

        usage:
            self.add_bonus()
        """

        self.current_bonus = Bonus()
        self.current_bonus.rect.center = (randrange(self.current_bonus.rect.width, self.wwidth - self.current_bonus.rect.width), -50)
        self.all_sprites.add(self.current_bonus)
        self.bonusgroup.add(self.current_bonus)
        self.create_bonus = False

    def respawn(self) -> None:
        """
        This function respawns the balloon after getting hit by any hurdle.
        """
        self.balloon.rect.x = randrange(0, self.wwidth - self.balloon.rect.width - 10)
        for hurdle in self.hurdles:
            while pygame.sprite.collide_mask(self.balloon, hurdle):
                self.balloon.rect.x = randrange(0, self.wwidth - self.balloon.rect.width - 10)
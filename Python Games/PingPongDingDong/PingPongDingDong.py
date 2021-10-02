import pygame
from pygame import gfxdraw
from random import choice

pygame.init()
pygame.display.set_caption('Ping Pong Ding Dong')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_SIZE = (1251, 600)

PADDLE_WIDTH = 11
PADDLE_HEIGHT = 100
PADDLE_MARGIN = 30
PADDLE_SPEED = 2

BALL_RADIUS = 12

PADDING = 10

MARGIN = 75
TOP_MARGIN = MARGIN + PADDING
BOTTOM_MARGIN = WINDOW_SIZE[1] - PADDING - PADDLE_HEIGHT

BALL_VELOCITY_VERTICAL = 1
BALL_VELOCITY_HORIZONTAL = 2


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


class Paddle:
    def __init__(self, left, top, width, height, paddle_keyup, paddle_keydown):
        self.left = left
        self.top = top

        self.width = width
        self.height = height

        self.rounded_edge_radius = self.width // 2

        self.paddle_keyup = paddle_keyup
        self.paddle_keydown = paddle_keydown

        self.should_move_up = False
        self.should_move_down = False

        self.display()

    def move_up(self):
        self.top = max(TOP_MARGIN, self.top - 2)

    def move_down(self):
        self.top = min(BOTTOM_MARGIN, self.top + 2)

    def update(self):
        key_states = pygame.key.get_pressed()

        if key_states[self.paddle_keyup]:
            self.move_up()

        if key_states[self.paddle_keydown]:
            self.move_down()

    def display(self):
        draw_circle(display, self.left + self.rounded_edge_radius,
                    self.top + self.rounded_edge_radius, self.rounded_edge_radius, WHITE)

        draw_circle(display, self.left + self.rounded_edge_radius,
                    self.top + self.height - self.rounded_edge_radius, self.rounded_edge_radius, WHITE)

        pygame.draw.rect(display, WHITE, (self.left, self.top + self.rounded_edge_radius,
                                          self.width, self.height - 2 * self.rounded_edge_radius))


def update_score(lost_player):
    global score1
    global score2

    if lost_player == 1:
        score2 += 1
    else:
        score1 += 1


class Ball:
    def __init__(self, left, top, radius, velocity_horizontal, velocity_vertical):
        self.left_original = left
        self.top_original = top

        self.left = left
        self.top = top

        self.radius = radius

        self.velocity_horizontal_original = velocity_horizontal
        self.velocity_vertical_original = velocity_vertical

        self.velocity_horizontal = velocity_horizontal
        self.velocity_vertical = velocity_vertical

    def initialize(self):
        self.left = self.left_original
        self.top = self.top_original
        self.velocity_horizontal = choice((1, -1)) * self.velocity_horizontal_original
        self.velocity_vertical = choice((1, -1)) * self.velocity_vertical_original

    def update(self):
        self.left += self.velocity_horizontal
        self.top += self.velocity_vertical

        if self.is_colliding():
            self.velocity_horizontal *= -1
            self.left += self.velocity_horizontal
            self.top += self.velocity_vertical

        if not (self.radius <= self.left <= WINDOW_SIZE[0] - self.radius):
            update_score(1 if self.velocity_horizontal < 0 else 2)
            self.initialize()
            return

        if not (MARGIN <= self.top - self.radius and self.top + self.radius <= WINDOW_SIZE[1]):
            self.velocity_vertical *= -1

        self.display()

    def display(self):
        draw_circle(display, self.left, self.top, self.radius, WHITE)

    def is_colliding(self):
        if self.velocity_horizontal < 0:
            paddle = left_paddle
        else:
            paddle = right_paddle

        center_x = paddle.left + paddle.width // 2
        center_y = paddle.top + paddle.height // 2

        dist_x = abs(self.left - center_x)
        dist_y = abs(self.top - center_y)

        if dist_x > paddle.width // 2 + self.radius: return False
        if dist_y > paddle.height // 2 + self.radius: return False

        if dist_x <= paddle.width // 2: return True
        if dist_y <= paddle.height // 2: return True

        return (dist_x - paddle.width // 2) ** 2 + (dist_y - paddle.height // 2) ** 2 <= (self.radius ** 2)


def draw_vertical_dashed_line(surf, color, x, length, width=1, dash_length=10):
    for index in range(0, length // dash_length, 2):
        pygame.draw.line(surf, color, (x, index * dash_length), (x, (index + 1) * dash_length), width)


clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('Arial', MARGIN // 2)

finished = False
display = pygame.display.set_mode(WINDOW_SIZE)

score1 = score2 = 0

left_paddle = Paddle(PADDLE_MARGIN,
                     TOP_MARGIN + (WINDOW_SIZE[1] - TOP_MARGIN - PADDLE_HEIGHT) // 2,
                     PADDLE_WIDTH, PADDLE_HEIGHT, pygame.K_w, pygame.K_s)

right_paddle = Paddle(WINDOW_SIZE[0] - PADDLE_MARGIN,
                      TOP_MARGIN + (WINDOW_SIZE[1] - TOP_MARGIN - PADDLE_HEIGHT) // 2,
                      PADDLE_WIDTH, PADDLE_HEIGHT, pygame.K_UP, pygame.K_DOWN)

ball = Ball(WINDOW_SIZE[0] // 2,
            MARGIN + (WINDOW_SIZE[1] - MARGIN) // 2,
            BALL_RADIUS,
            BALL_VELOCITY_HORIZONTAL,
            BALL_VELOCITY_VERTICAL)

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    display.fill(BLACK)


    ball.update()

    left_paddle.update()
    right_paddle.update()

    clock.tick(180)

    left_paddle.display()
    right_paddle.display()

    score_text1 = font.render('Score: ' + str(score1), True, WHITE)
    score_text2 = font.render('Score: ' + str(score2), True, WHITE)

    score_text_width1 = score_text1.get_rect().width
    score_text_width2 = score_text2.get_rect().width

    display.blit(score_text1, ((WINDOW_SIZE[0] // 2 - score_text_width1) // 2, 10))
    display.blit(score_text2, ((3 * WINDOW_SIZE[0] // 2 - score_text_width2) // 2, 10))

    pygame.draw.line(display, WHITE, (0, MARGIN), (WINDOW_SIZE[0], MARGIN))
    draw_vertical_dashed_line(display, WHITE, WINDOW_SIZE[0] // 2, WINDOW_SIZE[1])

    pygame.display.update()

import pygame
import os
pygame.font.init()
pygame.mixer.init()

width , height = 900 , 500 
WIN = pygame.display.set_mode(( width , height))
pygame.display.set_caption(" Space Game!!")

white = (255 , 255, 255)
black = ( 0,0,0)
RED = ( 255 , 0 , 0)
YELLOW = ( 255,255,0)
fps = 60
space_w , space_h = 55 ,40
velocity = 5
bullet_velocity = 7
max_bullets = 10

bullet_firesound = pygame.mixer.Sound('python\PygameForBeginners-main\Assets\Gun+Silencer.mp3')
bullet_hitsound = pygame.mixer.Sound('python\PygameForBeginners-main\Assets\Grenade+1.mp3')

health_font = pygame.font.SysFont( 'ARIAL BLACK' , 20)
winner_font = pygame.font.SysFont( 'ARIAL BLACK' , 40)
YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2

border = pygame.Rect(width//2 - 5,0,10,height)

space = pygame.transform.scale(pygame.image.load('python\PygameForBeginners-main\Assets\space.png') ,( width,height) )

yellow_spaceship = pygame.image.load('python\PygameForBeginners-main\Assets\spaceship_yellow.png')
yellow_spaceship = pygame .transform .rotate(pygame.transform.scale(yellow_spaceship , (space_w,space_h)), 90 )

red_spaceship = pygame.image.load('python\PygameForBeginners-main\Assets\spaceship_red.png')
red_spaceship = pygame .transform.rotate(pygame.transform.scale(red_spaceship , (space_w,space_h)) , 270)


def draw_window( red , yellow ,RED_bullets,  YELLOW_BULLETS , red_health , yellow_health):
    WIN.blit( space , ( 0,0))
    pygame.draw.rect(WIN ,black , border)

    red_health_text = health_font.render("HEALTH :" + " " + str( red_health) , 1,white)
    yellow_health_text = health_font.render("HEALTH :" + " " + str( yellow_health) , 1,white)
    WIN.blit( red_health_text, (width - red_health_text.get_width() -10 ,10))
    WIN.blit( yellow_health_text, (10 ,10))


    WIN.blit(yellow_spaceship,( yellow.x , yellow.y))
    WIN.blit(red_spaceship,( red.x , red.y))

    
    for bullet in RED_bullets:
        pygame.draw.rect( WIN , RED, bullet)
    for bullet in YELLOW_BULLETS:
        pygame.draw.rect( WIN , YELLOW, bullet)    


    pygame.display.update()


def winner(text):
    draw_text = winner_font.render(text ,1,white)
    WIN.blit(draw_text, (width/2 - draw_text.get_width() / 2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000) 


def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - velocity > 0:
            yellow.x -= velocity
    if keys_pressed[pygame.K_d] and yellow.x + velocity + yellow.width < border.x :
            yellow.x += velocity
    if keys_pressed[pygame.K_w] and yellow.y - velocity  > 20:
            yellow.y -= velocity
    if keys_pressed[pygame.K_s]and yellow.y + velocity + yellow.height < height - 20:
            yellow.y += velocity  


def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - velocity > border.x + border.width:
            red.x -= velocity
    if keys_pressed[pygame.K_RIGHT] and red.x + velocity + red.width < width:
            red.x += velocity
    if keys_pressed[pygame.K_UP] and red.y - velocity > 20:
            red.y -= velocity
    if keys_pressed[pygame.K_DOWN] and red.y + velocity + red.height < height - 20 :
            red.y += velocity              

def handle_bullets( YELLOW_BULLETS ,RED_bullets ,yellow ,red):
    for bullet in YELLOW_BULLETS:
        bullet.x += bullet_velocity
        if red.colliderect(bullet):
            pygame.event.post( pygame.event.Event(RED_HIT))
            YELLOW_BULLETS.remove(bullet)
        elif bullet.x > width:
            YELLOW_BULLETS.remove(bullet)
            
    for bullet in RED_bullets:
        bullet.x -= bullet_velocity
        if yellow.colliderect(bullet):
            pygame.event.post( pygame.event.Event(YELLOW_HIT))
            RED_bullets.remove(bullet)
        elif bullet.x < 0:
            RED_bullets.remove(bullet)

def main():
    red = pygame.Rect(700,300,space_w,space_h)
    yellow = pygame.Rect(100,300,space_w,space_h)

    RED_bullets =[]
    YELLOW_BULLETS = []

    red_health = 20
    yellow_health = 20

    Clock = pygame.time.Clock()
    
    run = True
    while run:
        Clock.tick(fps)
        

        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(YELLOW_BULLETS) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width , yellow.y + yellow.height//2 - 2 , 10 ,5)
                    YELLOW_BULLETS.append(bullet)
                    bullet_firesound.play()


                if event.key == pygame.K_RCTRL and len(RED_bullets) < max_bullets :  
                    bullet = pygame.Rect(red.x , red.y + red.height//2 - 2 , 10 ,5) 
                    RED_bullets.append(bullet)
                    bullet_firesound.play()
            
            if event.type == RED_HIT:
                red_health -= 1
                bullet_hitsound.play()

            if event.type == YELLOW_HIT: 
                yellow_health -= 1  
                bullet_hitsound.play()

        winner_text =" "    
        if red_health <=0:
            winner_text = " YELLOW WINS      KNOCK OUT !!"

        if yellow_health <=0 :  
            winner_text = " RED WINS          KNOCK OUT !!"
        if winner_text != " "  :
            winner( winner_text)   
            break
         
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed,yellow)
        red_movement(keys_pressed,red)

        handle_bullets( YELLOW_BULLETS,RED_bullets,yellow,red)

        draw_window( red , yellow , RED_bullets ,YELLOW_BULLETS , red_health , yellow_health)



    main()

if __name__ == "__main__" :
    main()

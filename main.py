import random
import time
import pygame
import os

pygame.font.init()

SIZE = 650

FONT_BIG = pygame.font.SysFont('comisans', SIZE//20)

FONT_SMALL = pygame.font.SysFont('comicsans', SIZE//40)
WIN = pygame.display.set_mode((SIZE,SIZE))

FPS = 60

SPACESHIP_LIFE = 3

SPACE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(SIZE,SIZE))

SPACESHIP_WIDTH = SIZE//15
SPACESHIP_HEIGHT = SIZE//15
SPACESHIP_INITIAL_POSITION_X = (SIZE//2) - (SPACESHIP_WIDTH//2)
SPACESHIP_INITIAL_POSITION_Y = (SIZE//1.1) - (SPACESHIP_HEIGHT//2)
SPACESHIP_SPEED = SIZE//125
SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship.png'))
SPACESHIP_SCALED = pygame.transform.scale(SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
SPACESHIP = pygame.transform.rotate(SPACESHIP_SCALED,180)

BULLET_WIDTH = SIZE//120
BULLET_HEIGHT = SIZE//60
BULLET_SPEED = SIZE//55

ALIEN_WIDTH = SIZE//25
ALIEN_HEIGHT = SIZE//25
ALIEN_SPEED = SIZE//240
ALIEN_IMAGE = pygame.image.load(os.path.join('Assets','alien.png'))
ALIEN = pygame.transform.scale(ALIEN_IMAGE,(ALIEN_WIDTH,ALIEN_HEIGHT))

#RGB (red green blue)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

def draw_window(spaceship, bullets, aliens, life, total_time):
    WIN.blit(SPACE_IMAGE,(0,0))
    WIN.blit(SPACESHIP,(spaceship.x,spaceship.y))

    for l in range(life):
        WIN.blit(SPACESHIP, (l*SPACESHIP_WIDTH,SPACESHIP_HEIGHT//1.5))

    for alien in aliens:
        WIN.blit(ALIEN, (alien.x,alien.y))
    for bullet in bullets:
        pygame.draw.rect(WIN, RED, bullet)
    if total_time != None:
        final_text = FONT_BIG.render('You lost in '+ str(total_time)+' s!',1,WHITE)
        WIN.blit(final_text, (SIZE//2 - final_text.get_width()//2, SIZE//2.5))
        restart = FONT_SMALL.render('Press Enter to restart or Esc to quit',1,WHITE)
        WIN.blit(restart, (SIZE//2 - restart.get_width()//2, SIZE//35 + final_text.get_height()+SIZE//2.5))
        
    pygame.display.update()

def stop_clockwatch(initial_time):
    return round(time.time() - initial_time,1)

def move_spaceship(spaceship):
    key_pressed = pygame.key.get_pressed()        
    if key_pressed[pygame.K_DOWN] and spaceship.y < SIZE - SPACESHIP_HEIGHT:
        spaceship.y = spaceship.y+SPACESHIP_SPEED        
    if key_pressed[pygame.K_UP] and spaceship.y > 0:
        spaceship.y = spaceship.y-SPACESHIP_SPEED    
    if key_pressed[pygame.K_LEFT] and spaceship.x > 0:      
        spaceship.x = spaceship.x-SPACESHIP_SPEED
    if key_pressed[pygame.K_RIGHT] and spaceship.x < SIZE - SPACESHIP_WIDTH:
        spaceship.x = spaceship.x+SPACESHIP_SPEED
    
def new_alien():
    return pygame.Rect(SIZE-random.randint(ALIEN_WIDTH,SIZE), 0,ALIEN_WIDTH,ALIEN_HEIGHT)

def main():
    clock = pygame.time.Clock()    
    run = True
    initial_time = time.time()
    total_time = None
    spaceship = pygame.Rect(SPACESHIP_INITIAL_POSITION_X, SPACESHIP_INITIAL_POSITION_Y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    bullets = []
    aliens = []
    life = SPACESHIP_LIFE
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #traz todos os eventos que ocorreram antes dessa linha
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets) < 3:
                    bullets.append (pygame.Rect(spaceship.x + (SPACESHIP_WIDTH // 2) - (BULLET_WIDTH // 2) , spaceship.y - BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT))              
                if event.key == pygame.K_RETURN and life<=0:                    
                    initial_time = time.time()
                    total_time = None
                    spaceship = pygame.Rect(SPACESHIP_INITIAL_POSITION_X, SPACESHIP_INITIAL_POSITION_Y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
                    bullets = []
                    aliens = []
                    life = SPACESHIP_LIFE
                if event.key == pygame.K_ESCAPE:
                    run = False

        move_spaceship(spaceship)
        for bullet in bullets:
            if bullet.y < 0:
                bullets.remove(bullet)
            bullet.y = bullet.y - BULLET_SPEED

        for alien in aliens:                                       
            alien.y = alien.y + ALIEN_SPEED
            if alien.y > SIZE:                               
                aliens.remove(alien)
                life = life-1

        if random.randint(1,100) == 1:
            aliens.append (new_alien())

        for alien in aliens:
            for bullet in bullets:
                if bullet.colliderect(alien):
                    aliens.remove(alien)
                    bullets.remove(bullet)
            if spaceship.colliderect(alien):
                aliens.remove(alien)
                life = life-1

        if life <= 0 and total_time == None:
            total_time = stop_clockwatch(initial_time)    
              
        draw_window(spaceship, bullets, aliens, life, total_time)
        
    pygame.quit()

if __name__ == "__main__": #evita que o programa rode quando for importado em outro lugar
    main()
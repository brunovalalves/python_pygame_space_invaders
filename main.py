import pygame
import os

SIZE = 650

WIN = pygame.display.set_mode((SIZE,SIZE))

FPS = 60

SPACE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(SIZE,SIZE))

SPACESHIP_WIDTH = SIZE//15
SPACESHIP_HEIGHT = SIZE//15
SPACESHIP_INITIAL_POSITION_X = (SIZE//2) - (SPACESHIP_WIDTH//2)
SPACESHIP_INITIAL_POSITION_Y = (SIZE//2) - (SPACESHIP_HEIGHT//2)
SPACESHIP_SPEED = SIZE//125
SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship.png'))
SPACESHIP_SCALED = pygame.transform.scale(SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
SPACESHIP = pygame.transform.rotate(SPACESHIP_SCALED,180)

BULLET_WIDTH = SIZE//120
BULLET_HEIGHT = SIZE//60
BULLET_SPEED = SIZE//55

ALIEN_WIDTH = SIZE//30
ALIEN_HEIGHT = SIZE//30
ALIEN_SPEED = SIZE//240

#RGB (red green blue)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

def draw_window(spaceship, bullets, aliens):
    WIN.blit(SPACE_IMAGE,(0,0))
    WIN.blit(SPACESHIP,(spaceship.x,spaceship.y))
    for alien in aliens:
        pygame.draw.rect(WIN, BLACK, alien)
    for bullet in bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update()

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
    
def main():
    clock = pygame.time.Clock()    
    run = True
    spaceship = pygame.Rect(SPACESHIP_INITIAL_POSITION_X, SPACESHIP_INITIAL_POSITION_Y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    bullets = []
    aliens = [pygame.Rect(SIZE//3, 0,ALIEN_WIDTH,ALIEN_HEIGHT)]
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #traz todos os eventos que ocorreram antes dessa linha
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets) < 3:
                    bullets.append (pygame.Rect(spaceship.x + (SPACESHIP_WIDTH // 2) - (BULLET_WIDTH // 2) , spaceship.y - BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT))              
        move_spaceship(spaceship)
        for bullet in bullets:
            if bullet.y < 0:
                bullets.remove(bullet)
            bullet.y = bullet.y - BULLET_SPEED
        
        for alien in aliens:
            if alien.y > SIZE:
                aliens.remove(alien) 
            alien.y = alien.y + ALIEN_SPEED
        draw_window(spaceship, bullets, aliens)
        
    pygame.quit()

if __name__ == "__main__": #evita que o programa rode quando for importado em outro lugar
    main()
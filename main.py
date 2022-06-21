import pygame

SIZE = 650

WIN = pygame.display.set_mode((SIZE,SIZE))

FPS = 60

SPACESHIP_WIDTH = SIZE//20
SPACESHIP_HEIGHT = SIZE//20
SPACESHIP_INITIAL_POSITION_X = (SIZE//2) - (SPACESHIP_WIDTH//2)
SPACESHIP_INITIAL_POSITION_Y = (SIZE//2) - (SPACESHIP_HEIGHT//2)
SPACESHIP_SPEED = SIZE//125
BULLET_WIDTH = SIZE//240
BULLET_HEIGHT = SIZE//240

#RGB (red green blue)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

def draw_window(spaceship, bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,spaceship)
    for bullet in bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()    
    run = True
    spaceship = pygame.Rect(SPACESHIP_INITIAL_POSITION_X, SPACESHIP_INITIAL_POSITION_Y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    bullets = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #traz todos os eventos que ocorreram antes dessa linha
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append (pygame.Rect(spaceship.x + (SPACESHIP_WIDTH // 2) - (BULLET_WIDTH // 2) , spaceship.y - BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT))
        key_pressed = pygame.key.get_pressed()        
        if key_pressed[pygame.K_DOWN] and spaceship.y < SIZE - SPACESHIP_HEIGHT:
            spaceship.y = spaceship.y+SPACESHIP_SPEED        
        if key_pressed[pygame.K_UP] and spaceship.y > 0:
            spaceship.y = spaceship.y-SPACESHIP_SPEED    
        if key_pressed[pygame.K_LEFT] and spaceship.x > 0:      
            spaceship.x = spaceship.x-SPACESHIP_SPEED
        if key_pressed[pygame.K_RIGHT] and spaceship.x < SIZE - SPACESHIP_WIDTH:
            spaceship.x = spaceship.x+SPACESHIP_SPEED
        draw_window(spaceship, bullets)
    pygame.quit()

if __name__ == "__main__": #evita que o programa rode quando for importado em outro lugar
    main()
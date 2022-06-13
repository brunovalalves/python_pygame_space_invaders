import pygame

SIZE = 650

WIN = pygame.display.set_mode((SIZE,SIZE))

FPS = 60

SPACESHIP_WIDTH = SIZE//20
SPACESHIP_HEIGHT = SIZE//20
SPACESHIP_INITIAL_POSITION_X = (SIZE//2) - (SPACESHIP_WIDTH//2)
SPACESHIP_INITIAL_POSITION_Y = (SIZE//2) - (SPACESHIP_HEIGHT//2)
SPACESHIP_SPEED = SIZE//125

WHITE = (255,255,255)
BLACK = (0,0,0)

def draw_window(spaceship):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,spaceship)
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()    
    run = True
    spaceship = pygame.Rect(SPACESHIP_INITIAL_POSITION_X, SPACESHIP_INITIAL_POSITION_Y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #traz todos os eventos que ocorreram antes dessa linha
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()        
        if key_pressed[pygame.K_DOWN]:
            spaceship.y = spaceship.y+SPACESHIP_SPEED        
        if key_pressed[pygame.K_UP]:
            spaceship.y = spaceship.y-SPACESHIP_SPEED    
        if key_pressed[pygame.K_LEFT]:      
            spaceship.x = spaceship.x-SPACESHIP_SPEED
        if key_pressed[pygame.K_RIGHT]:   
            spaceship.x = spaceship.x+SPACESHIP_SPEED
        draw_window(spaceship)
    pygame.quit()

if __name__ == "__main__": #evita que o programa rode quando for importado em outro lugar
    main()
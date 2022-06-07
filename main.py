import pygame

WIN = pygame.display.set_mode((300,300))

def draw_window(spaceship):
    WIN.fill((255,255,255))
    pygame.draw.rect(WIN,(0,0,0),spaceship)
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()    
    run = True
    spaceship = pygame.Rect(150, 225,25,25)
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        spaceship.y = spaceship.y-1
        spaceship.x = spaceship.x-1
        draw_window(spaceship)
    pygame.quit()

if __name__ == "__main__":
    main()
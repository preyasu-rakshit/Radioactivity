import pygame, sys

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Radioactivity")
clock = pygame.time.Clock()

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill([0, 0, 0])
    pygame.display.flip()
    clock.tick(60)
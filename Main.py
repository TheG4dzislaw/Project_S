import pygame

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 400
FPS = 60

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()

running = True

pos_x = 190

while running:
    clock.tick(FPS)
    pos_x += 1

    screen.fill("black")

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Drawing
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(pos_x, 190, 50, 50))
    
    pygame.display.update()

pygame.QUIT()
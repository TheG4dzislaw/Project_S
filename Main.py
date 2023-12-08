import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

running = True

pos_x = 190

while running:
    clock.tick(30)
    pos_x += 1

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Drawing
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(pos_x, 190, 50, 50))
    
    pygame.display.update()

pygame.QUIT()
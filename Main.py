import pygame
from draw import draw
from player import Player

#initiation of pygame
pygame.init()
pygame.display.set_caption("Project_S")

#display variables
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
FPS = 60

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

def main(screen):
    clock = pygame.time.Clock()
    running = True
    player = Player(100, 100, 50, 50)

    while running:
        clock.tick(FPS)

        #Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        draw(screen, player)

    pygame.quit()
    quit()        


if __name__ == "__main__":
    main(screen)
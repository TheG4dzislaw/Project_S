import pygame
from draw import draw
from player import Player

#TEST

#initiation of pygame
pygame.init()
pygame.display.set_caption("Project_S")

#display variables
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
FPS = 60

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

def control_handler(player):
    keys = pygame.key.get_pressed()

    #This variables reset player x & y velocity to 0 when nothing is pressed
    player.x_velocity = 0
    player.y_velocity = 0

    if keys[pygame.K_a]:
        player.move_left(player.PLAYER_VELOCITY)
    if keys[pygame.K_d]:
        player.move_right(player.PLAYER_VELOCITY)
    if keys[pygame.K_w]:
        player.move_up(player.PLAYER_VELOCITY)
    if keys[pygame.K_s]:
        player.move_down(player.PLAYER_VELOCITY)

def main(screen):
    clock = pygame.time.Clock()
    running = True
    player = Player(100, 400, 50, 50)

    while running:
        clock.tick(FPS)

        #Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        player.loop(FPS)
        control_handler(player)

        #Call drawing function
        draw(screen, player)

    pygame.quit()
    quit()        


if __name__ == "__main__":
    main(screen)
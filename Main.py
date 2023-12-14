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

#function responsible for control handling
def control_handler(player):
    keys = pygame.key.get_pressed()

    #This variables reset player x & y velocity to 0 when nothing is pressed
    player.x_velocity = 0
    player.y_velocity = 0

    if keys[pygame.K_a]:
        if(player.rect.x <= 0):
            player.move_left(0)
        else:
            player.move_left(player.PLAYER_VELOCITY)
    if keys[pygame.K_d]:
        if(player.rect.x >= (WINDOW_HEIGHT - player.rect.width)):
            player.move_right(0)
        else:
            player.move_right(player.PLAYER_VELOCITY)
    if keys[pygame.K_w]:
        if(player.rect.y < 240): #should be changed in near future as parametr - background height - player.rect.height + 5 (this five is a margin)
            player.move_up(0)
        else:
            player.move_up(player.PLAYER_VELOCITY)
    if keys[pygame.K_s]:
        if(player.rect.y > (WINDOW_WIDTH - player.rect.height - 50)): #also should be changed when background will be added
            player.move_down(0)
        else:
            player.move_down(player.PLAYER_VELOCITY)

def main(screen):
    clock = pygame.time.Clock()
    running = True
    player = Player(100, 400, 50, 100)

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
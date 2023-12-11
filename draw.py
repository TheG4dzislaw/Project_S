import pygame

BACKGROUND_COLOR = (54, 197, 244)

def draw(screen, player):

    screen.fill(BACKGROUND_COLOR)
    player.draw(screen)

    pygame.display.update()

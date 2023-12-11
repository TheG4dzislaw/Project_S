import pygame

class Player(pygame.sprite.Sprite):
    #variables describe player stats
    PLAYER_VELOCITY = 2
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0

    def move(self, direction_x, direction_y):
        self.rect.x += direction_x
        self.rect.y += direction_y

    def move_left(self, velocity):
        if(self.y_velocity == velocity or self.y_velocity == -velocity):
            self.x_velocity = -velocity * 0.7077
        else:
            self.x_velocity = -velocity

    def move_right(self, velocity):
        if(self.y_velocity == velocity or self.y_velocity == -velocity):
            self.x_velocity = velocity * 0.7077
        else:
            self.x_velocity = velocity

    def move_up(self, velocity):
        if(self.x_velocity == velocity or self.x_velocity == -velocity):
            self.y_velocity = -velocity * 0.7077
        else:
            self.y_velocity = -velocity

    def move_down(self, velocity):
        if(self.x_velocity == velocity or self.x_velocity == -velocity):
            self.y_velocity = velocity * 0.7077
        else:
            self.y_velocity = velocity

    def loop(self, FPS):
        self.move(self.x_velocity, self.y_velocity)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)
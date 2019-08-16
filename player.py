import pygame
from sys import exit

black = (0, 0, 0)

pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)

class player(positionable):

    def __init__(self, x, y):
        self.x = x
        self.x_velocity = 0.0
        self.y = y
        self.y_velocity = 0.0
        self.position = (self.x, self.y)
        self.img = pygame.image.load('player.png')

    def move(self):
        self.x, self.y = get_position()
        self.x = self.x * x_velocity * time
        self.y = self.y *y_velocity * time

    def get_position(self):
        self.position = (self.x, self.y)
        return self.position

    def draw(self):
        self.position = self.get_position()
        screen.blit(self.img, self.position)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit();
        elif event.type == KEYDOWN:
            if event.scancode == 13:
                y_velocity += 20 * time
            elif event.scancode == 0:
                x_velocity -= 20 * time
            elif event.scancode == 2:
                x_velocity += 20 * time

    screen.fill(black)
    player.draw()
    pygame.display.flip()

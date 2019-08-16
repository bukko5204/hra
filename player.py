import pygame
from sys import exit

black = (0, 0, 0)

pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)

class player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('player.png')

#    def move(self):
    def get_position(self):
        self.position = (self.x, self.y)
        return self.position

    def draw(self):
        self.position = self.get_position()
        screen.blit(self.img)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit();
    screen.fill(black)
    player.draw()
    pygame.display.flip()

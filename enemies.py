import pygame
from sys import exit

pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)

class enemy(positionable):

    def __init__(self, x, y, x_velocity, y_velocity, img):
        self.x = x
        self.y = y
        self.y_velocity = y_velocity
        self.x_velocity = x_velocity
        self.img = pygame.image.load(img)

    def draw(self):
        self.position = self.get_position()
        screen.blit(self.img, self.position)

# class spikes(enemy):
#
#     img = pygame.image.load('spikes.png')
#
#     #def draw(self):
#     #    return  pygame.draw()


spikes = enemy(10, 10, 0, 0, 'spikes.png')
black = 0, 0, 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit();

    screen.fill(black)
    spikes.draw()
    pygame.display.flip()
#toxic_rain = enemy( 20, 15, 0, 0, #img)
#mine = enemy(30, 0, 0, 0, img)
#bear = enemy()

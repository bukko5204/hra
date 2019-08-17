from player import player
import pygame
from sys import exit

pygame.init()

player = player(10, 10)
print(player.x)
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)

if __name__ == '__main__':
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.scancode == 13:
                    y_velocity += 20 * time
                elif event.scancode == 0:
                    x_velocity -= 20 * time
                elif event.scancode == 2:
                    x_velocity += 20 * time

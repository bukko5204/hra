from player import player
from enemies import enemy
from ground import ground
from physics import gravity
from deathscreen import deathscreen
import pygame
from sys import exit

pygame.init()

player = player(10, 10)
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)

while __name__ == '__main__':
    while player.alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     if event.scancode == 13:
            #
            #         y_velocity += 20 * time
            #
            #     elif event.scancode == 0:
            #         x_velocity -= 20 * time
            #     elif event.scancode == 2:
            #         x_velocity += 20 * time
        screen.fill((0, 0, 0))
        ground.draw()
        enemy.draw()
        player.draw()
        pygame.display.flip()

    while not player.alive:
        deathscreen()

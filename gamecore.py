from player import player
from enemies import enemy
from ground import ground
from physics import gravity
#from deathscreen import deathscreen
import pygame
from sys import exit

black = (26, 26, 26)
pygame.init()

player = player(10, 10)
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)
earth = ground(10, 200, 1, 'grass.png')
spikes = enemy(10, 10, 0, 0, 'spikes.png')
#player = player(200, 200)

while __name__ == '__main__':
    while player.alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.scancode == 13:
                    y_velocity += 20 * time

                elif event.scancode == 0:
                    x_velocity -= 20 * time

                elif event.scancode == 2:
                    x_velocity += 20 * time

        screen.fill(black)
        earth.draw()
        spikes.draw()
        player.draw()
        pygame.display.flip()

    while not player.alive:
        deathscreen()

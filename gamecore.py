
import sys
import pygame

pygame.init()

infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

if __name__ == '__main__':
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

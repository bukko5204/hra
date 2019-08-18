import pygame

pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)
restart = pygame.image.load('restart.png')
restart = pygame.transform.scale(restart, (300, 100))
exit = pygame.image.load('exit.png')
exit = pygame.transform.scale(exit, (150, 100))


def deathscreen():
    screen.fill((26, 26, 26))
    screen.blit(restart, (width/2 - width/8, height/3 - height/8))
    screen.blit(exit, (width/2 - 1.3*width/16 , height/2 - height/8))
    pygame.display.flip()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit();
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos == range((width/2 - width/8, height/3 - height/8),
                (width/2, heigth/3):
                player.alive = True
            elif event.pos == (width/2 - 1.3*width/16 , height/2 - height/8):
                pygame.quit()


    deathscreen()

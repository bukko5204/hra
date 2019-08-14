import pygame, sys

pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)

class ground:

    def __init__(self, y, lenght, rotation, img):
        self.y = y
        min_y = self.y
        self.lenght = lenght
        self.img = pygame.image.load(img)
        self.rotation = rotation

    def draw(self):
        self.position = (self.y , int(height*0.95))
        #ground = pygame.draw.rect(screen, (255, 255, 255), (25, 35, 100, 100))
        #screen.blit(ground, self.position)
        screen.blit(self.img, self.position)


earth = ground(10, 10, 10, 'grass.png')

black = 0, 0, 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit();

    screen.fill(black)
    earth.draw()
    pygame.display.flip()

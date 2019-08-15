import pygame, sys

pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height), 0, 32)

class ground:

    def __init__(self, y, lenght, rotation, img):
        self.y = y
        self.lenght = lenght
        self.rotation = rotation
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (self.lenght, 100))
        self.img = pygame.transform.rotate(self.img, self.rotation)
        self.position = (self.y , 10)

    def draw(self):
        screen.blit(self.img, self.position)


earth = ground(10, 200, 1, 'grass.png')

black = 0, 0, 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit();

    screen.fill(black)
    earth.draw()
    pygame.display.flip()

import pygame

class enemy(self,x, y, y_velocity, x_velocity, img):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = img

    def movement(self, y_velocity, x_velocity):
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def position(self.x, self.y):
        position = [self.x, self.y]

    def draw(position, self.img):
        pygame.draw(position, self.imgimg)

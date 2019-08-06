import os
import pygame

_image_library = {}

def get_image(path):
        global _image_library
        img = _image_library.get(path)
        if img == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                img = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return imag

class enemy:

    def __init__(self, x, y, x_velocity, y_velocity, img):
        self.x = x
        self.y = y
        self.y_velocity = y_velocity
        self.x_velocity = x_velocity
        self.img = img

    def position(self):
        position = [self.x, self.y]

    def draw(self):
        pygame.draw(position, self.img)

class spikes(enemy):
    x = 10
    y = 10
    y_velocity = 0
    x_velocity = 0
    img = get_image()
    img = pygame.image.load('autodraw 04_08_2019.png')


spikes = spikes()
#toxic_rain = enemy(toxic_rain, 20, 15, 0, 0, 2.5, #img)

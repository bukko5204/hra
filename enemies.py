import os
import pygame

_image_library = {}

def get_image(path):
        global _image_library
        img = _image_library.get(path)
        if img == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                img = pygame.image.load(canonicalized_path)
                _image_library[path] = img
        return img

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

    img = get_image('spikes.png')
    img = pygame.image.load('spikes.png')

    def draw():
        return  pygame.draw()

spikes = spikes(10, 10, 0, 0, 'spikes.png')
#toxic_rain = enemy( 20, 15, 0, 0, #img)
#mine = enemy(30, 0, 0, 0, img)

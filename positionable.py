class positionable:

    def __init__(self):
        self.x = x
        self.y = y

    def get_position(self):
        self.position = (self.x, self.y)
        return self.position

    def move(self):
        self.x += x_velocity * time
        self.y += y_velocity * time
        self.position = get_position()

    def draw(self):
        self.position = self.get_position()
        screen.blit(self.img, self.position)

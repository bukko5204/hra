from player import player

x_position = 0
y_position = 10
x_velocity = 10
y_velocity = 8
min_y_position = 0

g = 9.81
time = 0.001


def gravity(y_velocity, y_position,
            min_y_position):

    y_velocity -= g * time
    return y_velocity


def colision():
    if int(player.position) == int(ground.position) :
        player.y_velocity = 0.0
    elif int(player.postion) == int(enemy.position):
        player.alive = False





# while y_position > min_y_position:
#
#     y_velocity = gravity(y_velocity, y_position, min_y_position)
#     x_position += x_velocity * time
#     y_position += y_velocity * time
#     print(x_position, y_position, x_velocity, y_velocity)

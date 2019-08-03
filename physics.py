x_position = 0
y_position = 10
x_velocity = 10
y_velocity = 8
min_y_position = 0

g = 9.81

def gravity(y_velocity, y_position, min_y_position):
    if y_position > min_y_position:
        y_velocity -= g
    return y_velocity

while y_position > min_y_position:
    y_velocity = gravity(y_velocity, y_position, min_y_position)
    x_position += x_velocity
    y_position += y_velocity
    print(x_position, y_position, x_velocity, y_velocity)

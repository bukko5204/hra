x_position = 0
y_position = 0
x_velocity = 10
y_velocity = 8
min_y = -1

def Floor(x):
    rounded = int(x)
    if rounded > x:
        rounded -= 1
    return rounded

def Gravity(y_velocity, y_position, Floor):
    if y_position > min_y:
        g = Floor(y_velocity/2)
        y_velocity -= g
    return y_velocity

while True:
    y_velocity = Gravity(y_velocity, y_position, Floor)
    x_position += x_velocity
    y_position += y_velocity
    print(y_velocity)

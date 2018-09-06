from src.tools.parameters import default_max_deceleration, default_max_acceleration, default_time_of_reaction as dt
from src.tools.methods import solve_degree_two

default_max_deceleration = 2


def get_acceleration_non_moving_obstacle(a_min, current_speed, current_pos, current_pos_obstacle):

    # first condition:
    z = 2 * (current_pos_obstacle - current_pos) / (dt ** 2) - 2 * current_speed / dt

    print("z = " + str(z))

    a1 = -(dt ** 2) / a_min
    a2 = (-dt * current_speed / a_min + (dt ** 2) / 2)
    a3 = - (current_speed ** 2) / (2 * a_min) + current_speed * dt + current_pos - current_pos_obstacle

    print("a1 = " + str(a1))
    print("a2 = " + str(a2))
    print("a3 = " + str(a3))

    try:
        x, y = solve_degree_two(a1, a2, a3)
        print("x = " + str(x))
        print("y = " + str(y))
    except:
        print("except")
        return a_min

    # second condition: acceleration must be lower than y

    a = min(y, z, default_max_acceleration)
    print("a = " + str(a))

    # third condition:
    w = current_speed / dt
    print("w = " + str(w))

    return a


a_min = - default_max_deceleration
current_speed = 10
current_pos = 0
current_pos_obstacle = 100

i = 0

while True:
    i += 1
    print(i)

    a = get_acceleration_non_moving_obstacle(a_min, current_speed, current_pos, current_pos_obstacle)

    current_pos = current_pos + current_speed * dt + 0.5 * a * dt ** 2
    current_speed = max(current_speed + a * dt, 0)

    if i > 10:
        current_pos_obstacle = 300

    print("current_speed: " + str(current_speed))
    print("current_pos: " + str(current_pos))



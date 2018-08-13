import numpy as np


def stopping_distance(speed):
    return speed + 0.0796 * (speed ** 2) - 0.0198 * speed


def safety_distance(speed, factor=1.5):
    return factor * stopping_distance(speed)


def find_closest_car(current_car, cars):
    same_direction_cars = [c for c in cars if c.direction == current_car.direction]

    if current_car.direction in ["n"]:
        distances = [c.y - current_car.y if c.y > current_car.y else 1000000 for c in same_direction_cars]

    if current_car.direction in ["s"]:
        distances = [current_car.y - c.y if c.y < current_car.y else 1000000 for c in same_direction_cars]

    if current_car.direction in ["e"]:
        distances = [c.x - current_car.x if c.x > current_car.x else 1000000 for c in same_direction_cars]

    if current_car.direction in ["n"]:
        distances = [current_car.x - c.x if c.x < current_car.x else 1000000 for c in same_direction_cars]

    sorted_indexes = np.argsort(distances)
    closest_car = same_direction_cars[sorted_indexes[0]]

    return closest_car


def compute_distance_and_speed(acceleration, speed, time):
    new_speed = speed + acceleration * time
    distance = speed * time + acceleration * (time**2)
    return new_speed, distance

def find_closest_red_light(current_car, intersections):

    selected_intersections = []
    for i in intersections:
        if current_car.current_street in [i.street_a_id, i.street_b_id]:
            if (current_car.current_street == i.street_a_id and i.state != "a_passing") or (current_car.current_street == i.street_b_id and i.state != "b_passing"):
                selected_intersections.append(i)


    if current_car.direction == "n":
        selected_intersections = [i for i in selected_intersections if i.y >= current_car.y]
        distances = [i.x - current_car.x + i.y - current_car.y for i in selected_intersections]
        sorted_indexes = np.argsort(distances)
        return selected_intersections[sorted_indexes[0]]

    if current_car.direction == "e":
        selected_intersections = [i for i in selected_intersections if i.x >= current_car.x]
        distances = [i.x - current_car.x + i.y - current_car.y for i in selected_intersections]
        sorted_indexes = np.argsort(distances)
        return selected_intersections[sorted_indexes[0]]

    if current_car.direction == "s":
        selected_intersections = [i for i in selected_intersections if i.y <= current_car.y]
        distances = [i.x - current_car.x + i.y - current_car.y for i in selected_intersections]
        sorted_indexes = np.argsort(distances)
        return selected_intersections[sorted_indexes[-1]]

    if current_car.direction == "w":
        selected_intersections = [i for i in selected_intersections if i.x <= current_car.x]
        distances = [i.x - current_car.x + i.y - current_car.y for i in selected_intersections]
        sorted_indexes = np.argsort(distances)
        return selected_intersections[sorted_indexes[0]]


def obstacle_ahead(current_car, intersections, cars, map, car_to_street):
    closest_car = find_closest_car(
        current_car,
        [cars[i] for i in car_to_street[current_car.current_street]]
    )

    closest_red_light = find_closest_car(current_car, intersections)

    # TODO: test this and continue this method
    

























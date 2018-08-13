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

    return closest_car, distances[sorted_indexes[0]]


def compute_distance_and_speed(acceleration, speed, time):
    new_speed = speed + acceleration * time
    distance = speed * time + acceleration * (time**2)
    return new_speed, distance

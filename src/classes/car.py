from src.tools.methods import find_closest_car, compute_distance_and_speed, safety_distance
from src.tools.parameters import default_max_acceleration, default_max_deceleration

class Car:

    def __init__(
            self,
            id,
            x,
            y,
            current_street,
            direction,
            going_to,
            max_speed=30,
            length=4,
            start_date=0,
            max_acceleration=default_max_acceleration,
            max_deceleration=default_max_deceleration
    ):
        self.id = id
        self.max_speed = max_speed
        self.length = length
        self.start_date = start_date
        self.end_date = None
        self.going_to = going_to
        self.x = x
        self.y = y

        self.max_acceleration = max_acceleration
        self.max_deceleration = max_deceleration

        self.coming_from = (self.x, self.y)
        self.current_street = current_street
        self.direction = direction
        self.distance = 0
        self.time_elapsed = 0
        self.speed = 0
        self.acceleration = 0
        self.new_acceleration = 0

    def display(self):
        print("pos x: " + str(self.x))
        print("pos y: " + str(self.y))
        print("speed: " + str(self.speed))
        print("acceleration: " + str(self.acceleration))
        print("new_acceleration: " + str(self.new_acceleration))
        print()
        print()

    def choose_acceleration(self, time, car_to_street, cars):
        closest_car, distance = find_closest_car(self, [cars[i] for i in car_to_street[self.current_street]])

        _, projected_distance = compute_distance_and_speed(closest_car.acceleration, closest_car.speed, time)

        projected_distance += distance

        self.new_acceleration = projected_distance - safety_distance(self.speed) - self.speed * time
        self.new_acceleration /= time ** 2

        self.new_acceleration = max(self.new_acceleration, self.max_deceleration)
        self.new_acceleration = min(self.new_acceleration, self.max_acceleration)

    def move(self, time, intersections, car_to_street, distance=None):

        if self.x == self.going_to[0] and self.y == self.going_to[1]:
            return True
        remaining_distance = None

        if distance is None:
            self.acceleration = self.new_acceleration
            self.speed, distance = compute_distance_and_speed(self.acceleration, self.speed, time)
            self.speed = min(self.max_speed, self.speed)

        if self.direction in ["n", "s"]:
            if self.direction == "n":
                self.y += distance
                if self.y >= self.going_to[1]:
                    remaining_distance = abs(self.y - self.going_to[1])

            if self.direction == "s":
                self.y -= distance
                if self.y <= self.going_to[1]:
                    remaining_distance = abs(self.y + self.going_to[1])

            if remaining_distance is not None:
                # if self.x == self.going_to[0]:
                #     return True
                for i in intersections:
                    if i.y == self.going_to[1] and self.current_street in [i.street_a_id, i.street_b_id]:
                        intersection = i
                        break
                self.y = self.going_to[1]

                if self.x < self.going_to[0]:
                    self.direction = "e"
                else:
                    self.direction = "w"

                car_to_street[self.current_street].remove(self.id)

                self.current_street = intersection.street_a_id \
                                        if self.current_street == intersection.street_b_id \
                                        else intersection.street_a_id

                car_to_street[self.current_street].append(self.id)

                self.move(time, intersection, car_to_street, distance=remaining_distance)

        if self.direction in ["e", "w"]:
            # TODO refacto de tout ca pour moins de répétition de code
            if self.direction == "e":
                self.x += distance
                if self.x >= self.going_to[0]:
                    remaining_distance = abs(self.x - self.going_to[0])

            if self.direction == "w":
                self.x -= distance
                if self.x <= self.going_to[0]:
                    remaining_distance = abs(self.x + self.going_to[0])

            if remaining_distance is not None:
                # if self.y == self.going_to[1]:
                #     return True
                for i in intersections:
                    if i.x == self.going_to[0] and self.current_street in [i.street_a_id, i.street_b_id]:
                        intersection = i
                        break
                self.x = self.going_to[0]

                if self.y < self.going_to[1]:
                    self.direction = "n"
                else:
                    self.direction = "s"

                car_to_street[self.current_street].remove(self.id)

                self.current_street = intersection.street_a_id \
                    if self.current_street == intersection.street_b_id \
                    else intersection.street_a_id

                car_to_street[self.current_street].append(self.id)

                self.move(time, intersection, car_to_street, distance=remaining_distance)

        return False








































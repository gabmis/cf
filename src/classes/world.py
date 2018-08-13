from src.classes.car import Car
from src.classes.map import Map
import matplotlib.pyplot as plt
import time as tmt
from plotly.offline import plot


class World:

    def __init__(
            self
    ):
        self.car_start_dates = []
        self.car_end_dates = []
        self.car_coming_from_x = []
        self.car_coming_from_y = []
        self.car_going_to_x = []
        self.car_going_to_y = []
        self.car_distances = []
        self.id_attributor = 0
        self.map = Map(10, 10, 100)
        self.time = 0
        self.cars = []
        self.car_to_street = {}

        for street in self.map.streets:
            self.car_to_street[street.id] = []

    def spawn_car(self):
        car = Car(
            self.id_attributor,
            0,
            0,
            self.map.streets[0].id,
            "n",
            max_speed=30,
            length=4,
            start_date=self.time,
            going_to=[900, 700]
        )
        self.id_attributor += 1
        self.cars.append(car)
        self.car_to_street[car.current_street].append(car.id)
        car.display()

    def run_step(self, time):

        for car in self.cars:
            car.choose_acceleration(time, self.car_to_street, self.cars)

        for car in self.cars:
            if car.end_date is None:
                if car.move(time, self.map.intersections, self.car_to_street):
                    car.end_date = self.time

        for i in self.map.intersections:
            i.behave(time)

        self.time += time

    def run(self, n_steps, step_time):
        pass

    def run_and_display(self, n_steps, step_time):

        frames = []

        for n in range(n_steps):

            print(n)

            if n == 0:
                self.spawn_car()

            x_pos = []
            y_pos = []
            for car in self.cars:
                x_pos.append(car.x)
                y_pos.append(car.y)

            frames.append({'data': [{'x': x_pos, 'y': y_pos}]})

            self.run_step(step_time)

        for car in self.cars:
            car.display()

        frames.append({'layout': {'title': 'Nice plot !'}})
        figure = {'data': [{'x': frames[0]["data"][0]["x"], 'y': frames[0]["data"][0]["y"]}],
                  'layout': {'xaxis': {'range': [0, 1000], 'autorange': False},
                             'yaxis': {'range': [0, 1000], 'autorange': False},
                             'title': 'Simulation',
                             'updatemenus': [{'type': 'buttons',
                                              'buttons': [{'label': 'Play',
                                                           'method': 'animate',
                                                           'args': [None]}]}]
                             },
                  'frames': frames
                  }

        # plot(figure)

    def get_stats(self):
        pass
























from src.classes.street import Street
from src.classes.intersection import Intersection

import matplotlib.pyplot as plt


class Map:

    def __init__(
            self,
            number_of_vertical_blocks,
            number_of_horizontal_blocks,
            block_size
    ):
        self.number_of_vertical_blocks = number_of_vertical_blocks
        self.number_of_horizontal_blocks = number_of_horizontal_blocks
        self.block_size = block_size

        self.streets = []
        self.street_orientations = []
        self.intersections = []
        self.id_attributor = 0

        self.build_grid()
        self.build_intersections()

    def build_grid(self):
        for i in range(self.number_of_horizontal_blocks):
            self.streets.append(
                Street(
                    i * self.block_size,
                    0,
                    i * self.block_size,
                    self.number_of_vertical_blocks * self.block_size,
                    self.id_attributor
                )
            )
            self.street_orientations.append("ew")
            self.id_attributor += 1

        for j in range(self.number_of_vertical_blocks):
            self.streets.append(
                Street(
                    0,
                    j * self.block_size,
                    self.number_of_horizontal_blocks * self.block_size,
                    j * self.block_size, self.id_attributor
                )
            )
            self.street_orientations.append("ns")
            self.id_attributor += 1

    def build_intersections(self):
        for i in range(self.number_of_horizontal_blocks):
            for j in range(self.number_of_vertical_blocks):
                self.intersections.append(
                    Intersection(
                        i * self.block_size,
                        j * self.block_size,
                        i,
                        self.number_of_horizontal_blocks + j
                    )
                )

    def display(self):
        f = plt.figure(1)

        for street in self.streets:
            plt.plot([street.x1, street.x2], [street.y1, street.y2], 'k-', lw=2, figure=f, color='g')

        plt.show()
























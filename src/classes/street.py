from src.tools.parameters import default_max_speed, default_number_of_lanes


class Street:

    def __init__(
            self,
            x1,
            y1,
            x2,
            y2,
            id,
            max_speed=default_max_speed,
            number_of_lanes=default_number_of_lanes
    ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.id = id
        self.max_speed = max_speed
        self.number_of_lanes = number_of_lanes


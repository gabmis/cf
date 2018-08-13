from src.tools.parameters import default_a_b_time, default_b_a_time, default_lag_time


class Intersection:

    def __init__(
            self,
            x,
            y,
            street_a_id,
            street_b_id,
            a_b_time=default_a_b_time,
            b_a_time=default_a_b_time,
            lag_time=default_lag_time
    ):
        self.street_a_id = street_a_id
        self.street_b_id = street_b_id
        self.a_b_time = a_b_time
        self.b_a_time = b_a_time
        self.lag_time = lag_time
        self.x = x
        self.y = y

        self.state = "a_passing"

        self.running_count = 0

    def behave(self, time):
        self.running_count += time

        if self.state == "a_passing":
            if self.running_count >= self.a_b_time:
                self.state = "lag_a_b"
                self.running_count -= self.a_b_time

        elif self.state == "b_passing":
            if self.running_count >= self.b_a_time:
                self.state = "lag_b_a"
                self.running_count -= self.b_a_time

        elif self.state in ["lag_b_a", "lag_a_b"]:
            if self.running_count >= self.lag_time:
                self.running_count -= self.lag_time
                self.state = "a_passing" if self.state == "lag_b_a" else "b_passing"

        if self.running_count > 0:
            self.behave(0)























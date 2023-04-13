from Agent import Agent
from FoodSource import FoodSource


class Hawk(Agent):
    def __init__(self, sources: FoodSource) -> None:
        super().__init__(sources)

    def add_self_to_source(self):
        if self.location is not None:
            self.location.add_hawk()

    def remove_self_from_source(self):
        if self.location is not None:
            self.location.remove_hawk()
            self.location = None

    def clone(self):
        return Hawk(self.sources)

from Agent import Agent
from FoodSource import FoodSource


class Dove(Agent):
    def __init__(self, sources: FoodSource) -> None:
        super().__init__(sources)

    def add_self_to_source(self):
        self.location.add_dove()

    def remove_self_from_source(self):
        self.location.remove_dove()
        self.location = None

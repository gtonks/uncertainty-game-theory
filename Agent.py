import random

from FoodSource import FoodSource


class Agent:
    def __init__(self, sources: FoodSource) -> None:
        self.__sources = sources
        self.location = None

    def choose_source(self, limit: int=2):
        """
        limit: The number of agents that can be at a source at once.
        """
        assert self.location is None

        random.shuffle(self.__sources)
        for location in self.__sources:
            if location.get_agents() < limit:
                self.location = location
                break
        self.add_self_to_source()
        return location

    def add_self_to_source(self):
        raise NotImplementedError
    
    def remove_self_from_source(self):
        raise NotImplementedError

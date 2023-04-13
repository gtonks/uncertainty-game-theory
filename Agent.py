import random

from FoodSource import FoodSource


class Agent:
    def __init__(self, sources: FoodSource) -> None:
        self.sources = sources
        self.location = None

    def choose_source(self, limit: int=2):
        """
        limit: The number of agents that can be at a source at once.
        """
        assert self.location is None

        random.shuffle(self.sources)
        for location in self.sources:
            if location.get_agents() < limit:
                self.location = location
                break
        self.add_self_to_source()
        return self.location

    def add_self_to_source(self):
        raise NotImplementedError
    
    def remove_self_from_source(self):
        raise NotImplementedError
    
    def get_reward(self):
        """
        Returns:
            -1 to die
             0 to do nothing
             1 to reproduce
        """
        raise NotImplementedError

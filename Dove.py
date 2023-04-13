import random

from Agent import Agent
from FoodSource import FoodSource


class Dove(Agent):
    def __init__(self, sources: FoodSource) -> None:
        super().__init__(sources)

    def add_self_to_source(self):
        if self.location is not None:
            self.location.add_dove()

    def remove_self_from_source(self):
        if self.location is not None:
            self.location.remove_dove()
            self.location = None

    def clone(self):
        return Dove(self.sources)
    
    def get_reward(self):
        """
        Returns:
            -1 to die
             0 to do nothing
             1 to reproduce
        """
        if self.location is None:
            return -1
        else:
            n_agents = self.location.get_agents()
            if n_agents == 1:
                return 1
            else:
                n_hawks = self.location.get_hawks()
                if n_hawks == 1:
                    if random.random() > 0.5:
                        return -1
        return 0

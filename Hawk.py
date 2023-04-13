import random

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
                        return 1
                elif n_hawks == 2:
                    return -1
        return 0

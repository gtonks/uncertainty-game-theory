import random

from Hawk import Hawk
from FoodSource import FoodSource


class Hawk2(Hawk):
    def __init__(self, sources: FoodSource) -> None:
        super().__init__(sources)

    def clone(self):
        return Hawk2(self.sources)
    
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

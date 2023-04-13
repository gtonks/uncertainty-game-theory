import random

from Dove import Dove


class Dove1(Dove):
    def clone(self):
        return Dove1(self.sources)
    
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

import random

from Dove import Dove


class Dove2(Dove):
    def choose_source(self, limit: int = 999999):
        return super().choose_source(limit)

    def clone(self):
        return Dove2(self.sources)
    
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
                n_doves = self.location.get_doves()
                if n_hawks > 0:
                    if random.random() > 1 / n_doves:
                        return -1
                elif random.random() > 2 / n_doves:
                    return -1
        return 0

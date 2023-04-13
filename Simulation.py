import random

from FoodSource import FoodSource
from Agent import Agent
from Dove import Dove
from Hawk import Hawk


class Simulation:
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        self._sources = [FoodSource(i) for i in range(sources)]
        self.n_doves = [doves,]
        self.n_hawks = [hawks,]

    def step(self):
        random.shuffle(self._agents)
        for agent in self._agents:
            agent.choose_source()

        to_kill, to_clone = self.handle_rewards()

        for agent in self._agents:
            agent.remove_self_from_source()

        for agent in to_kill:
            self._agents.remove(agent)

        for agent in to_clone:
            self._agents.append(agent.clone())

        n_doves = 0
        n_hawks = 0
        for agent in self._agents:
            if isinstance(agent, Dove):
                n_doves += 1
            elif isinstance(agent, Hawk):
                n_hawks += 1
        self.n_doves.append(n_doves)
        self.n_hawks.append(n_hawks)

    def handle_rewards(self):
        """
        Returns a tuple:
            (agents_to_kill, agents_to_clone)
        """
        raise NotImplementedError

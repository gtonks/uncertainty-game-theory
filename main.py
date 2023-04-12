import random

from FoodSource import FoodSource
from Dove import Dove
from Hawk import Hawk


class Part1:
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        #self.__n_sources = sources
        self.__sources = [FoodSource() for _ in range(sources)]
        self.__doves = [Dove(self.__sources) for _ in range(doves)]
        self.__hawks = [Hawk(self.__sources) for _ in range(hawks)]
        self.n_doves = [doves,]
        self.n_hawks = [hawks,]

    def step(self):
        agents = self.__doves + self.__hawks
        random.shuffle(agents)
        to_remove = list()
        for agent in agents:
            if agent.choose_source() is None:
                to_remove.append(agent)
        for agent in to_remove:
            if agent is Dove:
                self.__doves.remove(agent)
            else:
                self.__hawks.remove(agent)
        self.n_doves.append(len(self.__doves))
        self.n_hawks.append(len(self.__hawks))
        for agent in agents:
            agent.remove_self_from_source()


if __name__ == "__main__":
    random.seed(42)
    sim = Part1(10, 20, 0)
    for i in range(20):
        sim.step()
        print(f"{sim.n_doves[i]} {sim.n_hawks[i]}")

import random

from FoodSource import FoodSource
from Dove import Dove
from Hawk import Hawk


class Part1:
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        #self.__n_sources = sources
        self.__sources = [FoodSource(i) for i in range(sources)]
        self.__doves = [Dove(self.__sources) for i in range(doves)]
        self.__hawks = [Hawk(self.__sources) for i in range(hawks)]
        self.n_doves = [doves,]
        self.n_hawks = [hawks,]

    def step(self):
        agents = self.__doves + self.__hawks
        random.shuffle(agents)
        to_kill = list()
        for agent in agents:
            new_source = agent.choose_source()
            if new_source is None:
                to_kill.append(agent)
        #     else:
        #         print(new_source.id, end='')
        # print()
        for agent in to_kill:
            if type(agent) is Dove:
                self.__doves.remove(agent)
            elif type(agent) is Hawk:
                self.__hawks.remove(agent)
            else:
                raise TypeError(f"Error: Can't kill {type(agent)}")
        self.n_doves.append(len(self.__doves))
        self.n_hawks.append(len(self.__hawks))
        for agent in agents:
            agent.remove_self_from_source()


if __name__ == "__main__":
    random.seed(42)
    sim = Part1(10, 30, 0)
    for i in range(20):
        sim.step()
        print(f"{sim.n_doves[i]} {sim.n_hawks[i]}")

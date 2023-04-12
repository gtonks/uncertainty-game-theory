import random

from FoodSource import FoodSource
from Dove import Dove
from Hawk import Hawk


class Part1:
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        #self.__n_sources = sources
        self.__sources = [FoodSource(i) for i in range(sources)]
        self.__agents = [Dove(self.__sources) for i in range(doves)] + [Hawk(self.__sources) for i in range(hawks)]
        self.n_doves = [doves,]
        self.n_hawks = [hawks,]

    def step(self):
        random.shuffle(self.__agents)
        for agent in self.__agents:
            agent.choose_source()
        #     else:
        #         print(new_source.id, end='')
        # print()
        to_kill = list()
        to_clone = list()
        for agent in self.__agents:
            if agent.location is None:
                to_kill.append(agent)
            else:
                agents_at_loc = agent.location.get_agents()
                if agents_at_loc == 1:
                    to_clone.append(agent)
                else:
                    pass

        for agent in to_kill:
            self.__agents.remove(agent)

        for agent in self.__agents:
            agent.remove_self_from_source()

        for agent in to_clone:
            self.__agents.append(agent.clone())

        self.n_doves.append(0)
        self.n_hawks.append(0)
        for agent in self.__agents:
            if type(agent) is Dove:
                self.n_doves[-1] += 1
            elif type(agent) is Hawk:
                self.n_hawks[-1] += 1


if __name__ == "__main__":
    random.seed(42)
    sim = Part1(10, 3, 0)
    for i in range(20):
        sim.step()
        print(f"{sim.n_doves[i]} {sim.n_hawks[i]}")

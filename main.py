import random

from FoodSource import FoodSource
from Dove import Dove
from Hawk import Hawk


class Part1:
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        self.__n_sources = sources
        self.__sources = [FoodSource() for _ in range(sources)]
        self.__doves = [Dove() for _ in range(doves)]
        self.__hawks = [Hawk() for _ in range(hawks)]

    def step(self):
        agents = self.__doves + self.__hawks
        random.shuffle(agents)
        for agent in agents:


if __name__ == "__main__":
    random.seed(42)

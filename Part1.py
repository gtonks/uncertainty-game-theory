import random

from Simulation import Simulation
from Dove1 import Dove1
from Hawk1 import Hawk1


class Part1(Simulation):
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        super().__init__(sources, doves, hawks)
        self._agents = [Dove1(self._sources) for i in range(doves)] + [Hawk1(self._sources) for i in range(hawks)]


if __name__ == "__main__":
    random.seed(42)
    sim = Part1(sources=60, doves=60, hawks=60)
    for i in range(20):
        sim.step()
        print(f"{sim.n_doves[i]} {sim.n_hawks[i]}")

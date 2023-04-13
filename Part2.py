import random

from Simulation import Simulation
from Dove2 import Dove2
from Hawk2 import Hawk2


class Part2(Simulation):
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        super().__init__(sources, doves, hawks)
        self._agents = [Dove2(self._sources) for i in range(doves)] + [Hawk2(self._sources) for i in range(hawks)]

    def rewards(self):
        pass


if __name__ == "__main__":
    random.seed(42)
    sim = Part2(sources=60, doves=60, hawks=60)
    for i in range(20):
        sim.step()
        print(f"{sim.n_doves[i]} {sim.n_hawks[i]}")

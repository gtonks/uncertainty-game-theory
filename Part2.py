import random

from Simulation import Simulation
from Dove2 import Dove2
from Hawk2 import Hawk2


class Part2(Simulation):
    def __init__(self, sources: int, doves: int, hawks: int) -> None:
        super().__init__(sources, doves, hawks)
        self._agents = [Dove2(self._sources) for i in range(doves)] + [Hawk2(self._sources) for i in range(hawks)]

    def handle_rewards(self):
        """
        Returns a tuple:
            (agents_to_kill, agents_to_clone)
        """
        to_kill = list()
        to_clone = list()

        fights = dict([(source.id, list()) for source in self._sources])
        for hawk in self._agents:
            reward = hawk.get_reward()
            if reward == -1:
                to_kill.append(hawk)
            elif reward == 1:
                to_clone.append(hawk)
            elif reward == -2:
                fights[hawk.location.id].append(hawk)

        for fight in fights.values():
            if len(fight) > 0:
                win_xp = -1
                for hawk in fight:
                    if hawk.xp > win_xp:
                        # This agent is winning
                        win_xp = hawk.xp
                    elif hawk.xp == win_xp:
                        # Neither this agent nor the one that previously set the record win
                        win_xp += 0.5
                for hawk in fight:
                    if hawk.xp == win_xp:
                        if hawk.location.get_doves() == 0:
                            to_clone.append(hawk)
                    else:
                        to_kill.append(hawk)

        return to_kill, to_clone


if __name__ == "__main__":
    random.seed(42)
    sim = Part2(sources=60, doves=60, hawks=60)
    for i in range(20):
        sim.step()
        print(f"{sim.n_doves[i]} {sim.n_hawks[i]}")

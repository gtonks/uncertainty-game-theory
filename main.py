import random
import matplotlib.pyplot as plt

from Part1 import Part1
from Part2 import Part2


random.seed(42)
sim_len = 150
n_sources = 600
n_doves = 60
n_hawks = 60

for sim in (Part1(n_sources, n_doves, n_hawks), Part2(n_sources, n_doves, n_hawks)):
    for i in range(sim_len):
        sim.step()
        print(f"{sim.n_doves[i]} {sim.n_hawks[i]}")
    plt.plot(sim.n_doves, label="Doves")
    plt.plot(sim.n_hawks, label="Hawks")
    plt.legend()
    plt.title(f"{type(sim).__name__} Simulation")
    plt.xlabel("Time Step")
    plt.ylabel("Number of Agents")
    plt.show()
    print()

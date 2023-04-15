import sys
import random
import matplotlib.pyplot as plt

from Part1 import Part1
from Part2 import Part2


random.seed(42)
sim_len = 150
n_sources = 60
n_doves = 119
n_hawks = 1
if len(sys.argv) == 4:
    try:
        n_sources = int(sys.argv[1])
        n_doves = int(sys.argv[2])
        n_hawks = int(sys.argv[3])
    except ValueError:
        print("Usage: python main.py [SOURCES DOVES HAWKS]")
        print("SOURCES, DOVES and HAWKS must be nonnegative integers")
        exit()
    try:
        assert n_sources >= 0
        assert n_doves >= 0
        assert n_hawks >= 0
    except AssertionError:
        print("Usage: python main.py [SOURCES DOVES HAWKS]")
        print("SOURCES, DOVES and HAWKS must be nonnegative integers")
        exit()
elif len(sys.argv) != 1:
        print("Usage: python main.py [SOURCES DOVES HAWKS]")
        exit()

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

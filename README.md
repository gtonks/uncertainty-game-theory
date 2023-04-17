# uncertainty-game-theory
Uncertainty Assignment 5: Game Theory


## Usage
```
python main.py [SOURCES DOVES HAWKS]
```
When run without arguments, the program defaults to 60 food sources, 119 doves and 1 hawk. Otherwise, enter three integers corresponding the desired number of each item.

`main.py` will simulate Part 1 first, then Part 2.


## Results
In the first part (`Figures/Part1.png`), the doves and hawks reached equilibrium when there were roughly equal numbers of both of them. In the second part (`Figures/Part1.png`), the doves have a clear advantage over the hawks. I think that this is mostly due to hawks no longer having a chance of reproducing when they run into doves. The result is that there are slightly fewer hawks than before, which leads to many more doves than before. Overall, more agents can survive at equilibrium in the second example with the default starting conditions.

Another insteresting insight is that the doves can no longer achieve a maximum population of 120 individuals in Part 2, even when no hawks are present (see `Figures/Part2_no_hawks.png`; compare with `Figures/Part1_no_hawks.png`).

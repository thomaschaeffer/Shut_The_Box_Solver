# Shut the Box Solver
A Python implementation of the Shut the Box game and a solver that calculates the probability of winning.

# Features
Play the game in the terminal.
Calculate winning probabilities.
Compare optimized and unoptimized solvers.
Plot execution times.

# Usage
Run the game: 
```bash
python -m shut_the_box.game
```

Run the solver performance comparison:
```bash
python -m shut_the_box.plot
```

Run the solver to obtains the probability to win:
```bash
python -m shut_the_box.solver
```

Run tests:
```bash
python -m pytest
```

The optimized solver uses memoization to avoid recalculating previously evaluated states.
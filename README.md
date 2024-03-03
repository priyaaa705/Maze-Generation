# Maze-Generation
Artificial Intelligence Assignment 1 - TCD

For this assignment, the open-source repository [pyamaze](https://github.com/MAN1986/pyamaze) has been utilized.

Requirements: 
```
pip install -r requirements.txt
```

If the requirements.txt doesn't work, the `pyamaze` library can be installed using:

```
pip install pyamaze
```

### Commands
1. Run the Main.py file:

The GUI allows changing parameters such as:
1. Grid Size
2. Goal Location
3. Algorithms to run together

### Defaults
Grid:
1. Rows: `30`
2. Cols: `30`
3. Goal: `(1, 1)` (Top Left) 

Search Algorithm:
The selected algorithms will run together:
1. DFS - Selected
2. BFS - Selected
3. AStar - Selected

Markov Decision Process:
The selected algorithms will run together:
1. Value Iteration - Selected
2. Policy Iteration - Selected

## Search Algorithms

To run, select checkboxes from the Search Algorithm section and click on the "Run Algos" button. It will execute the selected algorithm using the specified grid size and goal.
- Select any algorithm
- Click on `RUN SEARCH ALGOS`
- The algorithm will run in a new window

#### Analysis Parameters
To compare the algorithms, three metrics are displayed on top of the maze:
1. Final Path
2. Searched Path
3. Time Taken

## Markov Decision Process

To run, select checkboxes from the MDP section and click on the "Run Markov" button. It will execute the selected algorithm using the specified grid size and goal.
- Select any algorithm
- Click on `RUN MDP`
- The algorithm will run in a new window

#### Analysis Parameters
To compare the algorithms, three metrics are displayed on top of the maze:
1. Final Path 
2. Searched Path
2. Time Taken

## References

[1] MAN1986, (2021) pyamaze [Source Code] https://github.com/MAN1986/pyamaze

[2] Paul E. Black, "Manhattan distance", in Dictionary of Algorithms and Data Structures [online], Paul E. Black, ed. 11 February 2019. Available from: https://www.nist.gov/dads/HTML/manhattanDistance.html

[3] Paul E. Black, "Euclidean distance", in Dictionary of Algorithms and Data Structures [online], Paul E. Black, ed. 17 December 2004. Available from: https://www.nist.gov/dads/HTML/euclidndstnc.html

[4] Russell, S.J. and Norvig, P. (2022) Artificial Intelligence: A modern approach. Harlow: Pearson Education Limited.

[5] MDP_VI_PI_Q-learning_AIMA.ipynb by Tirthajyoti Sarkar: https://github.com/tirthajyoti/RL_basics

[6] Markov Decision Process by Joseph Su. Department of Computer Science, Georgia Institute of Technology: https://jsu800.github.io/docs/ml_mdp.pdf

[7] MazeMDP by Sally Gao. GitHub Repository: https://github.com/sally-gao/mazemdp

from pyamaze import maze, COLOR, agent, textLabel
import SearchAlgos as Algo
from MDP import ValueIteration, PolicyIteration
import timeit
import Visualisation as gui
import matplotlib.pyplot as plt

rows, cols = grid = (int(gui.rows), int(gui.cols))
goal_x, goal_y = GOAL = (int(gui.goal_x), int(gui.goal_y))

# -----------------MAZE----------------------
m = maze(rows=rows, cols=cols)
m.CreateMaze(x=goal_x, y=goal_y, pattern=None,
             theme=COLOR.dark, loopPercent=100)

# Collect metrics
time_metrics = {'DFS': [], 'BFS': [], 'A*': [], 'ValueIteration': [], 'PolicyIteration': []}
# Steps metric will exclude MDP algorithms
steps_metrics = {'DFS': [], 'BFS': [], 'A*': [], 'ValueIteration': [], 'PolicyIteration': []}

if gui.run_search_algos:
    # -----------------SEARCH ALGO----------------------
    Algo.NODES = 'ESNW'
    
    dfsPath = None
    bfsPath = None
    aStarPath = None
    agents = [0, 0, 0]

    for idx, val in enumerate(gui.AlgoRun):
        # -----------------DFS-----------------------
        if idx == 0 and val:
            DFS = Algo.DFS(m=m, goal=GOAL)
            DFS.set_params()
            # DFS.measure_memory_usage()
            DFS.search_path()
            dfsPath, dfsSearchedPath, calcDFSTime = DFS.get_forward_path()

            d = agent(parentMaze=m,
                      x=None, y=None,
                      shape='square', footprints=True, filled=True,
                      color=COLOR.green)

            agents[0] = d

            totalDFSPath = textLabel(m, f'DFS Path', len(dfsPath) + 1)
            totalDFSSearchedPath = textLabel(m, f'DFS Searched Path', dfsSearchedPath)
            totalDFSTime = textLabel(m, f'DFS Time', round(calcDFSTime * 1000, 4))
            # totalDFSMemory = textLabel(m, f'DFS Memory', round(DFS.memory_usage / 10**6, 4))

        # -----------------BFS-----------------------
        if idx == 1 and val:
            BFS = Algo.BFS(m=m, goal=GOAL)
            BFS.set_params()
            # BFS.measure_memory_usage()
            BFS.search_path()
            bfsPath, bfsSearchedPath, calcBFSTime = BFS.get_forward_path()

            b = agent(parentMaze=m,
                      x=None, y=None,
                      shape='square', footprints=True, filled=True,
                      color=COLOR.blue)

            agents[1] = b

            totalBFSPath = textLabel(m, f'BFS Path', len(bfsPath) + 1)
            totalBFSSearchedPath = textLabel(m, f'BFS Searched Path', bfsSearchedPath)
            totalBFSTime = textLabel(m, f'BFS Time', round(calcBFSTime * 1000, 4))
            # totalBFSMemory = textLabel(m, f'BFS Memory', round(BFS.memory_usage / 10**6, 4))

        # -----------------A*------------------------
        if idx == 2 and val:
            AStar = Algo.AStar(m=m, goal=GOAL)
            AStar.set_params()
            # AStar.measure_memory_usage()
            AStar.search_path()
            aStarPath, aStarSearchedPath, calcAStarTime = AStar.get_forward_path()

            a = agent(parentMaze=m,
                      x=None, y=None,
                      shape='square', footprints=True, filled=False,
                      color=COLOR.red)

            agents[2] = a

            totalAStarPath = textLabel(m, f'A* Path', len(aStarPath) + 1)
            totalAStarSearchedPath = textLabel(m, f'A* Searched Path', aStarSearchedPath)
            totalAStarTime = textLabel(m, f'A* Time', round(calcAStarTime * 1000, 4))
            # totalAStarMemory = textLabel(m, f'AStar Memory', round(AStar.memory_usage / 10**6, 4))

    tracingDict = {}
    for i, val in enumerate([dfsPath, bfsPath, aStarPath]):
        if val is not None:
            tracingDict[agents[i]] = val

    # ----------------TRACING--------------------
    m.tracePath(tracingDict,
                delay=2, kill=False,
                showMarked=True)
    m.run()

    # Print BFS Path
    print("BFS Path:", bfsPath)
    # Print DFS Path
    print("DFS Path:", dfsPath)
    # Print A* Path
    print("A* Path:", aStarPath)
    # Print BFS Searched Path
    print("BFS Searched Path:", bfsSearchedPath)
    # Print DFS Searched Path
    print("DFS Searched Path:", dfsSearchedPath)
    # Print A* Searched Path
    print("A* Searched Path:", aStarSearchedPath)
    # Print BFS Time
    print("BFS Time (ms):", round(calcBFSTime * 1000, 4))
    # Print DFS Time
    print("DFS Time (ms):", round(calcDFSTime * 1000, 4))
    # Print A* Time
    print("A* Time (ms):", round(calcAStarTime * 1000, 4))

if gui.run_mdp_algo:
    # -----------------ALGO----------------------
    setDeterministic = True

    # -----------------AGENT---------------------
    agents = [0, 0]

    pathVI = None
    pathPI = None
    # -----------------PATH----------------------
    if gui.SetValueIteration:
        print(GOAL)

        trackVI = ValueIteration(m, GOAL, isDeterministic=setDeterministic)
        trackVI.calculate_valueIteration()
        pathVI, timeVI, stepsVI = trackVI.create_searchPath((rows, cols))
        steps_metrics['ValueIteration'].append(stepsVI)  # Add VI steps to metrics
        # trackVI.measure_memory_usage(trackVI.calculate_valueIteration)
        pathVI, timeVI, stepsVI = trackVI.create_searchPath((rows, cols))
        
        v = agent(m, shape='arrow', footprints=True, color=COLOR.red)
        agents[0] = v

        totalVIPath = textLabel(m, f'Value Iteration Path', len(pathVI) + 1)
        totalVITime = textLabel(m, f'Value Iteration Time', round(timeVI * 1000, 4))
        # totalVIMemory = textLabel(m, f'Value Iteration Memory Peak', round(trackVI.memory_usage / 10**6, 4))

    if gui.SetPolicyIteration:
        print(GOAL)
        
        trackPI = PolicyIteration(m, GOAL, isDeterministic=setDeterministic)
        trackPI.calculate_policyIteration()
        pathPI, timePI, stepsPI = trackPI.create_searchPath((rows, cols))
        steps_metrics['PolicyIteration'].append(stepsPI)  # Add PI steps to metrics
        # trackPI.measure_memory_usage(trackPI.calculate_policyIteration)
        p = agent(m, shape='square', footprints=True, color=COLOR.blue)
        agents[1] = p

        totalPIPath = textLabel(m, f'Policy Iteration Path', len(pathPI) + 1)
        totalPITime = textLabel(m, f'Policy Iteration Time', round(timePI * 1000, 4))
        # totalPIMemory = textLabel(m, f'Policy Iteration Memory Peak', round(trackPI.memory_usage / 10**6, 4))

    tracingDict = {}
    for i, val in enumerate([pathVI, pathPI]):
        if val is not None:
            tracingDict[agents[i]] = val

    # ----------------TRACING--------------------
    m.tracePath(tracingDict, delay=200)
    m.run()

    # Print Value Iteration Path
    print("Value Iteration Path:", pathVI)
    # Print Policy Iteration Path
    print("Policy Iteration Path:", pathPI)
    # Print Value Iteration Time
    print("Value Iteration Time (ms):", round(timeVI * 1000, 4))
    # Print Policy Iteration Time
    print("Policy Iteration Time (ms):", round(timePI * 1000, 4))

# Print the maze values
def print_maze(m):
    for row in range(1, m.rows+1):
        for col in range(1, m.cols+1):
            cell = (row, col)
            cell_str = ''
            if m.maze_map[cell]['N']:
                cell_str += 'N'
            if m.maze_map[cell]['S']:
                cell_str += 'S'
            if m.maze_map[cell]['E']:
                cell_str += 'E'
            if m.maze_map[cell]['W']:
                cell_str += 'W'
            print(f"({row},{col})", end=' | ')
        print()  # Newline after each row

# Example usage after creating and setting up your maze 'm'
print_maze(m)    

# Function to run algorithms and collect metrics
def run_algorithms_and_collect_metrics(rows, cols, goal):
    m = maze(rows=rows, cols=cols)
    m.CreateMaze(loopPercent=100)

    metrics = {}

    # DFS
    dfs = Algo.DFS(m=m, goal=goal)
    dfs.set_params()
    dfs.search_path()
    _, dfs_steps, dfs_time = dfs.get_forward_path()
    metrics['DFS'] = (dfs_time, dfs_steps)

    # BFS
    bfs = Algo.BFS(m=m, goal=goal)
    bfs.set_params()
    bfs.search_path()
    _, bfs_steps, bfs_time = bfs.get_forward_path()
    metrics['BFS'] = (bfs_time, bfs_steps)

    # A*
    a_star = Algo.AStar(m=m, goal=goal)
    a_star.set_params()
    a_star.search_path()
    _, a_star_steps, a_star_time = a_star.get_forward_path()
    metrics['A*'] = (a_star_time, a_star_steps)

    # ValueIteration
    vi = ValueIteration(m=m, goal=goal, isDeterministic=True)
    vi.calculate_valueIteration()
    _, vi_time, vi_steps = vi.create_searchPath((rows, cols))
    metrics['ValueIteration'] = (vi_time, vi_steps)

    # PolicyIteration
    pi = PolicyIteration(m=m, goal=goal, isDeterministic=True)
    pi.calculate_policyIteration()
    _, pi_time, pi_steps = pi.create_searchPath((rows, cols))
    metrics['PolicyIteration'] = (pi_time, pi_steps)

    return metrics

# Initialize metrics dictionaries
time_metrics = {'DFS': [], 'BFS': [], 'A*': [], 'ValueIteration': [], 'PolicyIteration': []}
steps_metrics = {'DFS': [], 'BFS': [], 'A*': [], 'ValueIteration': [], 'PolicyIteration': []}

# Example maze sizes and goal
maze_sizes = [(5, 15), (20, 10), (15, 25), (30, 30), (50,50)]
goal = (1, 1)

# Collect metrics for each maze size
for size in maze_sizes:
    rows, cols = size
    metrics = run_algorithms_and_collect_metrics(rows, cols, goal)
    for algo, (time, steps) in metrics.items():
        time_metrics[algo].append(time)
        steps_metrics[algo].append(steps)

def plot_metrics(metrics, title, ylabel):
    plt.figure(figsize=(10, 6))
    
    # Define a dictionary for different markers
    markers = {
        'DFS': 'o',  # Circle
        'BFS': 's',  # Square
        'A*': 'v',   # Triangle up
        'ValueIteration': 'd',  # Diamond
        'PolicyIteration': 'p',  # Pentagon
    }
    
    for algo, values in metrics.items():
        print(f"Plotting {algo} with values: {values}")  # Debug print
        if values:  # Ensure there are values to plot
            plt.plot([f"{size[0]}x{size[1]}" for size in maze_sizes], values, 
                     marker=markers[algo], linestyle='-', label=algo)
    plt.title(title)
    plt.xlabel('Maze Size')
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Generate plots
plot_metrics(time_metrics, 'Algorithm Time Comparison', 'Time (seconds)')
plot_metrics(steps_metrics, 'Algorithm Steps Comparison', 'Steps Taken')

# Generate table
plt.figure(figsize=(10, 6))
plt.axis('off')
cell_text = []
for size, (time_values, steps_values) in zip(maze_sizes, zip(*[time_metrics.values(), steps_metrics.values()])):
    for algo, time, steps in zip(time_metrics.keys(), time_values, steps_values):
        cell_text.append([f"{size[0]}x{size[1]}", algo, f"{time:.2e}", steps])

plt.table(cellText=cell_text, colLabels=['Maze Size', 'Algorithm', 'Time Taken (s)', 'Steps Taken'], loc='center')
plt.title('Algorithm Comparison')
plt.show()

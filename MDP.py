import random, time

class MarkovDecisionProcess:
    def __init__(self, m=None, goal=None, isDeterministic=True):
        self.m = m
        self.goal = goal
        self.actions = {}

        self._discount = 0.9

        self.isDeterministic = isDeterministic
        self.create_actions()

        self.target = [self.goal]

    def set_heuristics(self):
        for key, value in self.actions.items():
            for k, v in value.items():
                # NON DETERMINISTIC
                if k == 'N':
                    value[k] = 0.8
                elif k == 'W':
                    value[k] = 0.1
                elif k == 'E':
                    value[k] = 0.5
                elif k == 'S':
                    value[k] = 0.5

    def create_actions(self):

        # DETERMINISTIC
        for key, val in self.m.maze_map.items():
            self.actions[key] = dict([(k, v) for k, v in val.items() if v == 1])

        # CHANGE TO STOCHASTIC
        if not self.isDeterministic:
            self.set_heuristics()

    def calculate_ValueIterationUtility(self, prob, reward, stateNext, utility):
        return prob * (reward + self._discount * utility[stateNext])

    def calculate_PolicyIterationUtility(self, prob, reward, state, stateNext, utility):
        return reward[state] + self._discount * (prob * utility[stateNext])

    def move(self, currentNode, direction):
        if direction == 'E':
            return currentNode[0], currentNode[1] + 1
        elif direction == 'W':
            return currentNode[0], currentNode[1] - 1
        elif direction == 'N':
            return currentNode[0] - 1, currentNode[1]
        elif direction == 'S':
            return currentNode[0] + 1, currentNode[1]

class ValueIteration(MarkovDecisionProcess):
    def __init__(self, m=None, goal=None, isDeterministic=True):

        super().__init__(m, goal, isDeterministic)

        self._reward = -4  # LIVING REWARD
        self._max_error = 10 ** (-3)

        self.target = [self.goal]
        self.values = {state: 0 for state in self.actions.keys()}
        self.values[self.target[0]] = 1

        self.algoPath = {}

        self.explored = []

        self.mainTime = 0

    def get_maxDelta(self, delta, utilityMax, state):
        return max(delta, abs(utilityMax - self.values[state]))

    def calculate_valueIteration(self):
        start = time.time()
        while True:
            delta = 0
            for state in self.actions.keys():
                if state == self.target[0]:
                    continue
                    
                utilityMax = float("-inf")
                
                for action, prob in self.actions[state].items():
                    for direction in action:
                        if self.m.maze_map[state][direction]:
                            childCell = self.move(state, direction)
                    reward = self._reward
                    if childCell == self.target[0]:
                        reward = 10000
                    utility = 0

                    utility += super().calculate_ValueIterationUtility(prob, reward, childCell, self.values)

                    if utility > utilityMax:
                        utilityMax = utility
                        
                delta = self.get_maxDelta(delta, utilityMax, state)

                self.values[state] = utilityMax

            if delta < self._max_error:
                break
        end = time.time()
        self.mainTime = end-start

    def create_searchPath(self, currNode):
        start = time.time()
        node = currNode
        steps = 0  # Initialize step counter

        while True:
            if node == self.target[0]:
                break

            selectedNode = None
            selectedNodeVal = None

            for direction in 'ENWS':
                if self.m.maze_map[node][direction]:
                    traverseDirection = self.move(node, direction)
                    
                    # If the traverseDirection is directly the target, select it immediately
                    if traverseDirection == self.target[0]:
                        selectedNode = traverseDirection
                        break

                    # For Value Iteration, use the utility values to select the next node
                    if selectedNodeVal is None or self.values[traverseDirection] > selectedNodeVal:
                        selectedNode = traverseDirection
                        selectedNodeVal = self.values[selectedNode]

            if selectedNode:
                steps += 1  # Increment step counter only if a new node is selected
                self.explored.append(node)  # Mark the current node as explored
                self.algoPath[node] = selectedNode  # Record the path
                node = selectedNode  # Move to the next node

        end = time.time()
        self.mainTime = end - start
        return self.algoPath, self.mainTime, steps

class PolicyIteration(MarkovDecisionProcess):
    def __init__(self, m=None, goal=None, isDeterministic=True):

        super().__init__(m, goal, isDeterministic)

        self.target = [self.goal]

        self.values = {state: 0 for state in self.actions.keys()}
        self.values[self.target[0]] = pow(10, 7)

        self.policyValues = {s: random.choice('N') for s in self.actions.keys()}

        self._reward = {state: -40 for state in self.actions.keys()}  # LIVING REWARD
        self._reward[self.target[0]] = pow(10, 8)

        self.algoPath = {}
        self.mainTime = 0

    def calculate_policyIteration(self):
        start = time.time()
        policyTrigger = True
        while policyTrigger:
            policyTrigger = False
            valueTrigger = True

            while valueTrigger:
                valueTrigger = False

                for state in self.actions.keys():
                    if state == self.target[0]:
                        continue

                    utilityMax = float('-infinity')
                    actionMax = None

                    for action, prob in self.actions[state].items():
                        for direction in action:
                            if self.m.maze_map[state][direction]:
                                childNode = self.move(state, direction)

                        utility = super().calculate_PolicyIterationUtility(prob, self._reward, state, childNode,
                                                                           self.values)

                        if utility > utilityMax:
                            utilityMax = utility
                            actionMax = action

                        self.policyValues[state] = actionMax
                        self.values[state] = utilityMax

                        if self.policyValues[state] != actionMax:
                            policyTrigger = True
                            self.policyValues[state] = actionMax

        end = time.time()
        self.mainTime = end-start
        
    def create_searchPath(self, currNode):
        start = time.time()
        node = currNode
        steps = 0  # Initialize step counter

        while node != self.target[0]:
            # Determine the next node based on the current policy
            nextNode = self.move(node, self.policyValues[node])

            if nextNode != node:  # Check to ensure we're not stuck in the same node
                steps += 1  # Increment step counter when moving to a new node

            self.algoPath[node] = nextNode
            node = nextNode  # Move to the next node

            if node == self.target[0]:  # Break the loop if the target is reached
                break

        end = time.time()
        self.mainTime = end - start
        return self.algoPath, self.mainTime, steps

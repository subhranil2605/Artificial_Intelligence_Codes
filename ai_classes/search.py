from ai_classes.problem import GraphProblem
from ai_classes.node import Node
from collections import deque


# breadth first search
def breadth_first_search(problem: GraphProblem):
    node = Node(problem.initial)

    if problem.goal_test(node.state):
        return node

    frontier = deque([node])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child.path()

                frontier.append(child)
    return None


# depth first search
def depth_first_search(problem: GraphProblem):
    frontier: list = [(Node(problem.initial))]
    explored = set()

    while frontier:
        node = frontier.pop()

        if problem.goal_test(node.state):
            return node.path()

        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)

    return None

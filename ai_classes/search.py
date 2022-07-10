from ai_classes.problem import GraphProblem
from collections import deque
from node import Node


class Search:
    def __init__(self):
        pass

    @staticmethod
    def breadth_first_search(problem):
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

from __future__ import annotations
from abc import ABC, abstractmethod
from collections import deque
import numpy as np
import heapq


class Problem(ABC):
    """
    Blueprint of the various problems i.e., Abstract class of the problems
    """

    def __init__(self, initial: str, goal: str = None):
        self.initial: str = initial  # initial state
        self.goal: str = goal  # goal state

    @abstractmethod
    def actions(self, state: str):
        """
        getting the children (list of child) of a node
        
        :param state: current state
        :raises ImplementationError: If not implemented in the extended class 
        """
        pass

    def goal_test(self, state: str) -> bool:
        """
        Test for the state is the goal state or not
        
        :param state: current state
        :returns: if the self.goal and current state are same then returns True ele False
        """
        return state == self.goal


class GraphProblem(Problem):
    """
    Extends from the abstract class Problem, it represents the Graph related problems
    like Travelling in Romania problem, etc.
    """

    def __init__(self, initial: str, goal: str, graph: Graph):
        """
        constructor of the GraphProblem
        
        :param initial: initial state of the proble
        :param goal: goal state of the problem
        :param graph: Graph instance of the problem
        """
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, A: str) -> list:
        """
        neighbor or child of the parent
        
        :param A: the node to be expanded to get the list of the children
        :returns: list of the children
        """
        return list(self.graph.get(A))

    def path_cost(self, cost_so_far, A, B):
        """
        calculate path cost
        """
        return cost_so_far + self.graph.get(A, B)

    def h(self, node):
        """
        heuristic value
        """
        heuristic_values = getattr(self.graph, 'heuristics', None)

        return heuristic_values[node]


class Graph:
    """
    Graph class
    
    """

    def __init__(self, graph_dict: dict = None, directed: bool = True):
        """
        constructor of the Graph
        
        :param graph_dict: dictionary representation of the problem
        :param directed: if the dictionary is directed or not
        """
        self.graph_dict: dict = graph_dict or {}
        self.directed: bool = directed

        # convert the directed graph into the undirected one
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """
        Algorithm to converts the directed graph into an undirected one.
        """
        for parent in list(self.graph_dict.keys()):  # parent: keys of the dict
            for child in self.graph_dict[parent]:  # each child of the parent

                # if the child is in the dict i.e., there exists a key in the dict named as the current child
                if child in self.graph_dict:
                    # if the parent of which the current child is generated
                    # is not the list of the child's value
                    if parent not in self.graph_dict[child]:
                        # update the list of child's value
                        # add the parent in the child's value list
                        self.connect(child, parent)

                # if the child doesn't exist in the dict
                else:
                    # create the child key with a empty list in the dict
                    # and append the parent in the list
                    self.connect(child, parent)

    def connect(self, A: str, B: str):
        """
        Create a key if not in the dict OR Update the list of the existing key's value
        
        :param A: key of the dict to be craeted or selected for update
        :param B: value to be inserted in the list of the key's value
        """
        self.graph_dict.setdefault(A, []).append(B)

    def get(self, a: str, b=None):
        """
        Class method to get the value of a key of the dict
        :param a: the key to get the value from it
        :returns: if key a not exists then returns empty dict or the a's values
        """
        links = self.graph_dict.setdefault(a, {})
        if b:
            return links.get(b)
        else:
            return links


def UndirectedGraph(graph_dict: dict = None) -> Graph:
    """
    Creating the undirected graph
    :param graph_dict: dictionary of the problem
    :returns: undirected representation of the graph as a Graph instance
    """
    return Graph(graph_dict=graph_dict, directed=False)


class Node:
    """
    Node class
    
    """

    def __init__(self, state: str, parent: Node = None, path_cost=0):
        """
        constructor of the Node class
        :param state: current state
        :param parent: previous node from which the current node is expanded, default None
         """
        self.state: str = state
        self.parent: Node = parent
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        """ Overrides the 'repr' method """
        return f"<Node {self.state}>"

    def __lt__(self, other):
        """Compares two nodes"""
        return self.state < other.state

    def expand(self, problem: GraphProblem) -> list[Node]:
        """
        Expand the current node or state
        :param problem: Problem instance
        :returns: the list of the child nodes 
         """
        return [self.child_node(action) for action in problem.actions(self.state)]

    def child_node(self, action: str) -> Node:
        """
        create a child node with the
        > state: child state
        > parent: current Node
        > and path cost to get to the child
        
        :param action: child state
        :returns: child Node instance
        
        """
        next_node = Node(action, self, problem.path_cost(self.path_cost, self.state, action))

        return next_node

    def path(self) -> list[Node]:
        """
        Gives the path from start to goal node
        """
        node: Node = self  # node: current Node
        path_back: list = list()  # path_back: empty list

        while node:
            # append the node in the path_back
            path_back.append(node)

            # now the current node is the parent of the current node
            node = node.parent

            # returns the reversed list of the path
        return path_back[::-1]


def print_path(path: list):
    """Print the path from start to goal"""
    [print(p.state, end=" => ") if i != len(path) - 1 else print(p.state) for i, p in enumerate(path)]


class PriorityQueue:
    def __init__(self, order='min', f=lambda x: x):
        """
        Constructor method of the priority queue. 
        returns minimum value if 'min' and max value if 'max' 
        priority depends on the function f
        """
        self.heap = []
        if order == 'min':
            self.f = f
        elif order == 'max':
            self.f = lambda x: -f(x)
        else:
            raise ValueError('Order must be min or max')

    def append(self, item):
        """Insert element in the priority queue"""
        heapq.heappush(self.heap, (self.f(item), item))

    def extend(self, items):
        """Extends list of elements in the priority queue"""
        for item in items:
            self.append(item)

    def pop(self):
        """Returns the most priority value and deleted it from the priority queue"""
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        """Return current capacity of priority queue."""
        return len(self.heap)

    def __contains__(self, key):
        """Return True if the key is in priority queue."""
        return any([item == key for _, item in self.heap])

    def __getitem__(self, key):
        """Returns the first value associated with key in priority queue.
        Raises KeyError if key is not present."""
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        """Delete the first occurrence of key."""
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)


def astar_search(problem):
    """
    A* Search using Graph Search
    :param problem: GraphProblem instance of the problem
    :returns: path of the start to goal or None at the failure to find the path
    """

    # evaluation function
    def f(n):
        return n.path_cost + problem.h(n.state)

    node = Node(problem.initial)  # initial node
    frontier = PriorityQueue('min', f)  # priority queue to store the nodes
    frontier.append(node)  # appending initial node
    explored = set()  # visited node set

    while frontier:
        node = frontier.pop()  # node with minimum g(n) + h(n)

        # checks if the current node is the goal or not
        if problem.goal_test(node.state):
            return node.path()

        # add the node to visited set
        explored.add(node.state)

        # expand the node 
        for child in node.expand(problem):

            # if the child is not in the priority queue and visited set
            # then add it in the priority queue
            if child.state not in explored and child not in frontier:
                frontier.append(child)

            # if the child in the priority queue
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)

    return None


if __name__ == '__main__':
    # directed graph
    problem_graph = Graph(dict(
        S=dict(F=3, B=1, A=2),
        A=dict(D=3, C=2),
        B=dict(E=4, D=2),
        C=dict(G=4),
        D=dict(G=4),
        F=dict(G=6)
    ))

    # adding the heuristics attribute to the problem graph instance
    problem_graph.heuristics = dict(
        S=6,
        A=4,
        B=5,
        C=2,
        D=2,
        E=8,
        F=4,
        G=0,
    )

    start = 'S'
    end = 'G'
    problem = GraphProblem(start, end, problem_graph)

    a_star_path = astar_search(problem)

    print("A* Search")
    print_path(a_star_path)
    print(f"Path Cost {a_star_path[-1].path_cost}")

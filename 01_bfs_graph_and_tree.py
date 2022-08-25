from __future__ import annotations
from abc import ABC, abstractmethod
from collections import deque


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

    def get(self, a: str):
        """
        Class method to get the value of a key of the dict

        :param a: the key to get the value from it
        :returns: if key a not exists then returns empty dict or the a's values
        """
        return self.graph_dict.setdefault(a, {})


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

    def __init__(self, state: str, parent: Node = None):
        """
        constructor of the Node class

        :param state: current state
        :param parent: previous node from which the current node is expanded, default None
         """
        self.state: str = state
        self.parent: Node = parent

    def __repr__(self):
        """ Overrides the 'repr' method """

        return f"<Node {self.state}>"

    def expand(self, problem: GraphProblem) -> list[Node]:
        """
        Expand the current node or state

        :param problem: Problem instance
        :returns: the list of the child nodes 
         """
        return [self.child_node(action) for action in problem.actions(self.state)]

    def child_node(self, action: str) -> Node:
        """
        Create child node instance
        
        :param action: child state
        :returns: child Node instance
         """

        # create a child node with the
        # state: child state
        # parent: current Node
        next_node = Node(action, self)

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


# bredth-first search: tree search algorithm
def bfs_tree(problem: GraphProblem, verbose: bool = False) -> list | None:
    """
    Breadth First Search using Tree Search. Does not Record the visited states

    :param problem: GraphProblem instance of the problem
    :param verbose: if true, printing the operation
    :returns: path of the start to goal or None at the failure to find the path
    """

    # queue
    frontier: deque = deque([Node(problem.initial)])

    s: str = ""
    while frontier:
        s += f"queue: {list(frontier)}\n"
        node: Node = frontier.popleft()  # current node selected from the queue
        s += f"Current State: {node.state}\n"
        s += f"After selecting {node} the queue is {list(frontier)}\n"

        # checks the node after it is expanded
        if problem.goal_test(node.state):
            if verbose:
                print(s)
            return node.path()

        # append all the children of the current node at the end of the queue
        s += f"Children of {node.state} : {node.expand(problem)}\n"
        frontier.extend(node.expand(problem))
        s += f"After inserting, queue: {list(frontier)}\n\n"

    # if the path is not found then returns None
    return None


# breadth-first serach graph search algorithm
def bfs_graph(problem: GraphProblem, verbose: bool = False) -> list | None:
    """
    Breadth First Search using Graph Search. Records the visited states

    :param problem: GraphProblem instance of the problem
    :param verbose: if true, printing the operation
    :returns: path of the start to goal or None at the failure to find the path
    """
    # initial node
    node: Node = Node(problem.initial)

    # checks if the initial state is the goal state
    if problem.goal_test(node.state):
        return node

    # queue
    frontier: deque = deque([node])

    # storing the visited nodes in a set
    explored: set = set()

    s: str = ""
    while frontier:
        s += f"queue: {list(frontier)}\n"
        node = frontier.popleft()  # select the first element from the queue
        s += f"Current State: {node.state}\n"
        s += f"After selecting {node} the queue is {list(frontier)}\n"
        explored.add(node.state)  # add the node to the visited set

        s += f"Children of {node.state} : {node.expand(problem)}\n"
        for child in node.expand(problem):
            # if the child not in explored and not in the queue 
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    if verbose:
                        print(s)
                    return child.path()
                frontier.append(child)
        s += f"After inserting, queue: {list(frontier)}\n\n"

    # if the path is not found then returns None
    return None


# print the path
def print_path(path: list):
    [print(p.state, end=" => ") if i != len(path) - 1 else print(p.state) for i, p in enumerate(path)]


if __name__ == "__main__":
    # data for the problem of travelling Romania
    romania_map_graph: dict['str', list['str', ...]] = dict(
        Arad=['Zerind', 'Sibiu', 'Timisoara'],
        Bucharest=["Urziceni", "Pitesti", "Giurgiu", "Fagaras"],
        Craiova=["Drobeta", "Rimnicu", "Pitesti"],
        Drobeta=["Mehadia"],
        Eforie=["Hirsova"],
        Fagaras=["Sibiu"],
        Hirsova=["Urziceni"],
        Iasi=["Vaslui", "Neamt"],
        Lugoj=["Timisoara", "Mehadia"],
        Oradea=["Zerind", "Sibiu"],
        Pitesti=["Rimnicu"],
        Rimnicu=["Sibiu"],
        Urziceni=["Vaslui"]
    )

    graph: Graph = UndirectedGraph(romania_map_graph.copy())

    romania_problem: GraphProblem = GraphProblem('Arad', 'Bucharest', graph)

    graph_search_path: list[Node] = bfs_graph(romania_problem)
    tree_search_path: list[Node] = bfs_tree(romania_problem)

    print("\n\nGraph Search")
    print_path(graph_search_path)

    print("\nTree Search")
    print_path(tree_search_path)

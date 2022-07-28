from abc import ABC, abstractmethod
from collections import deque


# Abstract class for a general problem
class Problem(ABC):
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal
        
    @abstractmethod
    def actions(self, state):
        pass
    
    @abstractmethod
    def result(self, state, action):
        pass
    
    def goal_test(self, state):
        """Test for the state is the goal state or not"""
        if isinstance(self.goal, list):
            return any(x is state for x in self.goal)
        else:
            return state == self.goal


# graph related problem
class GraphProblem(Problem):
    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph
        
    def actions(self, A):
        """neighbor or child of the parent"""
        return list(self.graph.get(A))
    
    def result(self, state, action):
        """The result just passes the action"""
        return action


# graph
class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            # make the graph undirected
            self.make_undirected()
            
    def make_undirected(self):
        for parent in list(self.graph_dict.keys()):    # keys of the graph dict
            for child in self.graph_dict[parent]:      # each value of the value list
                
                # if the value is in the dict i.e., update the list of the existing parents
                if child in self.graph_dict:
                    # update the list if the parent is not in it.
                    if parent not in self.graph_dict[child]:
                        self.connect(child, parent)
                
                # if the child in not in the dict
                else:
                    self.connect(child, parent)

    # connecting nodes        
    def connect(self, A, B):
        self.graph_dict.setdefault(A, []).append(B)
        
    # get the child of a parent
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        return links if b is None else links.get(b)
    
# making a graph undirected
def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)


# Node class 
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
    
    def __repr__(self):
        return f"<Node {self.state}>"
    
    def expand(self, problem):
        return [self.child_node(problem, action)
               for action in problem.actions(self.state)]
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node
    
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
            
        return path_back[::-1]


# breadth-first serach 
def bfs(problem):
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
                print(child)
    return None



if __name__ == "__main__":
    # data for the problem of travelling Romania
    romania_map_graph = dict(
        Arad = ['Zerind', 'Sibiu', 'Timisoara'],
        Bucharest = ["Urziceni", "Pitesti", "Giurgiu", "Fagaras"],
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

    graph = UndirectedGraph(romania_map_graph.copy())

    romania_problem = GraphProblem('Arad', 'Bucharest', graph)

    path = bfs(romania_problem)


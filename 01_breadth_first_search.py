from collections import deque
import numpy as np


# expanding the dict with state and parent adding to it
# to get the path
def expand(graph, A):
    return [{"state": action, "parent": A} for action in graph.get(A)]


# getting the path from start to goal
def path(start, child, paths):
    b,  path_back = child, [child['state']]

    while b['parent'] != start:
        for p in paths:
            if p['state'] == b['parent']:
                path_back.append(p['state'])
                b = p
                
    return [start] + list(reversed(path_back))


# make the graph undirected
def make_undirected_graph(graph_dict):
    graph = graph_dict
    
    for parent in list(graph_dict.keys()):
        for child in graph_dict[parent]:
            if child in graph:
                if parent not in graph[child]:
                    graph.setdefault(child, []).append(parent)
            else:
                graph.setdefault(child, []).append(parent)
                
    return graph
        


# breadth first search
def bfs(graph, start, goal):
    node = start
    
    if node == goal:
        return node
    
    frontier = deque([node])        # queue
    explored = set()                # visited states
    
    paths = []
    
    while frontier:
        node = frontier.popleft()
        explored.add(node)
        
        for child in expand(graph, node):                
            if child["state"] not in explored and child["state"] not in frontier:
                paths.append(child)
                
                if child["state"] == goal:
                    return path(start, child, paths) 
                
                frontier.append(child["state"])       
             
    return None

    


if __name__ == "__main__":

    romania_map_graph = make_undirected_graph(dict(
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
    ))


    start = 'Arad'
    end = 'Giurgiu'

    print(bfs(romania_map_graph, start, end))

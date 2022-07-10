from ai_classes.problem import GraphProblem
from ai_classes.graph import Graph, UndirectedGraph
from ai_classes.search import depth_first_search

if __name__ == "__main__":
    # data for the problem of travelling Romania
    romania_map_graph = dict(
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

    graph = UndirectedGraph(romania_map_graph.copy())

    romania_problem = GraphProblem('Arad', 'Zerind', graph)

    path = depth_first_search(romania_problem)

    print(path)
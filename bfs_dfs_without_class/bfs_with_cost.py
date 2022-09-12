graph_problem = dict(
    A = dict(F=5, C=7, B=13),
    B = dict(H=3, D=3),
    C = dict(G=5, E=1, D=5),
    D = dict(H=2),
    E = dict(G=4),
    F = dict(G=6, A=5)
)

def make_undirected(new_graph):
    graph = new_graph.copy()
    for parent, children in list(graph.items()):
        for child, path_cost in children.items():
            if child not in graph:
                graph.setdefault(child, dict()).setdefault(parent, path_cost)
            else:
                if parent not in children:
                    graph.setdefault(child, dict()).setdefault(parent, path_cost)
    
    return graph


print(make_undirected(graph_problem.copy()))



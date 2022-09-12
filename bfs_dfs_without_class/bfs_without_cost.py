from collections import deque

graph_problem = dict(
    A = ["F", "C", "B"],
    B = ["H", "D"],
    C = ["G", "E", "D"],
    D = ["H"],
    E = ["G"],
    F = ["G", "A"]
)


def make_undirected_graph(graph_dict):
    graph = graph_dict.copy()
    
    for parent in list(graph_dict.keys()):
        for child in graph_dict[parent]:
            if child not in graph:
                graph.setdefault(child, []).append(parent)
            else:
                if parent not in graph[child]:
                    graph.setdefault(child, []).append(parent)
                
    return graph


def expand(graph_dict: dict, A: str):
    return [{'state': action, 'parent': A} for action in graph_dict.get(A)]


def path(start, current_state, paths):
    c = current_state
    path_back = [current_state['state']]

    while c['parent'] != start:
        for p in paths:
            if p['state'] == c['parent']:
                path_back.append(p['state'])
                c = p

    return [start] + path_back[::-1]


def goal_test(A, B):
    return A == B


def bfs(graph, start, end):
    node = start

    if goal_test(node, end):
        return node

    frontier = deque([node])
    explored = set()

    paths = []

    while frontier:
        node = frontier.popleft()
        explored.add(node)

        for child in expand(graph, node):
            if child['state'] not in explored and child['state'] not in frontier:
                paths.append(child)

                if goal_test(child['state'], end):
                    return path(start, child, paths)

                frontier.append(child['state'])

    return None        

        
if __name__ == "__main__":
    graph = make_undirected_graph(graph_problem)

    start = 'E'
    goal = 'H'

    print(bfs(graph, start, goal))



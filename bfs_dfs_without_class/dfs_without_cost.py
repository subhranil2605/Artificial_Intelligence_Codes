from collections import deque


# make the graph undirected
def make_undirected(graph_dict: dict) -> dict:
    graph = graph_dict.copy()

    for parent in list(graph.keys()):
        for child in graph[parent]:
            if child not in graph:
                graph.setdefault(child, []).append(parent)
            else:
                if parent not in graph[child]:
                    graph.setdefault(child, []).append(parent)
                    
    return graph


# goal test
def goal_test(A, B):
    return A == B

    
# expand
def expand(graph_dict: dict, A: str):
    return [{'state': action, 'parent': A} for action in graph_dict.get(A)]


# path
def path(start: str, current_child: dict, paths: list) -> list:
    c = current_child
    path_back = [current_child['state']]

    while c['parent'] != start:
        for p in paths:
            if p['state'] == c['parent']:
                path_back.append(p['state'])
                c = p

    return [start] + path_back[::-1]


# dfs
def dfs(graph, start, end):
    node = {'state': start, 'parent': None}
    
    frontier = deque([node['state']])
    frontier_parent = deque([node['parent']])
    explored = set()
    paths = []

    while frontier:
        node = frontier.popleft()
        node_parent = frontier_parent.popleft()

        if goal_test(node, end):
            return path(start, {'state': node, 'parent': node_parent}, paths)

        explored.add(node)

        for child in expand(graph, node):
            if child['state'] not in explored and child['state'] not in frontier:
                paths.append(child)
                frontier.appendleft(child['state'])
                frontier_parent.appendleft(child['parent'])
                
    return None


if __name__ == "__main__":
    # graph problem provided
    graph_problem = dict(
        A = ["F", "C", "B"],
        B = ["H", "D"],
        C = ["G", "E", "D"],
        D = ["H"],
        E = ["G"],
        F = ["G", "A"]
    )

    # undirected instance of the graph
    graph = make_undirected(graph_problem)
    start, goal = 'E', 'H'

    dfs_path = dfs(graph, start, goal)
    print(dfs_path)

class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed

        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for parent in list(self.graph_dict.keys()):  # keys of the graph dict
            for child in self.graph_dict[parent]:  # each value of the value list

                # if the value is in the dict i.e., update the list of the existing parents
                if child in self.graph_dict:
                    # update the list if the parent is not in it.
                    if parent not in self.graph_dict[child]:
                        self.connect(child, parent)

                # if the child in not in the dict
                else:
                    self.connect(child, parent)

    def connect(self, A, B):
        self.graph_dict.setdefault(A, []).append(B)

    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        return links if b is None else links.get(b)


def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)

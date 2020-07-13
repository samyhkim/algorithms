# DFS + stack, node coloring
def is_bipartite(graph):
    seen = {}

    # we need to check every node bc it is possible that
    # graph[0] doesn't have any vertices connected
    for node in range(len(graph)):
        if node not in seen:
            if dfs(graph, seen, node, 1) == False:
                return False

    return True


def dfs(graph, seen, node, color):
    # node seen before in previous call stack, check its color
    if node in seen:
        if seen[node] != color:
            return False
        return True

    # node not seen before, add to seen with color
    seen[node] = color

    # get edges of node and check their color
    edges = graph[node]
    for edge in edges:
        if dfs(graph, seen, edge, -color) == False:
            return False

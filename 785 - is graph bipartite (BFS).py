# BFS + queue, node coloring
def is_partite(graph):
    seen = {}

    # we need to check every node bc it is possible that
    # graph[0] doesn't have any vertices connected
    for node in range(len(graph)):
        if node not in seen:
            if bfs(graph, seen, node) == False:
                return False

    return True


def bfs(graph, seen, start):
    queue = [(start, 1)]

    while queue:
        node, color = queue.pop(0)

        # node has been seen before, check its color
        if node in seen:
            if seen[node] != color:
                return False
            continue

        # node not seen before, add to seen with color
        seen[node] = color

        # get edges of node and add to queue
        edges = graph[node]
        for edge in edges:
            queue.append((edge, -color))

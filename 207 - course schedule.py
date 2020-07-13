def can_finish(num_courses, prerequisites):
    return topological_bfs(num_courses, prerequisites)


def topological_bfs(num_nodes, edges_list):
    adj_list = [[] for _ in range(num_nodes)]
    # c2 (course 2) is a prerequisite of c1 (course 1)
    # i.e c2c1 is a directed edge in the graph
    for c1, c2 in edges_list:
        adj_list[c2].append(c1)

    # 1. create list to store number of incoming edges of each vertex
    in_degrees = [0] * num_nodes
    for v1, v2 in edges_list:
        # v2v1 form a directed edge
        in_degrees[v1] += 1

    # 2. create a queue of all vertices with no incoming edge
    # at least one such node must exist in a non-empty acyclic graph
    # vertices in this queue have the same order as the eventual topo sort
    queue = []
    for vertex in range(num_nodes):
        if in_degrees[vertex] == 0:
            queue.append(vertex)

    count = 0  # intialize count of visited vertices
    topo_order = []  # will contain final topological order

    while queue:
        vertex = queue.pop(0)
        topo_order.append(vertex)
        count += 1

        # for each descendent of current vertex, reduce its in_degree by 1
        for descendant in adj_list[vertex]:
            in_degrees[descendant] -= 1
            if in_degrees[descendant] == 0:
                queue.append(descendant)

    if count != num_nodes:
        return None  # graph has at least one cycle
    else:
        return topo_order


print(can_finish(2, [[1, 0]]))

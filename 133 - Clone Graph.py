# DFS recurisve
def clone_graph(node):
    if not node:
        return

    node_copy = Node(node.val)
    lookup = {node: node_copy}
    dfs(node, lookup)
    return node_copy


def dfs(node, lookup):
    for neighbor in node.neighbors:
        if neighbor not in lookup:
            neighbor_copy = Node(neighbor.val)
            lookup[neighbor] = neighbor_copy
            lookup[node].neighbors.append(neighbor_copy)
            dfs(neighbor, lookup)
        else:
            lookup[node].neighbors.append(lookup[neighbor])


# BFS
def clone_graph3(node):
    if not node:
        return
    node_copy = Node(node.val)
    lookup = {node: node_copy}

    queue = [node]
    while queue:
        node = queue.pop(0)
        for neighbor in node.neighbors:
            if neighbor not in lookup:  # neighbor is not visited
                neighbor_copy = Node(neighbor.val)
                lookup[neighbor] = neighbor_copy
                lookup[node].neighbors.append(neighbor_copy)
                queue.append(neighbor)
            else:
                lookup[node].neighbors.append(lookup[neighbor])

    return node_copy

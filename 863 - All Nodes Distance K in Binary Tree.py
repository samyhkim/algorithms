'''
If we view the tree structure as the graph, then it is easy to come up the BFS solution to find the nodes that are located at a certain distance from the target node.

What is missing in the original tree data structure that makes the above idea a bit tricky to implement is the explicit pointer to a node's parent which is the neighbor for a node, the same as its children nodes.

Due to this missing pointer, there is no explicit way for a node to reach out directly its neighbor nodes that is connected through the parent node.

So the solution becomes clear, let's construct a graph from a given tree structure. One could have two slightly different approaches.

construct an adjacent list, where each entry consists of key:list, where key is the node itself, and the list contains its neighbors.

construct a map that maps each node to its parent. One could use less space in this case, since we do not store the child nodes as opposed to the above option.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_graph(node, parent, graph):
    if node is None:
        return

    if parent is not None:
        if node not in graph:
            graph[node] = [parent]
        else:
            graph[node].append(parent)

    if node.left is not None:
        if node not in graph:
            graph[node] = [node.left]
        else:
            graph[node].append(node.left)
        build_graph(node.left, node, graph)

    if node.right is not None:
        if node not in graph:
            graph[node] = [node.right]
        else:
            graph[node].append(node.right)
        build_graph(node.right, node, graph)


def distance_K(root, target, K):
    k_distance_nodes = []
    visited = set()
    graph = {}  # adjacent list; vertex: [parent, left, right]

    build_graph(root, None, graph)  # DFS to build graph

    # BFS to retrieve the nodes with given distance
    # starting from the target node
    queue = [(target, 0)]

    while queue:
        node, distance = queue.pop(0)

        if node in visited:
            continue
        visited.add(node)

        if distance == K:
            k_distance_nodes.append(node.val)
        elif distance < K:
            if node in graph:  # for error handling 2nd test case
                for child in graph[node]:  # all nodes in layer
                    queue.append((child, distance + 1))

    return k_distance_nodes


# root = Node(3)
# root.left = Node(5)
# root.right = Node(1)
# root.left.left = Node(6)
# root.left.right = Node(2)
# root.left.right.left = Node(7)
# root.left.right.right = Node(4)
# root.right.left = Node(0)
# root.right.right = Node(8)

# print(distance_K(root, root.left, 2))

root = Node(1)
print(distance_K(root, root, 3))

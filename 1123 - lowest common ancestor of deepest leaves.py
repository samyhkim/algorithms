class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca_deepest_leaves(root):
    lca = lca_helper(root)
    return lca[0]


def lca_helper(node):
    if node is None:
        return [None, 0]

    # traverse all the way down to find deepest node
    left_node, left_depth = lca_helper(node.left)
    right_node, right_depth = lca_helper(node.right)
    max_depth = max(left_depth, right_depth)

    # pass through node with deepest depth through call stack
    if left_depth > right_depth:
        return [left_node, max_depth + 1]
    elif left_depth < right_depth:
        return [right_node, max_depth + 1]
    else:  # both depths are equal
        # current node is ancestor of both left and right nodes
        return [node, max_depth + 1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(lca_deepest_leaves(root))

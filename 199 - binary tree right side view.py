'''
res = [root.val]
while root is not None:
    if node.right is not None:
        res.append(node.right.val)
        node = node.right
    else:
        if node.left is not None:
            res.append(node.left.val)
        node = node.left
return res
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_side_view(root):
    rights = []  # return list of node vals
    queue = [(root, 0)]  # track node's level

    while queue:
        node, level = queue.pop(0)
        if node:  # eliminates None values
            # ensures addition of one node per level
            if len(rights) == level:
                rights.append(node.val)

        # always give priority to right node
        queue.append(node.right, level + 1)
        queue.append(node.left, level + 1)

    return rights


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(right_side_view(root))

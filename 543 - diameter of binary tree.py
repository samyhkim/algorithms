def diameter_of_binary_tree(root):
    diameter = [0]
    depth(root, diameter)
    return diameter[0]


def depth(root, diameter):
    if not root:
        return 0
    left_height = depth(root.left, diameter)
    right_height = depth(root.right, diameter)
    diameter[0] = max(diameter[0], left_height + right_height)
    return 1 + max(left_height, right_height)

def closest_value(root, target):
    closest_node = root.val

    while root:
        if abs(root.val - target) < abs(closest_node - target):
            closest_node = root

        if target < root:
            root = root.left
        else:
            root = root.right

    return closest_node

def level_order(root):
    if not root:
        return

    levels = []
    queue = [root]

    while queue:
        curr_nodes = []
        next_level = []

        for node in queue:
            curr_nodes.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        levels.append(curr_nodes)
        queue = next_level

    return levels

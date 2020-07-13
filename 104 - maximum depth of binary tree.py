# recursive
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# iterative
def max_depth2(root):
    if not root:
        return 0

    depth = 0
    queue = [root]

    while queue:
        depth += 1

        for node in range(len(queue)):
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth

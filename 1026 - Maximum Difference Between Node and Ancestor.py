def max_ancestor_diff(root):
    if not root:
        return
    return helper(root, root.val, root.val)


def helper(node, high, low):
    if not node:
        return high - low

    # collect highest and lowest nodes as we move down the tree
    # so when we reach the end of a path, we will always have the
    # maximum difference this path could have made
    high = max(high, node.val)
    low = min(low, node.val)

    return max(helper(node.left, high, low), helper(node.right, high, low))

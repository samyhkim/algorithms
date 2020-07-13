def lowest_common_ancestor(root, p, q):
    if root == p or root == q:
        return root

    left = None
    right = None

    if root.left:
        left = lowest_common_ancestor(root.left, p, q)
    if root.right:
        right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right

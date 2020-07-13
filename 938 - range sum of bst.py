class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
Approach:
BST always has lesser nodes in left subtree and greater nodes in right subtree.
If node is less than L, we would never check even lower.
    But we can check its right subtree for more greater nodes.
If node is greater than R, we would never check even higher.
    But we can check its left subtree for more lesser nodes.
When our node can't go left/right and has received a value from its right/left
call stack, then check if itself is between L and R. If so, add it to sum.

O(n), O(h)
'''


def range_sum_BST(root, L, R):
    if root is None:
        return 0

    sum = 0

    # greater than lower bound, go lower until val is lower than L
    # then check if any nodes in right subtree are valid
    if root.val > L:
        sum += range_sum_BST(root.left, L, R)

    # lower than upper bound, go higher until val is greater than R
    # then check if any nodes in left subtree are valid
    if root.val < R:
        sum += range_sum_BST(root.right, L, R)

    if L <= root.val <= R:
        sum += root.val

    return sum


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

print(range_sum_BST(root, 7, 15))

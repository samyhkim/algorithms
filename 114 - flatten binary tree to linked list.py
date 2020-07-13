'''
1. flatten left subtree
2. find left subtree's tail
3. set root's left to None, root's right to root'left, tail's right to root.right
4. flatten the original right subtree
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def flatten(root):
    # escape condition
    if not root:
        return
    right = root.right
    if root.left:
        # flatten left subtree
        flatten(root.left)
        # find the tail of left subtree
        tail = root.left
        while tail.right:
            tail = tail.right
        # left <-- None, right <-- left, tail's right <- right
        root.left, root.right, tail.right = None, root.right, right
    # flatten right subtree
    flatten(right)

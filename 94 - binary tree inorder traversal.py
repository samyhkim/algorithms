class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# iterative


def inorderTraversal(root):
    res = []
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res


root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print(inorderTraversal(root1))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# recursive


def is_valid_BST(root):
    return check_BST(root, float("-inf"), float("inf"))


def check_BST(node, left, right):
    if node is None:
        return True
    if not left < node.val < right:
        return False
    return check_BST(node.left, left, node.val) and check_BST(node.right, node.val, right)

# iterative


# def is_valid_BST(root):
#     if root is None:
#         return None
#     node = root
#     stack = []
#     prev = None
#     while stack or node:
#         while node:
#             stack.append(node)
#             node = node.left
#         node = stack.pop()
#         if prev is not None and node.value <= prev.value:
#             return False
#         prev = node
#         node = node.right
#     return True

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(is_valid_BST(root))

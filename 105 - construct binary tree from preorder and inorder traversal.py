'''
pop preorder[0] and find its index position in inorder
assign found node as root
root.left = buildTree(preorder, inorder[:index])
root.right = buildTree(preorder, inorder[index+1:])
keep going until inorder is empty
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = buildTree(preorder, inorder[:index])
        root.right = buildTree(preorder, inorder[index + 1:])
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

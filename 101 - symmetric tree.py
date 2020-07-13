'''
the trickiest part is the last return statement:
check_symmetric(left.left, right.right) and check_symmetric(left.right, right.left)
remember to check outsides together and insides together
'''


def isSymmetric(root):
    if root is None:
        return True
    return check_symmetric(root.left, root.right)


def check_symmetric(left, right):
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    return left.val == right.val and check_symmetric(left.left, right.right) and check_symmetric(left.right, right.left)

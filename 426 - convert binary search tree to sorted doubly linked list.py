def tree_to_doubly_list(root):
    if not root:
        return
    stack = []
    dummy = prev = Node(0)
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        node.left = prev  # assign curr left to last node
        prev.right = node  # assign last node's right to curr node
        prev = node  # save curr node
        node = node.right  # move onto next node
    dummy.right.left = prev
    prev.right = dummy.right
    return dummy.right

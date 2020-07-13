def zigzag_level_order(root):
        if root is None:
        return None
    res = []
    level = [root]
    zigzag = False
    while level:
        currentNodes = []
        nextLevel = []
        for node in level:
            currentNodes.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        if zigzag == True:
            currentNodes.reverse()
            zigzag = False
        else:
            zigzag = True
        res.append(currentNodes)
        level = nextLevel
    return res

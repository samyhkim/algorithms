class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        '''
        return a boolean, whether we have a next smallest number
        '''
        return len(self.stack) > 0

    def next(self):
        '''
        return an integer, the next smallest number
        '''
        node = self.stack.pop()
        next = node.right
        while next:
            self.stack.append(next)
            next = next.left
        return node.val

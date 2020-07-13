class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        '''
        Encodes a tree to a single string.
        '''
        if not root:
            return ""

        # approaching encoded as an empty string will return -101 for test
        # case ['-1', '0', '1'] which will return ['-', '1', '0', '1'] later
        # in deserialize() when running "nodes = list(data)"
        encoded = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                encoded.append(str(node.val))
            else:
                encoded.append("#")

        return ",".join(encoded)

    def deserialize(self, data):
        '''
        Decodes your encoded data to a tree.
        '''
        if not data:
            return None

        # using list(data) will return ['-', '1', '0', '1']
        # for test case ['-1', '0', '1']
        nodes = data.split(",")
        root = Node(int(nodes[0]))
        queue = [root]

        # every odd index is a left node
        # every even index is a right node
        index = 1
        while queue:
            node = queue.pop(0)

            if nodes[index] is not "#":
                node.left = Node(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not "#":
                node.right = Node(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(4)
# root.right.right = Node(5)

root = Node(-1)
root.left = Node(0)
root.right = Node(1)

codec = Codec()
encoded = codec.serialize(root)
decoded = codec.deserialize(encoded)

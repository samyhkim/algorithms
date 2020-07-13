'''
Same as "987 - Vertical Order Traversal of a Binary Tree" except
don't sort at the end.

Difference:
314. If two nodes are in the same row and column, the order
should be from left to right.
987. If two nodes have the same position, then the value of
the node that is reported first is the value that is smaller.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def vertical_traversal(root):
    verticals = {}  # return list of node vals grouped by x-coord
    queue = [(root, 0)]  # track node's x-coord

    while queue:
        temp = {}

        # collect current level's nodes and their placements
        for node in range(len(queue)):
            node, x_coord = queue.pop(0)
            if node:  # eliminates None values
                if x_coord not in temp:
                    temp[x_coord] = [node.val]
                else:
                    temp[x_coord].append(node.val)

                # get nodes in next level of tree
                queue.append([node.left, x_coord - 1])
                queue.append([node.right, x_coord + 1])

        # dump current level's nodes and their placements into verticals
        for x_coord in temp:
            if x_coord not in verticals:
                verticals[x_coord] = temp[x_coord]
            else:
                # append will return [1, [5, 6]]
                # extend will return [1, 5, 6]
                verticals[x_coord].extend(temp[x_coord])

    # sort by placements and return their nodes
    return [verticals[x_coord] for x_coord in sorted(verticals)]


# root = Node(3)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(vertical_traversal(root))

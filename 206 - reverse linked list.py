class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseList(head):
    new = None
    curr = head
    while curr:
        next = curr.next  # saves curr's next position
        curr.next = new  # assign's curr's position to new
        new = curr  # new takes curr's old spot for next curr add
        curr = next  # curr takes next's saved position
    return new


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

reverseList(head)

# Singly linked list node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Iteratively
def merge_two_lists(l1, l2):
    l3 = curr = Node(0)

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2

    return l3.next

# Recursively
# def merge_two_lists(l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     if l1.val < l2.val:
#         l1.next = mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = mergeTwoLists(l1, l2.next)
#         return l2


l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(4)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)

merge_two_lists(l1, l2)

# Singly linked list node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# One-pass
def remove_nth_node_from_end(head, n):
    dummy = fast = slow = Node(0)
    dummy.next = head

    # iterate fast n times forward
    for _ in range(n):
        fast = fast.next

    # fast will stop when its curr/next pointer is None
    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


# # Standard
# def removeNthNodeFromEnd(head, n):
#     '''
#     Given linked list: 1->2->3->4->5, and n = 2.
#     while head:
#         count += 1
#     while curr < count:
#         curr = curr.next
#     '''
#     dummy = curr = Node(0)
#     dummy.next = curr.next = head
#     list_len = 0
#     count = 0
#     while head:
#         list_len += 1
#         head = head.next
#     while count < list_len-n-1:
#         count += 1
#         curr = curr.next
#     curr.next = curr.next.next
#     return dummy.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

removeNthNodeFromEnd(head, 2)

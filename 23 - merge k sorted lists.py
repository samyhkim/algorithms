import heapq


# Singly linked list node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# modified merge sort
def merge_k_lists(lists):
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    l = merge_k_lists(lists[:mid])
    r = merge_k_lists(lists[mid:])
    return merge(l, r)


def merge(l, r):
    dummy = cur = Node(0)
    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next
        else:
            cur.next = r
            r = r.next
        cur = cur.next
    cur.next = l or r
    return dummy.next


# heap
# def merge_k_lists(lists):
#     min_heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
#     dummy = Node(0)
#     curr = dummy
#     while min_heap:
#         val, i, node = min_heap[0]
#         if not node.next:  # exhausted one linked-list
#             heapq.heappop(min_heap)
#         else:
#             # recycling tie-breaker i guarantees uniqueness
#             heapq.heappush(min_heap, (node.next.val, i, node.next))
#             heapq.heappop(min_heap)
#         curr.next = node
#         curr = curr.next
    # return dummy.next


l1 = Node(1)
l1.next = Node(4)
l1.next.next = Node(5)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)

l3 = Node(2)
l3.next = Node(6)

lists = [l1, l2, l3]

print(merge_k_lists(lists))

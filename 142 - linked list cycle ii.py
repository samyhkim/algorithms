def detect_cycle(head):
    slow = fast = head
    while True:
        if fast is None or fast.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    while head != slow:
        head = head.next
        slow = slow.next
    return head

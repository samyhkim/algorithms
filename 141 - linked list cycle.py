def has_cycle(head):
    if not head:
        return False
    slow = fast = head
    fast = fast.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

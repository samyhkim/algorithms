# singly linked list
class Node:
    def __init(self, val):
        self.val = val
        self.next = None


'''
Requires extraction of sum's ones digit and tens digit:
ones = sum % 10
tens = sum // 10

Keep in mind of test case:
l1 = [5]
l2 = [5]
This case requires sum to be included in while condition
bc after the first iteration, l1 and l2 are empty, but sum == 1
'''


def add_two_numbers(l1, l2):
    dummy = curr = Node(0)
    sum = 0
    while l1 or l2 or sum:
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        curr.next = Node(sum % 10)  # ones digit
        sum //= 10  # tens digit, carry over
        curr = curr.next
    return dummy.next

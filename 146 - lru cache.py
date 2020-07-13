class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_from_tail(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def bring_to_front(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.append_to_front(node)

    def append_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.prev.next = node
        node.next.prev = node


class LRUCache:
    def __init__(self, capacity):
        self.size = 0
        self.max_size = capacity
        self.lookup = {}
        self.linked_list = LinkedList()

    def get(self, key):
        if key in self.lookup:
            self.linked_list.bring_to_front(self.lookup[key])
            return self.lookup[key].value
        else:
            return -1

    def put(self, key, value):
        if key in self.lookup:
            node = self.lookup[key]
            node.value = value
            self.linked_list.bring_to_front(node)
        else:
            if self.size == self.max_size:
                self.lookup.pop(self.linked_list.tail.prev.key)
                self.linked_list.remove_from_tail()
            else:
                self.size += 1
            node = Node(key, value)
            self.lookup[key] = node
            self.linked_list.append_to_front(node)

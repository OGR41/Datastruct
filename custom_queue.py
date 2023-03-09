

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data=None):
        if self.head is None:
            self.head = Node(data, self.tail)
        self.head = Node(self.head.data, self.tail)
        self.tail = Node(data)

    def dequeue(self):
        if self.head is None:
            return None
        dequeue_element = self.head
        self.head = self.head.next_node
        return dequeue_element.data

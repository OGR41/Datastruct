

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
            new_node = Node(data, self.tail)
            self.head = new_node
        self.head = Node(self.head.data, self.tail)
        new_node = Node(data)
        self.tail = new_node


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')

print(queue.head.data)
print(queue.head.next_node.data)
print(queue.tail.data)
print(queue.tail.next_node)
print(queue.tail.next_node.data)

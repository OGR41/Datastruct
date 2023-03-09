

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = Node(data)
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.tail is None:
            self.tail = Node(data)
            self.head = Node(data)
        elif self.head.data == self.tail.data:
            self.tail = Node(data)
            self.head.next_node = self.tail
        else:
            self.tail = Node(data)
            self.head.next_node.next_node = self.tail

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)


ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()

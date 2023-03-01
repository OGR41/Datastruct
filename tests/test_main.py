import unittest
from main import Node, Stack
from custom_queue import Queue


class TestMain(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1, None)
        self.n2 = Node(2, self.n1)
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')

    def test_push_pop(self):
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node, None)
        self.assertEqual(self.n1.data, 1)
        self.assertEqual(self.n1.next_node, None)
        self.assertEqual(self.n2.data, 2)
        self.assertEqual(self.n2.next_node, self.n1)
        self.stack.pop()
        self.assertEqual(self.stack.top.data, 'data1')


class TestCustomqueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_enqueue(self):
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)


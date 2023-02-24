import unittest
from main import Node, Stack


class TestMain(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1, None)
        self.n2 = Node(2, self.n1)
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')

    def test_push(self):
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node, None)
        self.assertEqual(self.n1.data, 1)
        self.assertEqual(self.n1.next_node, None)
        self.assertEqual(self.n2.data, 2)
        self.assertEqual(self.n2.next_node, self.n1)

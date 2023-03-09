import unittest
from custom_queue import Queue


class TestCustomQueue(unittest.TestCase):
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

    def test_dequeue(self):
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.queue.dequeue()
        self.assertEqual(self.queue.head.data, 'data2')
        self.assertEqual(self.queue.head.next_node, None)
        self.queue.dequeue()
        self.assertEqual(self.queue.head, None)

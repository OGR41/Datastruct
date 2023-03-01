

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data=None):
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        remove = self.top
        self.top = self.top.next_node
        return remove.data


# def main():
#     stack = Stack()
#     stack.push('data1')
#     data = stack.pop()
#     print(stack.top)
#     print(data)
#     stack = Stack()
#     stack.push('data1')
#     stack.push('data2')
#     data = stack.pop()
#     print(stack.top.data)
#     print(data)
#
#
# if __name__ == '__main__':
#     main()

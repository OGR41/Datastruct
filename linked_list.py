

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    linked_list = []
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = Node(data)
            self.linked_list.insert(0, self.head.data)
        else:
            self.head = Node(data, self.head)
            self.linked_list.insert(0, self.head.data)

    def insert_at_end(self, data):
        if self.tail is None:
            self.tail = Node(data)
            self.head = Node(data)
            self.linked_list.append(self.tail.data)
        elif self.head.data == self.tail.data:
            self.tail = Node(data)
            self.head.next_node = self.tail
            self.linked_list.append(self.tail.data)
        else:
            self.tail = Node(data)
            self.head.next_node.next_node = self.tail
            self.linked_list.append(self.tail.data)

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

    def to_list(self):
        return self.linked_list

    def get_data_by_id(self, id):
        Except.except_get_data_by_id(id)
        for i in self.linked_list:
            if type(i) is dict:
                if i['id'] == id:
                    return i


class Except(Exception):
    def except_get_data_by_id(self):
        for i in LinkedList.linked_list:
            try:
                if type(i) is not dict:
                    raise TypeError
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')


# ll = LinkedList()
# ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
# ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
# ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
# ll.insert_beginning({'id': 0, 'username': 'serebro'})
# lst = ll.to_list()
# for item in lst:
#     print(item)
# user_data = ll.get_data_by_id(3)
# print(user_data)

#
# ll = LinkedList()
# ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
# ll.insert_at_end('idusername')
# ll.insert_at_end([1, 2, 3])
# ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
# user_data = ll.get_data_by_id(2)
# print(user_data)

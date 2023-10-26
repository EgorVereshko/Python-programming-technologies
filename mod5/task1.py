class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

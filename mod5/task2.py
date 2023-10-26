class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeued_node = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            dequeued_node.next = None
            return dequeued_node.data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def print_queue(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

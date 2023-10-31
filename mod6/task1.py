class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None

    def remove(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None or current.next is None:
                    return
                current.next = current.next
            if current.next is None:
                return
            current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(n - 1):
                if current is None:
                    return
                current = current.next
            if current is None:
                return
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


my_list = LinkedList()

my_list.push(1)
my_list.push(2)
my_list.push(3)
print(my_list.get(0))
print(my_list.get(2))

my_list.remove(1)
print(my_list.get(1))

my_list.insert(1, 4)
print(my_list.get(1))

for item in my_list:
    print(item)

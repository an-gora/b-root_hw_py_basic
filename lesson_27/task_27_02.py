class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        cur_node = self.head
        if self.is_empty():
            print("Stack Underflow")
        else:
            while cur_node is not None:
                print(cur_node.data, "->", end=" ")
                cur_node = cur_node.next
            return


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.display()

print("\nTop element is ", my_stack.peek())

my_stack.pop()
my_stack.pop()

my_stack.display()

print("\nTop element is ", my_stack.peek())

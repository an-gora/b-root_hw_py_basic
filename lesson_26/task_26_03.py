class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if len(self._items) == 0:
            return None
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def reverse(self, string_to_reverse:str):
        n = len(string_to_reverse)
        reversed_string = ''
        for i in range(0, n):
            self._items.append(string_to_reverse[i])
        for i in range(0, n):
            reversed_string += self._items.pop()
        return reversed_string

    def get_from_stack(self, element):
        if element in self._items:
            self._items.remove(element)
        else:
            raise ValueError(f'{element} is not found')


s= Stack()
s.push(1)
s.push(3)
s.push(5)
s.push(8)
print(s)
s.get_from_stack(3)
print(s)








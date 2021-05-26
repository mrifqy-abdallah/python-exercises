class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._current = None
        self._size = 0

        for v in values:
            self.push(v)

    def __len__(self):
        return self._size

    def __iter__(self):
        return self

    def __next__(self):
        if self._current is None:
            self._current = self._head  # Reset _current
            raise StopIteration
        val = self._current._value
        self._current = self._current._next
        return val

    def head(self):
        if self._size == 0:
            raise EmptyListException("Linked List is empty.")
        return self._head

    def push(self, value):
        prev = self._head
        self._head = Node(value)
        self._head._next = prev
        self._current = self._head
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise EmptyListException("Linked List is empty.")
        val = self._head._value
        self._head = self._head._next
        self._current = self._head
        self._size -= 1
        return val

    def reversed(self):
        return reversed([s for s in self])


class EmptyListException(Exception):
    pass

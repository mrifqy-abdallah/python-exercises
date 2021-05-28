class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self._value = value
        self._succeeding = succeeding
        self._previous = previous


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        if self._head is None:
            print("Linked List is empty.")
            return
        node = self._head
        while node is not None:
            yield node._value
            node = node._succeeding

    def push(self, value):
        self._size += 1

        if self._head is None:
            self._head = Node(value)
            self._tail = self._head
            return

        new_node = Node(value, None, self._tail)
        self._tail._succeeding = new_node
        self._tail = new_node

    def pop(self):
        if self._head is None:
            raise EmptyListException("Cannot pop from empty Linked List.")

        self._size -= 1
        tail = self._tail._value

        if self._head == self._tail:
            self._head, self._tail = None, None
            return tail

        self._tail = self._tail._previous
        self._tail._succeeding = None
        return tail

    def shift(self, ):
        if self._head is None:
            raise EmptyListException("Cannot shift from empty Linked List.")

        self._size -= 1
        head = self._head._value

        if self._head == self._tail:
            self._head, self._tail = None, None
            return head
        
        self._head = self._head._succeeding
        self._head._previous = None
        return head


    def unshift(self, value):
        if self._head is None:
            # If Linked list is empty, unshift is no different than push
            self.push(value)
        else:
            self._size += 1
            new_node = Node(value, self._head, None)
            self._head._previous = new_node
            self._head = new_node

        


class EmptyListException(Exception):
    pass
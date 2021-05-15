from collections import deque


class BufferFullException(Exception):
    def __init__(message: str):
        super().__init__("Buffer is Full.")


class BufferEmptyException(Exception):
    def __init__(message: str):
        super().__init__("Buffer is Empty.")


class CircularBuffer:
    def __init__(self, capacity: int):
        self.buffer = deque(maxlen=capacity)

    def read(self):
        # Read the oldest value in self.buffer. If it has no value, raise exception.
        if self.buffer:
            return self.buffer.popleft()
        raise BufferEmptyException()

    def write(self, data: str):
        # Write new value to self.buffer if it still has free capacity, otherwise raise exception
        if len(self.buffer) < self.buffer.maxlen:
            self.buffer.append(data)
            return
        raise BufferFullException()

    def overwrite(self, data: str):
        # Write new value to self.buffer
        # If it's full already, the oldest value will be deleted first
        if len(self.buffer) == self.buffer.maxlen:
            self.buffer.popleft()
        self.buffer.append(data)
        return

    def clear(self):
        return self.buffer.clear()

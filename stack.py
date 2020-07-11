class Stack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            raise RuntimeError("pop from empty stack")

    def peek(self):
        try:
            return self._data[-1]
        except IndexError:
            raise RuntimeError("cannot peek an empty stack")

    def __len__(self):
        return len(self._data)

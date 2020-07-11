import heapq


class Heap:

    def __init__(self, initial_data=None):
        if initial_data is not None:
            self._data = initial_data
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, item)

    def pop(self):
        try:
            return heapq.heappop(self._data)
        except IndexError:
            raise IndexError("pop from empty heap")

    def peek(self):
        try:
            return self._data[0]
        except IndexError:
            raise IndexError("peek into empty heap")

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    heap = Heap([1, 3, 0, -1])
    heap.push(5)
    heap.push(2)
    heap.push(0)
    heap.push(3)

    for _ in range(len(heap)):
        print(heap.pop())

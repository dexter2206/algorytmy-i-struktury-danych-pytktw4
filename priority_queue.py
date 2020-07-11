from heap import Heap


class PriorityQueue:

    def __init__(self):
        self._heap = Heap()
        self._counter = 0

    def put(self, item, priority=0):
        self._heap.push((priority, self._counter, item))
        self._counter += 1

    def get(self):
        if len(self._heap) == 0:
            raise IndexError("Cannot get item from an empty queue.")
        _, _, item = self._heap.pop()
        return item

    def __len__(self):
        return len(self._heap)


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.put("Task 1")
    pq.put("High priority task", priority=-1)
    pq.put("Perform code review", -1)
    pq.put({"source": "192.168.1.1", "dest": "8.8.8.8"}, priority=1)
    pq.put({"source": "192.168.1.1", "dest": "8.8.8.8"}, priority=0)

    while len(pq) > 0:
        print(pq.get())

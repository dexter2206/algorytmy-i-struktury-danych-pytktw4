import heapq


if __name__ == '__main__':
    numbers = [1, 2, -1, 0, 4, 6, 3]
    heapq.heapify(numbers)
    print(numbers)
    print(heapq.heappop(numbers))
    print(numbers)
    heapq.heappush(numbers, 0.5)
    print(numbers)


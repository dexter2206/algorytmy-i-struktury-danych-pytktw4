def partition(items):
    pivot = items[-1]
    left = 0
    right = len(items) - 2

    while left < right:
        while left < right and items[left] <= pivot:
            left += 1

        while right > left and items[right] >= pivot:
            right -= 1

        items[left], items[right] = items[right], items[left]

    items[right], items[-1] = items[-1], items[right]
    return right

if __name__ == '__main__':
    items = [3, 1, 0, 4, 2, -1, 5, 2]
    print(partition(items))
    print(items)


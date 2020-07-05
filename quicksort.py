def partition(items):
    pivot = items[-1]
    left = 0
    right = len(items) - 1

    while left < right:
        while left < right and items[left] <= pivot:
            left += 1

        while right > left and items[right] >= pivot:
            right -= 1

        if left < right:
            items[left], items[right] = items[right], items[left]


    items[left], items[-1] = items[-1], items[left]
    return left


def quicksort(items):
    if len(items) < 2:
        return items
    split = partition(items)
    return quicksort(items[:split]) + [items[split]] + quicksort(items[split+1:])


if __name__ == '__main__':
    items = [3, 1, 0, 4, 2, -1, 5, 1]
    print(quicksort(items))



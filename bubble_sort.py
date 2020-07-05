def bubble_sort(items):
    items = list(items)

    for i in range(len(items) - 1, 0, -1):
        for j in range(0, i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    return items

if __name__ == '__main__':
    print(bubble_sort([7, 3, 1, 4, 0, 2, 5]))

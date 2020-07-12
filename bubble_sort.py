def bubble_sort(items, key=None, reversed=False):
    items = list(items)

    if key is not None:
        keys = [key(item) for item in items]
    else:
        keys = list(items)

    for i in range(len(items) - 1, 0, -1):
        for j in range(0, i):
            if keys[j] > keys[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                keys[j], keys[j + 1] = keys[j + 1], keys[j]
    if reversed:
        items = items[::-1]
    return items

if __name__ == '__main__':
    print(bubble_sort([7, 3, 1, 4, 0, 2, 5], reversed=True))
    #print(bubble_sort(["z", "abc", "foo", "pl"]))
    #print(bubble_sort(["z", "abc", "foo", "pl"], key=len))

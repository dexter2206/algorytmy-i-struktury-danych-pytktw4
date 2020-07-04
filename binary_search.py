def binary_search(sequence, x):
    left, right = 0, len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] == x:
            return mid
        elif sequence[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    raise ValueError(f"Element {x} not in sequence.")


def _binary_search_rec(sequence, x, left, right):
    if left > right:
        raise ValueError(f"Element {x} not in sequence")

    mid = (left + right) // 2
    if sequence[mid] == x:
        return mid
    elif sequence[mid] > x:
        right = mid - 1
    else:
        left = mid + 1

    return _binary_search_rec(sequence, x, left, right)


def binary_search_rec(sequence, x):
    return _binary_search_rec(sequence, x, 0, len(sequence) - 1)


if __name__ == '__main__':
    print(binary_search_rec([1, 3, 7, 9, 10, 20], 20))

    try:
        binary_search_rec([1, 3, 4, 5, 7, 8, 9, 30], 10)
    except ValueError as err:
        print(err)

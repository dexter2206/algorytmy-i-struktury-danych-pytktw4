def merge(first, second):
    i = j = 0
    merged = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1
    while i < len(first):
        merged.append(first[i])
        i += 1
    while j < len(second):
        merged.append(second[j])
        j += 1
    return merged


if __name__ == '__main__':
    print(merge([-1, 0, 3, 4], [-2, 1, 2, 3.5]))

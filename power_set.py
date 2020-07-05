from typing import Any, List, Iterable, Set


def power_set(collection: Iterable[Any]) -> List[Set[Any]]:
    it = iter(collection)
    try:
        x = next(it)
    except StopIteration:
        return [set()]
    result = []
    for small_set in power_set(it):
        result.append(small_set)
        result.append(small_set.union({x}))
    return result


if __name__ == '__main__':
    print(power_set({1, 2, 3}))


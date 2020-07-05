from bubble_sort import bubble_sort

my_sort = bubble_sort

def test_sorts_permuted_sequence():
    items = [2, 1, 5, 0, -1]
    assert my_sort(items) == [-1, 0, 1, 2, 5]


def test_leaves_original_sequence_unchanged():
    items = [3, 1, 5, 0, 2, 1, 6]
    old_items = list(items)
    my_sort(items)
    assert items == old_items


def test_sorted_sequence_remains_sorted():
    items = [1, 3, 5, 7, 10, 11]
    assert my_sort(items) == items


def test_sorts_sequence_sorted_in_descending_order():
    items = [11, 10, 7, 5, 3, 1]
    assert my_sort(items) == list(reversed(items))


def test_returns_empty_list_for_empty_sequence():
    assert my_sort([]) == []

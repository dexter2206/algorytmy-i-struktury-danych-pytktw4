from merge import merge


def test_merges_interleaved_sequences():
    first = [-1, 0, 2, 3]
    second = [-2, 1, 4, 5]
    assert merge(first, second) == [-2, -1, 0, 1, 2, 3, 4, 5]


def tests_merges_when_one_sequences_is_strictly_smaller():
    first = [-2, -1, 0]
    second = [1, 2, 3]
    assert merge(first, second) == [-2, -1, 0, 1, 2, 3]


def tests_merges_when_one_sequences_is_empty():
    first = []
    second = [1, 3, 5, 10, 121]
    assert merge(first, second) == [1, 3, 5, 10, 121]


def test_merges_when_sequences_have_common_elements():
    first = [0, 1, 1, 1, 2]
    second = [-1, 0, 1, 1, 3, 4]
    assert merge(first, second) == [-1, 0, 0, 1, 1, 1, 1, 1, 2, 3, 4]

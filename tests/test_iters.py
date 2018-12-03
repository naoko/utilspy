from utilspy.iters import flatten, merge_sorted


def test_flatten():
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    assert list(flatten(items)) == list(range(1, 9))


def test_merge_sorted():
    iterables = ([1, 5, 6], [2, 4, 8], [3, 7])
    assert list(merge_sorted(*iterables)) == list(range(1, 9))

import heapq
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    """Flatten nested sequence to a single list of values"""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x, ignore_types)
        else:
            yield x


def merge_sorted(*iterables: list):
    """merge *sorted* sequence together"""
    merged = iterables[0]
    for idx, l in enumerate(iterables[1:]):
        merged = heapq.merge(merged, l)
    return merged

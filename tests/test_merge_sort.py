
from da.sorting.merge_sort import mergesort


def test_merge_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]
    assert mergesort(arr) == [3, 4, 7, 9, 42, 69, 420]

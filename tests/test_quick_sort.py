from da.sorting.quick_sort import quicksort


def test_quick_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]
    assert quicksort(arr) == [3, 4, 7, 9, 42, 69, 420]

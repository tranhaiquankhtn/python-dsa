from da.sorting.insertion_sort import insertion_sort


def test_insertion_sort():
    nums = [9, 3, 7, 4, 69, 420, 42]
    assert insertion_sort(nums) == [3, 4, 7, 9, 42, 69, 420]

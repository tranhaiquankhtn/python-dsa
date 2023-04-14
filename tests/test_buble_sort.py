from da.sorting.buble_sort import bublesort


def test_bubble_sort():
    nums = [9, 3, 7, 4, 69, 420, 42]
    assert bublesort(nums) == [3, 4, 7, 9, 42, 69, 420]

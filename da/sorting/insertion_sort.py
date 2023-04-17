from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    for i, num in enumerate(nums):
        j = i
        while (j > 0 and nums[j] < nums[j-1]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

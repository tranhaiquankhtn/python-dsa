from typing import List


def binary_fn(arr: List[int], target: int) -> bool:
    lo, hi = 0, len(arr)
    while lo < hi:
        m = lo + (hi - lo) // 2
        if arr[m] == target:
            return True
        elif arr[m] < target:
            lo = m + 1
        else:
            hi = m
    return False

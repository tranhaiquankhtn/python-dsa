from typing import List


def quicksort(arr: List[int]) -> List[int]:
    def qs(lo: int, hi: int):
        if lo >= hi:
            return
        pv = partition(lo, hi)
        qs(lo, pv - 1)
        qs(pv + 1, hi)

    def partition(lo: int, hi: int) -> int:
        pv = arr[hi]

        idx = lo - 1
        for i in range(lo, hi):
            if arr[i] <= pv:
                idx += 1
                arr[i], arr[idx] = arr[idx], arr[i]
        idx += 1
        arr[idx], arr[hi] = arr[hi], arr[idx]
        return idx

    qs(0, len(arr) - 1)
    return arr

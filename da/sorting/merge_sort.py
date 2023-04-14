from typing import List


def mergesort(nums: List[int]) -> List[int]:
    def msort(l: int, r: int):
        if l >= r:
            return
        m = (l + r) // 2
        msort(l, m)
        msort(m + 1, r)
        merge(l, r, m)

    def merge(l: int, r: int, m: int):
        i, j = l, m + 1
        list = []
        for k in range(r - l + 1):
            if j > r or (i <= m and nums[i] < nums[j]):
                list.append(nums[i])
                i += 1
            else:
                list.append(nums[j])
                j += 1

        # copy merged array back to original one
        for k in range(len(list)):
            nums[l] = list[k]
            l += 1

    msort(0, len(nums) - 1)
    return nums

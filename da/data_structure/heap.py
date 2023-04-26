import math
from typing import Optional


class MinHeap:
    def __init__(self):
        self.data = []

    def __len__(self) -> int:
        return len(self.data)

    def insert(self, item: int) -> None:
        self.data.append(item)
        self.heapify_up(len(self.data) - 1)

    def poll(self) -> Optional[int]:
        if len(self.data) == 0:
            return None

        min_value = self.data[0]
        if len(self.data) == 1:
            self.data = []
            return min_value

        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_value

    def heapify_up(self, index: int) -> None:
        if index == 0:
            return

        p = self.parent(index)
        if self.data[p] > self.data[index]:
            self.data[p], self.data[index] = self.data[index], self.data[p]
            self.heapify_up(p)

    def heapify_down(self, index: int) -> None:
        l = self.left_child(index)
        r = self.right_child(index)

        if index >= len(self.data) - 1 or l >= len(self.data) - 1:
            return

        if self.data[l] > self.data[r] and self.data[index] > self.data[r]:
            self.data[r], self.data[index] = self.data[index], self.data[r]
            self.heapify_down(r)
        elif self.data[r] > self.data[l] and self.data[index] > self.data[l]:
            self.data[l], self.data[index] = self.data[index], self.data[l]
            self.heapify_down(l)

    def parent(self, idx) -> int:
        return math.floor(idx - 1 / 2)

    def left_child(self, index: int) -> int:
        return index * 2 + 1

    def right_child(self, index: int) -> int:
        return index * 2 + 2

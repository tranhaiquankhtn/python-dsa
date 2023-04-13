from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.prev: Optional[Node] = None


class Stack(Generic[T]):
    def __init__(self):
        self.length = 0
        self.head: Optional[Node] = None

    def push(self, val: T):
        node = Node(val)
        self.length += 1
        if not self.head:
            self.head = node
            return
        node.prev = self.head
        self.head = node

    def pop(self) -> Optional[T]:
        if not self.head:
            return None

        self.length -= 1

        head = self.head
        self.head = head.prev
        head.prev = None

        return head.val

    def peek(self) -> Optional[T]:
        if self.head:
            return self.head.val
        return None

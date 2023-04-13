
from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class Queue(Generic[T]):
    def __init__(self):
        self.length = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def enqueue(self, item: T):
        node = Node(item)
        self.length += 1
        if not self.tail:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def deque(self) -> Optional[T]:
        if not self.head:
            return None

        self.length -= 1
        if self.length == 0:
            tmp = self.head
            self.head = self.tail = None
            return tmp.val

        head = self.head
        self.head = head.next
        head.next = None
        return head.val

    def peek(self) -> Optional[T]:
        if self.head:
            return self.head.val
        return None

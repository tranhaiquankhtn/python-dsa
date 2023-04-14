from typing import Generic, Optional
from da.types import T


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.next: Optional[Node] = None


class SinglyLinkedList(Generic[T]):
    def __init__(self):
        self.length = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, val: T):
        node = Node(val)
        self.length += 1
        if not self.tail:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def prepend(self, val: T):
        node = Node(val)
        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head = node

    def remove(self, val: T) -> Optional[T]:
        prev = cur = self.head
        while cur:
            if val == cur.val:
                break
            prev = cur
            cur = cur.next
        return self.remove_node(cur, prev)

    def remove_at(self, index: int) -> Optional[T]:
        if index > self.length:
            return None

        prev = cur = self.head
        i = 0
        while cur and i < index:
            prev = cur
            cur = cur.next
            i += 1
        return self.remove_node(cur, prev)

    def remove_node(self,
                    cur: Optional[Node],
                    prev: Optional[Node]) -> Optional[T]:
        if not cur:
            return None

        self.length -= 1
        if cur == self.head:
            self.head = cur.next

        if cur == self.tail:
            self.tail = prev

        if prev:
            prev.next = cur.next

        return cur.val

    def get(self, index: int) -> Optional[T]:
        node = self.get_at(index)
        if node:
            return node.val
        return None

    def get_at(self, index: int) -> Optional[Node]:
        if index > self.length:
            return None

        i = 0
        cur = self.head
        while cur and i < index:
            cur = cur.next
            i += 1

        return cur

from typing import Generic, Optional
from da.types import T


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class DoublyLinkedList(Generic[T]):
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

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def prepend(self, val: T):
        node = Node(val)
        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    # get node by index
    def get(self, index: int) -> Optional[T]:
        node = self.get_at(index)
        if node:
            return node.val
        return None

    def get_at(self, index: int) -> Optional[Node]:
        if index > self.length:
            return None

        i, cur = 0, self.head
        while cur and i < index:
            cur = cur.next
            i += 1
        return cur

    def get_node(self, val: T) -> Optional[Node]:
        cur = self.head
        while cur:
            if val == cur.val:
                break
            cur = cur.next
        return cur

    def remove(self, val: T) -> Optional[T]:
        node = self.get_node(val)
        return self.remove_node(node)

    def remove_at(self, index: int) -> Optional[T]:
        node = self.get_at(index)
        return self.remove_node(node)

    def remove_node(self, node: Optional[Node]) -> Optional[T]:
        if not node:
            return None

        self.length -= 1
        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        node.next = node.prev = None
        return node.val

from typing import Optional, Dict
from da.types import Node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.mappings: Dict[str, Node] = {}
        self.reversed_mapping: Dict[Node, str] = {}

    def get(self, k: str) -> Optional[int]:
        node: Node = self.mappings.get(k)
        if not node:
            return None

        self.detach(node)
        self.prepend(node)
        return node.value

    def update(self, k: str, v: int) -> None:
        node: Node = self.mappings.get(k)
        if not node:
            node = Node(v)
            self.mappings[k] = node
            self.reversed_mapping[node] = k
            self.prepend(node)
            self.trim()

        self.detach(node)
        self.prepend(node)

    def detach(self, node: Node) -> None:
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if len(self.mappings) == 1:
            self.head = self.tail = None

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev

        node.next = None
        node.prev = None

    def prepend(self, node: Node) -> None:
        if not self.head:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def trim(self) -> None:
        if len(self.mappings) > self.capacity:
            k = self.reversed_mapping.get(self.tail)
            if not k:
                return
            del self.mappings[k]
            del self.reversed_mapping[self.tail]
            self.detach(self.tail)

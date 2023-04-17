from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class BinaryTreeNode(Generic[T]):
    def __init__(self, val: T,
                 left: Optional['BinaryTreeNode'] = None,
                 right: Optional['BinaryTreeNode'] = None):
        self.val: T = val
        self.left: Optional[BinaryTreeNode] = left
        self.right: Optional[BinaryTreeNode] = right


class GraphEdge:
    def __init__(self, to: int, weight: int):
        self.to = to
        self.weight = weight

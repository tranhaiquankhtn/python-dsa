
from typing import Optional
from da.types import BinaryTreeNode


def bfs(root: Optional[BinaryTreeNode], needle: int) -> bool:
    if not root:
        return False

    return root.val == needle or bfs(root.left, needle) or bfs(root.right, needle)

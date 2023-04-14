from typing import Optional
from da.types import BinaryTreeNode


def dfs(root: Optional[BinaryTreeNode], needle: int) -> bool:
    if not root:
        return False

    if root.val == needle:
        return True

    if root.val < needle:
        return dfs(root.right, needle)
    return dfs(root.left, needle)

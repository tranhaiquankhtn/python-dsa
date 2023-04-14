from typing import Optional
from da.types import BinaryTreeNode


def compare(root1: Optional[BinaryTreeNode],
            root2: Optional[BinaryTreeNode]) -> bool:
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False
    return root1.val == root2.val and compare(root1.left, root2.left) and compare(root1.right, root2.right)

from typing import List, Optional
from da.types import BinaryTreeNode


def bt_pre_order(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []
    return [root.val] + bt_pre_order(root.left) + bt_pre_order(root.right)


def bt_pre_order_iterative(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    res, stack = [], [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)

        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return res


def bt_in_order(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []
    return bt_in_order(root.left) + [root.val] + bt_in_order(root.right)


def bt_in_order_iterative(root: Optional[BinaryTreeNode]) -> List[int]:
    res, stack = [], []

    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

    return res


def bt_post_order(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []
    return bt_post_order(root.left) + bt_post_order(root.right) + [root.val]


def bt_post_order_iterative(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    res, stack = [], [root]
    while stack:
        cur = stack.pop()
        res.insert(0, cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res

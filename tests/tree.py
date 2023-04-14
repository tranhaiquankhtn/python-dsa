from da.types import BinaryTreeNode


tree1: BinaryTreeNode[int] = BinaryTreeNode[int](
    20,
    right=BinaryTreeNode(
        50,
        right=BinaryTreeNode(
            100),
        left=BinaryTreeNode(
            30,
            right=BinaryTreeNode(
                45),
            left=BinaryTreeNode(
                29)
        )
    ),
    left=BinaryTreeNode(
        10, right=BinaryTreeNode(15),
        left=BinaryTreeNode(
            5,
            right=BinaryTreeNode(7),
        ),
    )
)


tree2: BinaryTreeNode[int] = BinaryTreeNode[int](
    20,
    right=BinaryTreeNode(
        50,
        left=BinaryTreeNode(
            30,
            right=BinaryTreeNode(
                45,
                right=BinaryTreeNode(49)
            ),
            left=BinaryTreeNode(
                29,
                left=BinaryTreeNode(21)
            )
        )
    ),
    left=BinaryTreeNode(
        10,
        right=BinaryTreeNode(15),
        left=BinaryTreeNode(
            5,
            right=BinaryTreeNode(7)
        )
    )
)

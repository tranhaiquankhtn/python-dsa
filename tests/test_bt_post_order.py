from da.tree.traverse import bt_post_order, bt_post_order_iterative
from .tree import tree1


def test_bt_post_order():
    assert bt_post_order(tree1) == [
        7,
        5,
        15,
        10,
        29,
        45,
        30,
        100,
        50,
        20,
    ]


def test_bt_post_order_iterative():
    assert bt_post_order_iterative(tree1) == [
        7,
        5,
        15,
        10,
        29,
        45,
        30,
        100,
        50,
        20,
    ]

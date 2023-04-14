from da.tree.traverse import bt_in_order, bt_in_order_iterative
from .tree import tree1


def test_bt_in_order():
    assert bt_in_order(tree1) == [
        5,
        7,
        10,
        15,
        20,
        29,
        30,
        45,
        50,
        100,
    ]


def test_bt_in_order_iterative():
    assert bt_in_order_iterative(tree1) == [
        5,
        7,
        10,
        15,
        20,
        29,
        30,
        45,
        50,
        100,
    ]

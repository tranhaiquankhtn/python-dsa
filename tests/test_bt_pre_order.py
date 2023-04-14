from da.tree.traverse import bt_pre_order, bt_pre_order_iterative
from .tree import tree1


def test_bt_pre_order():
    assert bt_pre_order(tree1) == [
        20,
        10,
        5,
        7,
        15,
        50,
        30,
        29,
        45,
        100,
    ]


def test_bt_pre_order_iterative():
    assert bt_pre_order_iterative(tree1) == [
        20,
        10,
        5,
        7,
        15,
        50,
        30,
        29,
        45,
        100,
    ]

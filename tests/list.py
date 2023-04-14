from typing import Any


def test_list(list: Any):
    list.append(5)
    list.append(7)
    list.append(9)

    assert list.get(2) == 9
    assert list.remove_at(1) == 7
    assert list.length == 2

    list.append(11)
    assert list.remove_at(1) == 9
    assert list.remove(9) is None
    assert list.remove_at(0) == 5
    assert list.remove_at(0) == 11
    assert list.length == 0

    list.prepend(5)
    list.prepend(7)
    list.prepend(9)

    assert list.get(2) == 5
    assert list.get(0) == 9
    assert list.remove(9) == 9
    assert list.length == 2
    assert list.get(0) == 7

from da.searching.binary_search import binary_fn


def test_binary_search_array():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_fn(foo, 69) is True
    assert binary_fn(foo, 1336) is False
    assert binary_fn(foo, 69420) is True
    assert binary_fn(foo, 69421) is False
    assert binary_fn(foo, 1) is True
    assert binary_fn(foo, 0) is False

from da.searching.bt_bfs import bfs
from .tree import tree1


def test_bt_bfs():
    assert bfs(tree1, 45) is True
    assert bfs(tree1, 7) is True
    assert bfs(tree1, 69) is False

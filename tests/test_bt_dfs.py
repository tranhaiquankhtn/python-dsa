
from da.searching.bt_dfs import dfs
from .tree import tree1


def test_bt_dfs():
    assert dfs(tree1, 45) is True
    assert dfs(tree1, 7) is True
    assert dfs(tree1, 69) is False

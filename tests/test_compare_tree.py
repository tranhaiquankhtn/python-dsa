
from da.tree.compare import compare
from .tree import tree1, tree2


def test_compare():
    assert compare(tree1, tree1) is True
    assert compare(tree1, tree2) is False
